#Hyper text transfer protocol
'''Is a standard protocol to communicate on web'''

#Requests module
'''
Library to send http requests
Used to connect to API's and send and recieve data in json format
'''

#Http requests - CRUD
'''
GET     -> To Fetch data from the server
POST    -> To send data to server
PUT     -> To update existing data
DELETE  -> To remove data
'''

#%%
#GET
import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)
print(response.json())

# %%
#POST
import requests
url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title":"abc",
    "body":"Sai"
}

response = requests.post(url,data)
print(response.json())

# %%
#PUT
import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

data ={
    "id":101,
    "title": "pranith",
    "body": "sai"
}

response = requests.put(url,data)
print(response.json())

# %%
#DELETE
import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)
print(response.status_code)

# %%
#Parameters
'''Request header - To display extra information'''
