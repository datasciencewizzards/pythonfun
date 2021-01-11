# import JSON package

import json

# Convert JSON to Python object : Python dictionary

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print("Person {} has age {}".format(y["name"], y["age"]));

# Convert Python object - Dictionary to String

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print("String conversion of a python object {}", y)


# Convert various python datatypes into Strings

def printCustom(x):
    print("DataType {} has string value {}".format(type(x), x))


printCustom(json.dumps({"name": "John", "age": 30}))
printCustom(json.dumps(["apple", "bananas"]))
printCustom(json.dumps(("apple", "bananas")))
printCustom(json.dumps("hello"))
printCustom(json.dumps(42))
printCustom(json.dumps(31.76))
printCustom(json.dumps(True))
printCustom(json.dumps(False))
printCustom(json.dumps(None))

# Format the results

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x,indent=10)

print("JSON with formatting {}".format(y))


y = json.dumps(x, indent=4, separators=("$$", ":"))
print("JSON with formatting {}".format(y))

y = json.dumps(x, indent=4,sort_keys=True, separators=("$$", ":"))
print("JSON with formatting {}".format(y))

