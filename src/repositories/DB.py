import os, json
from typing import Any


def modify(name: str, key: str, field: str, data: Any) -> None:
    """
    Use to modify a specific field.

    name -- name of json file.\n
    key -- key of element you want to modify.\n
    field -- field name.\n
    data -- data to record old data.
    """
    dic = db(name)
    dic[key][field] = data
    save(name, dic)

def modify_vect(name: str, key: str, field: str, position: int, data: Any) -> None:
    """
    Use to modify a specific vector position in a field

    name -- name of json file.\n
    key -- key of element you want to modify.\n
    field -- field name.\n
    position -- vector field position \n
    data -- data to record old data.
    """
    dic = db(name)
    dic[key][field][position] = data
    save(name, dic)

def consult(name: str, key: str, field: str) -> Any:
    """
    Use to consult data in a field
    """
    dic = db(name)
    return dic[key][field]

def insert(name: str, element: dict) -> None:
    """
    Use to insert a new element into a json file
    """
    dic = db(name)
    dic.update(element)
    save(name, dic)

def delete(name: str, key: str) -> None:
    """
    Use to delete a element from json file
    """
    dic = db(name)
    dic.pop(key)
    save(name, dic)

def delete_all(name: str) -> None:
    """
    Use to clear json file
    """
    dic = db(name)
    dic.clear()
    save(name, dic)

def db(name: str) -> dict:
    """
    Use to get a dict from json file
    """
    dic = {}
    if os.path.exists('src/repositories/BD/' + str(name) + '.json'):
        with open('src/repositories/BD/' + str(name) + '.json') as f:
            try:
                dic = json.load(f)
            except:
                pass
    return dic

def save(name: str, dic: dict) -> None:
    """
    Use to save a dict into file
    """
    with open('src/repositories/BD/' + str(name) + '.json', 'w') as f:
        json.dump(dic, f)
