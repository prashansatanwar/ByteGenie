import axios from "axios";

const URL = process.env.REACT_APP_APIURL

export async function sendQuery(userQuery) {
    var config = {
        method: 'POST',
        url: URL + 'submit',
        headers: {
            'Content-Type': 'application/json'
        },
        data: userQuery
    };

    try {
        const response = await axios(config);
        return response.data;
    } catch (error) {
        console.error("There was an error! ", error);
    }

}
