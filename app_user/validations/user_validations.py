from app_user.models.user_models import User

def validate_login(value,flag):
    if isinstance(value,str) == False:
        return "Login digitado não é do tipo String."
    if flag  == "creation":
        if User.query.filter_by(login=value).first() != None:
            return "Login já cadastrado, por favor selecione outro."

    return True

def validate_name(value):
    if isinstance(value,str) == False:
        return "O nome digitado não é do tipo String."
    else:
        return True

def validate_password(value):
    if isinstance(value,str) == False:
        return "A senha digitada não é do tipo String."
    
    if value.size < 8:
        return "A senha precisa ter no mínimo 8 digitos."

    return True

def validate_creation_data(data:dict):
    result_login = validate_login(data['login'],'creation')
    if result_login != True:
        return result_login

    result_name = validate_name(data['name'])
    if result_name != True:
        return result_name 

    result_password = validate_password(data['password'])
    if result_password != True:
        return result_password

    return True           

def validate_update_data(data:dict):
    result_login = validate_login(data['login'],'update')
    if result_login != True:
        return result_login

    result_name = validate_name(data['name'])
    if result_name != True:
        return result_name 

    result_password = validate_password(data['password'])
    if result_password != True:
        return result_password

    return True