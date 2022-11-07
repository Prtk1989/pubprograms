# Pickle module
#Pickle in Python is primarily used in serializing and deserializing Python object
#structure. In other words, it’s the process of converting a Python object into
#a byte stream to store it in a file/database, maintain program state across
#sessions, or transport data over the network. The pickled byte stream can be
#used to re-create the original object hierarchy by unpickling the stream.
#This whole process is similar to object serialization in Java or .Net.

import pickle

def storeData():
    # initializing data to be stored in db
    Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',
    'age' : 21, 'pay' : 40000}
    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
    'age' : 50, 'pay' : 50000}
  
    # database
    db = {}
    db['Omkar'] = Omkar
    db['Jagdish'] = Jagdish
      
    # Its important to use binary mode
    dbfile = open('examplePickle', 'ab')
      
    # source, destination
    pickle.dump(db, dbfile)                     
    dbfile.close()
  
def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')     
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()
  
if __name__ == '__main__':
    storeData()
    loadData()
    
#output
'''
python P60_PickleModule.py
Omkar => {'age': 21,  'name': 'Omkar Pathak',  'key': 'Omkar',  'pay': 40000}
Jagdish => {'age': 50,  'name': 'Jagdish Pathak',  'key': 'Jagdish',  'pay': 50000}
'''
######## OR ##########

# initializing data to be stored in db
Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 
'age' : 21, 'pay' : 40000}
Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
'age' : 50, 'pay' : 50000}
  
# database
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish
  
# For storing
b = pickle.dumps(db)       # type(b) gives <class 'bytes'>
  
# For loading
myEntry = pickle.loads(b)
print(myEntry)

