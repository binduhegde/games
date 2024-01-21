# https://opentdb.com/api.php
import requests
from quiz_setup import Setup
import time 

#############################################################################
#* THIS FILE IS RESPONSIBLE FOR REQUESTING THE DATA THROUGH API AND
#* STORING IT IN A LIST CALLED QUESTION_DATA WHICH WE WILL IMPORT IN MAIN.PY
#############################################################################

# this is from quiz_setup.py
setup = Setup()
result = setup.result
# this is the category code in the opentdb.com
categories_dict = {'General Knowledge':9, 'Books':10, 'Films':11, 'Music':12, 'Computer Science':18, 'Mathametics':19, 'Sports':21, 'History':23, 'Politics':24, 'celebrities':26, 'Animals':27}

parameters = {
    'difficulty': result['difficulty'].lower(),
    'amount': result['amount'],
    'type': 'multiple',
    'category': categories_dict[result['category']]
}

def request_data():
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    return response.json()

data = request_data()
# code 1 means that opendtb doesn't have asked number of quesitons in which case it will send an empty result
if data['response_code'] == 1:
    # we just ignore the difficulty level in that case so that it'll send enough data now
    parameters.pop('difficulty')
    # opentdb has restricted requests to 1 requestion per 5 secs. so we are waiting 5 secs before requesting once again
    time.sleep(5)
    data = request_data()

# storing the questions here. eg:
# question_data = [{'question':'how many', 'options':[1,2,3,4], 'correct_answer':4}]
# the option values are not shuffled so the correct ans is always the last one
question_data = []
for i in data['results']:
    question_data.append({"question": i['question'], "options":i['incorrect_answers']+[i['correct_answer']], "correct_answer":i['correct_answer']})
