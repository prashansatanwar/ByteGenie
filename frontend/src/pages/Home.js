import React, { useState } from 'react'
import { sendQuery } from '../service/Api';

function Home() {
    const [query, setQuery] = useState("");
    const [result, setResult] = useState(null);
    const [columnNames, setColumnNames] = useState([]);
    const [data, setData] = useState([]);

    const [loading, setLoading] = useState(false);

    const [alert, setAlert] = useState("");

    function handleChange(e) {
        e.preventDefault();
        const input = e.target.value;
        setQuery(input);
    }

    async function handleSubmit() {
        if(!query) {
            setAlert("You need to provide a query to execute.")
            return;
        }
        
        setAlert("");
        setResult(null);
        setLoading(true);
        const response = await sendQuery(query);

        setResult(response.result);
        setColumnNames(response.result.column_names);
        setData(response.result.data);

        setLoading(false);
    }
    function  handleKeyDown (e) {
        if (e.key === 'Enter') {
          handleSubmit();
        }
      }

    return (
        <div className='h-screen w-full p-10 bg-[#f1e3d3] flex flex-col items-center '>
            <p className='text-2xl mb-8 text-left font-medium'>
                ByteGenie: Natural Language to SQL Query
            </p>
            
            <div className='w-3/4 flex' >
                <input required type='text' className='w-full h-[3em] outline-none bg-transparent border-2 border-black hover:border-slate-600 px-2 ' value={query} onChange={handleChange} onKeyDown={handleKeyDown}/>
                <button onClick={handleSubmit} className='px-2 ml-2  w-[2em] aspect-square rounded-full hover:shadow-lg' >
                    GO
                </button>
            </div>

            <div className='flex-grow w-full mt-10 px-2 overflow-auto'>

                {result ?
                    <div className='pt-4 '>
                        <table>
                            <thead className='h-[2em] border-b-4 border-black border-double'>
                                <tr>
                                {columnNames.map((colName, index) => (
                                    <th key={index} className='mx-2 px-2 uppercase'>{colName}</th>
                                ))}
                                </tr>
                            </thead>
                            <tbody>
                                {data.map((row, rowIndex) => (
                                <tr key={rowIndex} className=''>
                                    {row.map((cell, cellIndex) => (
                                        <td key={cellIndex} className='mx-2 px-2'>
                                            <p className='h-20 overflow-auto'>
                                                {cell}
                                            </p>
                                        </td>
                                    ))}
                                </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                    :
                    <div className='h-full flex items-center justify-center'>
                        {
                            loading && 
                            <p> 
                                Searching...
                            </p>
                        }

                        {
                            alert && 
                            <p>
                                {alert}
                            </p>
                        }
                    </div>
                }
            </div>


        </div>
    )
}

export default Home