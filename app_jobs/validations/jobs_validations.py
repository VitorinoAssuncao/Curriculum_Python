import requests
import json
import datetime

def validate_user_id(user_id:int):
    result_from_request = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
    print(result_from_request.status_code)
    if result_from_request.status_code != 200:
        return "Usuário não encontrado"
    
    if isinstance(user_id,int) != True:
        return "Código de Usuário em formato invalido."

    return True 

def validate_dates(date_begin,date_out):
    new_date_begin = datetime.date.fromisoformat(date_begin)
    new_date_out = datetime.date.fromisoformat(date_out)
    if new_date_begin >= new_date_out:
        return "A data de saída não pode ser menor ou igual a data de entrada."

    if new_date_out > datetime.date.today():
        return "A data de saída não pode ser superior a hoje."

    if new_date_begin > datetime.date.today():
        return "A data de ínicio não pode ser superior a hoje."

    return True

def validate_enterprise(enterprise:str):
    if len(enterprise) < 1 :
        return "O campo de empresa deve ser preenchido."

    if isinstance(enterprise,str) != True:
        return "O campo de empresa está sendo enviado no formato incorreto."

    return True

def validate_function(function:str):
    if len(function) < 1 :
        return "O campo de função deve ser preenchido."

    if isinstance(function,str) != True:
        return "O campo de função está sendo enviado no formato incorreto."

    return True

def validate_activities(activities:str):
    if len(activities) < 1 :
        return "O campo de atividades exercidas deve ser preenchido."

    if isinstance(activities,str) != True:
        return "O campo de atividades exercidas está sendo enviado no formato incorreto."

    return True


def validate_jobs_data(data_jobs:dict):
    result_user_id = validate_user_id(data_jobs['user_id'])
    if result_user_id != True:
        return result_user_id

    result_dates = validate_dates(data_jobs['date_begin'],data_jobs['date_out'])
    if result_dates != True:
        return result_dates

    result_enterprise = validate_enterprise(data_jobs['enterprise'])
    if result_enterprise != True:
        return result_enterprise

    result_function = validate_function(data_jobs['function'])
    if result_function != True:
        return result_function

    result_activities = validate_activities(data_jobs['activities'])
    if result_activities != True:
        return result_activities

    return True

