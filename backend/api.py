from flask import request, Blueprint, jsonify
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI
import os
import json
from dotenv import load_dotenv

from db import execute_query
from prompt import bot_sql

full_database_docs = bot_sql

load_dotenv()

llm = GoogleGenerativeAI(model='gemini-pro', google_api_key=os.environ.get('GEMINI_API_KEY'))

api = Blueprint('api', __name__)

def get_query_from_llm(user_query):
    messages = [
        {"role": "system", "content": "You are an assistant familiar with the following Database documentation: " + full_database_docs},
        {"role": "user", "content": user_query},
    ]
    response = llm.invoke(messages)
    return json.loads(response)["query"]


@api.route("/submit", methods=['POST'])
def submit():
    user_query = request.get_json()

    sql_query = get_query_from_llm(user_query)
    result = execute_query(sql_query)
    response = {"message": "Query recieved", "result":result}

    return jsonify(response)
