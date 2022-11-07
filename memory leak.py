#memory leak


https://www.geeksforgeeks.org/memory-leak-in-python-requests/#:~:text=When%20a%20programmer%20forgets%20to,the%20performance%20of%20the%20machine.



import gc


#call any function which assigns values to few variables

print gc.get_objects ()   #prints count of all the objects in the memory 

gc.collect()    #cleans up unused objects from heap memory

print gc.get_objects() #now this count will be less