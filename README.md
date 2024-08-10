# Introduction
This is an AI-powered data interaction application. This application allows user to use natural language to fetch data from a database. This is a tool that will enable users that does not possess SQL expertise to interact with the data, making the data more accessible to a wider set of audience.

# Backend 

## Techstack
1. Python
2. MySQL
   
## Installation and setup
1. Install the requirements using the following command: `pip install -r ./backend/requirements.txt`
2. Get the `GEMINI_API_KEY` by following instructions mentioned [here](https://aistudio.google.com/app/apikey).
3. Create a _.env_ file and setup the environment variables:
   1. DB_USERNAME
   2. DB_PASSWORD
   3. DB_HOST
   4. DB_PORT 
   5. GEMINI_API_KEY
4. To initialize the database, run the _db.py_ file : `python ./backend/db.py`
5. Run the API server: `python ./backend/app.py`

## Data
Minimal data processing was applied to parse the data provided from csv files into the MySQL database. 
1. Modified the number of employees field by taking the average of the range provided 
2. Modified the string in company revenue field to a float


## API
The app uses flask to create and serve endpoints. 
1. POST /submit: 
Recieves the query text in plain english through the body of the request and returns the queried data.

# Frontend
The frontend uses the /submit API endpoint provided by the backend to query data.
## Techstack
1. React JS
2. TailwindCSS
   
## Installation and setup
1. Navigate to the frontend directory.
2. Install the libraries: `npm install`
3. Start a server: `npm start`

## Interacting with the UI
1. Enter a user query in the textbox visible. 
2. Click on GO to get the results.

# Challenges faced
**Prompt Engineering**: Writing a generalized prompt for the LLM proved to be challenging. Initially the LLM was responding with either invalid SQL queries or incorrect ones. Providing examples in the prompt helped the LLM learn what kind of output is required. Deviating too far from the examples sometimes gives a poorly generated query. Through out the Query the LLM needs to be reminded to return the output in the correct format. 


# Future Scope
## Improving the UI
1. A better format to view the data can be added instead of using the table directly. 
2. Alerts can be added for when there is no available data.
## Improving the Backend
1. Prompt could be improved to consider more scenarios.
2. The database schema used can be enhanced to make the data easy to query.
3. Query retries can be added incase of failure scenarios (eg: LLM returns an invalid response).
4. Unit tests can be added.
