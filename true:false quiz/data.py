# https://opentdb.com/api.php
import requests
from quiz_setup import Setup
import time 

setup = Setup()
result = setup.result
categories_dict = {'General Knowledge':9, 'Books':10, 'Films':11, 'Music':12, 'Computer Science':18, 'Mathametics':19, 'Sports':21, 'History':23, 'Politics':24, 'celebrities':26, 'Animals':27}

parameters = {
    'difficulty': result['difficulty'].lower(),
    'amount': result['amount'],
    'type': 'boolean',
    'category': categories_dict[result['category']]
}

def request_data():
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    return response.json()

data = request_data()
if data['response_code'] == 1:
    parameters.pop('difficulty')
    time.sleep(5)
    data = request_data()

question_data = []
for i in data['results']:
    question_data.append({"question": i['question'], "correct_answer":i['correct_answer']})
