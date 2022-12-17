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

def load_handwriting(filename_without_format: str, py_file = False):
    if py_file:
        from handwritings.miquy import miquy
        return miquy

    with open("handwritings\\" + filename_without_format + ".json", 'r') as f:
        data = json.load(f)
    return data