# Python HTTP Request module

#pip install requests (install reuests module first then import it)

import requests

url = "http://github.com"


response = requests.get(url)

print response.content
print response.header
print response.cookies
print response.is_redirect #returns true if the request was redirected
print response.json #will give a dictionary then you can get all key value pairs
print response.url
print response.text
print response.status_code
response.close() #close the connection to the server


2. get using authentication

response = request.get(url,auth=("prateek","agnihotri"))
print response.status_code # if 200 means it was successful, 403 means not successful

or

from requests.auth import HTTPBasicAuth
  
response = requests.get(url,auth = HTTPBasicAuth('user', 'pass'))


3. get using certificate

response = requests.get(url, verify ='/path/to/certfile')

4. use timeout

response = requests.get(url,timeout=1.0)   #in seconds

5. redirect
#first, make a request without setting the 'allow_redirects' parameter to False:
myobj = {'username':'xyz','password':'123'}
x = requests.post(url, data = myobj)
print(x.text)

result_dictionary = x.json()


print("----------------")

#then, make a request with the 'allow_redirects' parameter set to False:
x = requests.post(url, data = myobj, allow_redirects=False)
print(x.text)

#post example
import requests
>>> api_url = "https://jsonplaceholder.typicode.com/todos"
>>> todo = {"userId": 1, "title": "Buy milk", "completed": False}
>>> response = requests.post(api_url, json=todo)   #preferred way is to use json= <dictionary>
>>> response.json()
{'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

>>> response.status_code
201



6. Session object #so that future request can be sent to same session object, no need to open a new session everytime

s= request.Session()

#now send repeated requests using s object to same server

response = s.get(url)

7. Difference between put and post


(i)Post is used to create new objects

Put will create new object when sent for the 1st time if object doesn't exist
next time it will just update same object.

(ii) post is not idempotent means, n post request will try to create n objects

put is idempotent , n request will be considered as single update req

(iii) in PUT call there will be endpoint+id sent in the api call but 
in post call there will be just endpoint mentioned in the url to create the resource

8. PUT vs PATCH
The main difference between the PUT and PATCH method is that the PUT method
uses the request URI to supply a modified version of the requested resource
which replaces the original version of the resource whereas the PATCH method
supplies a set of instructions to modify the resource. If the PATCH document
is larger than the size of the new version of the resource sent by the PUT
method then the PUT method is preferred.

9. storing response in json dictionary and using it



response = requests.get("https://api.github.com")

out_dict = response.json()
print (out_dict['authorizations_url'])

10. alternates to requests module


(i) import urllib3
(ii) import httplib2
(iii) import httpx

11.  handle access token in headers while making GET call

session = requests.Session()
session.headers.update({'Authorization': 'Bearer {access_token}'})
response = session.get('https://httpbin.org/headers')


12. What are the components of an HTTP request?
An HTTP request have five components. These are:

Action showing HTTP method like GET, PUT, POST, DELETE.
Uniform Resource Identifier (URI): URI is the identifier for the resource on the server.
HTTP version: Indicate the HTTP version like- HTTP V1.1.
Request Header: Request Header carries metadata for the HTTP request message. 
Metadata could be a client type, format supported by the client, format of a message body, cache setting etc.
Request Body: Resource body indicates message content or resource representation.

'''
13. What is URI? What is the purpose of web-based service and what is it's format

URI stands for Uniform Resource Identifier. It is a string of characters designed for unambiguous identification of resources and extensibility by the URI scheme. 
The purpose of URI is to locate the resource on the server hosting of the web service.

A URIs format is <protocol>://<service-name>/<Resource Type>/<ResourceID>

'''

14 Which purpose does the OPTIONS method serve for the RESTful Web services?

The OPTIONS Method lists down all the operations of a web service supports. 
It creates read-only requests to the server.


OPTIONS tells you things such as "What methods are allowed for this resource".

HEAD gets the HTTP header you would get if you made a GET request, but without the body. 
This lets the client determine caching information, what content-type would be returned, 
what status code would be returned. The availability is only a small part of it.


15 What are the most commonly used HTTP methods supported by REST?

GET is only used to request data from a specified resource. Get requests can be cached and bookmarked. It remains in the browser history and haS length restrictions. GET requests should never be used when dealing with sensitive data.
POST is used to send data to a server to create/update a resource. POST requests are never cached and bookmarked and do not remain in the browser history.
PUT replaces all current representations of the target resource with the request payload.
DELETE removes the specified resource.
OPTIONS is used to describe the communication options for the target resource.
HEAD asks for a response identical to that of a GET request, but without the response body.

16 REST Architecture

REST stands for representational state transfer and is a software architecture style that defines a pattern for client and server communications over a network. REST provides a set of constraints for software architecture to promote performance, scalability, simplicity, and reliability in the system.

REST defines the following architectural constraints:

a. Stateless: The server won’t maintain any state between requests from the client.

b. Client-server: The client and server must be decoupled from each other, allowing each to develop independently.

c. Cacheable: The data retrieved from the server should be cacheable either by the client or by the server.

d. Uniform interface: The server will provide a uniform interface for accessing resources without defining their representation.

e. Layered system: The client may access the resources on the server indirectly through other layers such as a proxy or load balancer.

f. Code on demand (optional): The server may transfer code to the client that it can run, such as JavaScript for a single-page application.

Note, REST is not a specification but a set of guidelines on how to architect a network-connected software system.


17 DELETE

import requests
>>> api_url = "https://jsonplaceholder.typicode.com/todos/10"
>>> response = requests.delete(api_url)
>>> response.json()
{}

>>> response.status_code
200

18 PATCH, PATCH differs from PUT in that it doesn’t completely replace the existing resource. 
It only modifies the values set in the JSON sent with the request.

import requests
>>> api_url = "https://jsonplaceholder.typicode.com/todos/10"
>>> todo = {"title": "Mow lawn"}
>>> response = requests.patch(api_url, json=todo)
>>> response.json()
{'userId': 1, 'id': 10, 'title': 'Mow lawn', 'completed': True}

>>> response.status_code
200




