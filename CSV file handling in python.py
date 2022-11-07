# Reading CSV files in python


import csv
 
# opening the CSV file
with open('Giants.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  for lines in csvFile:
        print(lines)


# OR using dictreader class
It is similar to the previous method, the CSV file is first opened using the
open() method then it is read by using the DictReader class of csv module
which works like a regular reader but maps the information in the CSV file
into a dictionary.

The very first line of the file consists of dictionary keys.

import csv
 
# opening the CSV file
with open('Giants.csv', mode ='r') as file:   
        
       # reading the CSV file
       csvFile = csv.DictReader(file)
 
       # displaying the contents of the CSV file
       for lines in csvFile:
            print(lines)


# Writing CSV files in Python

Using csv.writer class
Using csv.DictWriter class


writerow() and writerows() 2 methods to write single
line and multiple lines together.


import csv 
    
# field names 
fields = ['Name', 'Branch', 'Year', 'CGPA'] 
    
# data rows of csv file 
rows = [ ['Nikhil', 'COE', '2', '9.0'], 
         ['Sanchit', 'COE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'SE', '1', '9.5'], 
         ['Prateek', 'MCE', '3', '7.8'], 
         ['Sahil', 'EP', '2', '9.1']] 
    
# name of csv file 
filename = "university_records.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)




Writing from a dictionary :

Writeheader() method to write 1st row

import csv 
    
# my data rows as dictionary objects 
mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'}, 
         {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'}, 
         {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'}, 
         {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'}, 
         {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'}, 
         {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}] 
    
# field names 
fields = ['name', 'branch', 'year', 'cgpa'] 
    
# name of csv file 
filename = "university_records.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader()    #no argument as it is passed above already
        
    # writing data rows 
    writer.writerows(mydict) 
