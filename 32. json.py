"""
JSON is trst, written with javascript object notation.
JSON is a syntax for storing and exchanging data.
Python has a built-in package called json, which can be used to work with JSON data.
If we have a JSON string, we can parse it by using the json.loads() method.
If we have a python object, we can convert it into a json string by using the json.dumps() method.
Following types object can convert into JSON strings:
    dict, list, tuple, string, int, float, True, False, None

"""
"""
parsing a python string by using json.loads():
"""
import json
x = ' {"name": "John", "age": 30, "city": "New YOrk" }'
y = json.loads(x)
print(y["age"])

"""
Convert from python to JSON using json.dumps().
"""
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)
print(y)

