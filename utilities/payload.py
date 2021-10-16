from utilities.configurations import *


def addpetpayloadDefault():
    body = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    return body


def addpetpayload(name, status):
    body = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": name,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": status
    }
    return body