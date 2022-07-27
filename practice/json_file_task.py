import json

###
def write_dict_to_json_file(file_name:str, obj:dict):
    if not file_name.endswith(".json"):
        raise ValueError()
    obj["password"] = str(obj['password'])[::-1]
    j=json.dumps(obj)
    with open(file_name, 'w') as file: 
        file.write(j)

###
def read_dict_from_file(file_name)->dict:
    with open(file_name, 'r') as file:
        obj = dict(json.loads(file.read()))
        if 'password' in obj.keys():
            obj['password'] = str(obj['password'])[::-1]
        return obj
    
    

user = {
    'login': 'bloodSkill1w',
    'password': '1256'
}
# write_dict_to_json_file('radik.json', user)
print(read_dict_from_file("radik.json"))