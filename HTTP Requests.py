# Python HTTP Request module

#pip install requests (install reuests module first then import it)

import requests

url = "http://github.com"


response = request.get(url)

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

response = requests.get(url,timeout=0.001)

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


i) import urllib3
ii) import httplib2
iii) import httpx
