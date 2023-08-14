import requests
from datetime import datetime



APP_ID = '897ce1bd'
API_KEY = 'da62b4961577c0ef4b9e016371b57d26'
DATE = datetime.now()
ddmmyyyy = DATE.strftime('%d/%m/%Y')
time = DATE.strftime('%H:%M:%S')

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_input = input('Tell me which exercises did you do today?: ')

header = {
    'x-app-id':APP_ID,
    'x-app-key':API_KEY
}

exercise_params = {
    'query': exercise_input,
    'gender':'male',
    'weight_kg':65,
    'height_cm':181,
    'age':25
}

response = requests.post(url = exercise_endpoint, json = exercise_params, headers=header)
result = response.json()
sheety_url = 'https://api.sheety.co/b986aa330f6b7bd3394167dfe6964521/myWorkouts/workouts'

record = {
    'workout':{
        "date":ddmmyyyy,
        'time':time,
        'exercise':result['exercises'][0]['user_input'].title(),
        'duration':result['exercises'][0]['duration_min'],
        'calories':result['exercises'][0]['nf_calories']
    }
}


end = requests.post(sheety_url, json = record)

print(end.text)

