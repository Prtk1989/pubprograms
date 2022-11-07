# JSON File handling in python


# 1 # Python program to convert JSON to Python
 
 
import json
 
# JSON string
employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'
 
# Convert string to Python dict
employee_dict = json.loads(employee)
print(employee_dict)
 
print(employee_dict['name'])



# 2 # Python program to read json file
  
  
import json
  
# Opening JSON file
f = open('data.json',)
  
# returns JSON object as
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)
  
# Closing file
f.close()


# 3 # Python program to convert Python to JSON
  
  
import json
  
# Data to be written
dictionary ={
  "id": "04",
  "name": "sunil",
  "department": "HR"
}
  
# Serializing json
json_object = json.dumps(dictionary, indent = 4)
print(json_object)


# Python program to write JSON
# to a file
  
  
import json
  
# Data to be written
dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}
  
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)




# 4 # Python program to update JSON
 
 
import json
  
# JSON data:
x =  '{ "organization":"GeeksForGeeks",
        "city":"Noida",
        "country":"India"}'
 
# python object to be appended
y = {"pin":110096}
 
# parsing JSON string:
z = json.loads(x)
  
# appending the data
z.update(y)
 
# the result is a JSON string:
print(json.dumps(z))



# 5 # Python program to update JSON
 
 
import json
 
 
# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended
y = {"emp_name":"Nikhil",
     "email": "nikhil@geeksforgeeks.org",
     "job_profile": "Full Time"
    }
     
write_json(y)
