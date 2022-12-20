import json

'''
json file must looks like:
{
    "A": {

    }
}
'''

'''
content may looks like:
{
    "A": {
        "connectable": "down",
        "margin-left": 10,
        "margin-right": 5,
        "curve": [(30, 20), (28, 23), (11, 23), (25, 25)]
    }
}
'''

def load_handwriting(filename_without_format: str):
    with open("handwritings\\" + filename_without_format + ".json", 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data