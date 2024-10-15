# case study
# map function is a specified function for each element in iterable.
# filter function is return an iterator where the items are filtered in the function test throw it is correct or not.
# reduce function is powerful tool to performing a cumulative operations in the iterables.
from functools import reduce

# Case study

employees = [{'First_Name':"Lokesh",'Last_Name':'Raju','Age':30},
             {'First_Name':"Sai",'Last_Name':'Hemanth','Age':25},
             {'First_Name':"Pavan",'Last_Name':'Kiran','Age':65},
             {'First_Name':"Akhil",'Last_Name':'Salagala','Age':53},
             {'First_Name':"satya",'Last_Name':'krishna','Age':28},
             {'First_Name':"Raj",'Last_Name':'Kumar','Age':26},
             {'First_Name':"Saddam",'Last_Name':'Hussain','Age':45},
             {'First_Name':"Subhani",'Last_Name':'Mabu','Age':25},
             {'First_Name':"Guna",'Last_Name':'Sekhar','Age':29},
             {'First_Name':"Madhan",'Last_Name':'Mohan','Age':49},
             {'First_Name':"Khadar",'Last_Name':'Basha','Age':50},
             {'First_Name':"Prasanth",'Last_Name':'Chanti','Age':32},
             {'First_Name':"Surendra",'Last_Name':'Patti','Age':33},
             {'First_Name':"Kishore",'Last_Name':'kumar','Age':38}]

# Write first name and last name only

print(list(map(lambda x:x['First_Name']+x['Last_Name'],employees)))
# i want the age is less than 40

print(list(filter(lambda x:x['Age']<40,employees)))


# Reduce(function, Iterable)
#Task1:-

lst = [12, 13, 29, 50, 1]
print(reduce(lambda x,y:x+y,lst ))

#Task2:- Find the lowest value

print(reduce(lambda x,y: x if x<y else y, lst))