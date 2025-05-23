import json

#Python to Json and Json to python
'''
1. Json is always with "" double course
2. Lower case is allowed --> true/false
3. If type is Json it will return as str class
'''
#Json is a universal format for data exchange
#Json is a string
#Java Script Object Notion (Json)
#Used to store and exchange data betweeen a server and a client
#Similar to Python dictionary
'''Difference Python Dictionary vs Json
    Type is Dictionary          Type is Json
    Single or Double cots       Double cots only
    Case sensitvie              No Case Senstive (can store true/false with small letters)
    '''

#%%
#To encode, decode data
#Python to Json: Serialization
#Uses "dumps"

import json
data = {"name":"Pranith", "age": 27}
print(json.dumps(data))
type(data)

# %%
#Json to Python: Deserialization
#Uses "loads"

import json
data = '{"name":"Pranith", "age": 27}'
print(json.loads(data))
type(data)


# %%
#API's
''' Purpose of API's
1. Transfer data from client to server
2. To enable applications talk to each other'''

'''
You     ->  Python code
Waiter  ->  API
Kitchen -> Server or Database
'''

#Requests - You need to install requests module
#pip install requests - Command "pip3 install requests"
'''
1. GET      -> To Get data
2. POST     -> To send data'''

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print(response.json())

# %%
#POST
import requests
url = "https://jsonplaceholder.typicode.com/posts"
my_data ={
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response = requests.post(url,json=my_data)
print(response.status_code)
print(response.json())


# %%
#List of public API's
'''
1. https://jsonplaceholder.typicode.com
2. https://openweathermap.org/api
3. https://www.coingecko.com/en/api
4. https://jokeapi.dev/
5. https://newsapi.org/'''