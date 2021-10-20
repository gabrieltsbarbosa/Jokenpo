import os, json
from typing import Any


def modify(name: str, key: str, field: str, data: Any) -> None:
    """
    Modify a specific field in an element, return None.

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
    Modify a specific vector field in an element, return None

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
    Consult data in a field, return requested info  

    name -- name of json file.\n
    key -- key of element you want to modify.\n
    field -- field name.
    """
    dic = db(name)
    return dic[key][field]

def insert(name: str, element: dict) -> None:
    """
    Insert a new element into a json file, return None

    name: name of json file.\n
    element: dict containing the element to be inserted into the json file 
    """
    dic = db(name)
    dic.update(element)
    save(name, dic)

def delete(name: str, key: str) -> None:
    """
    Delete a element from json file, return None

    name -- name of json file.\n
    key -- key of element you want to delete.
    """
    dic = db(name)
    dic.pop(key)
    save(name, dic)

def delete_all(name: str) -> None:
    """
    Clear json file, return None.

    name -- name of json file.
    """
    dic = db(name)
    dic.clear()
    save(name, dic)

def db(name: str) -> dict:
    """
    Get full content from json file in a dict, return dict

    name: name of json file.
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
    Save a dict into file, return None

    name: name of json file.\n
    dic: dict to be saved into the json file 
    """
    with open('src/repositories/BD/' + str(name) + '.json', 'w') as f:
        json.dump(dic, f)
