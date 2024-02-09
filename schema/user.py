from pymongo import MongoClient

db = MongoClient("mongodb://127.0.0.1:27017/")['anyDO']

user_schema = {
    'name': {
        'type': 'string',
        'minlength': 1,
        'required': True,
    },
    'email': {
        'type': 'string',
        "required": True,
    },
    'password': {
        'type': 'string',
        "required": True,
    }
}

