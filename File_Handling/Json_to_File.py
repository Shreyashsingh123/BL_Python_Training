import json
# nested json data

d={"name":"harsh",
   "age":21,
   "marks":{
       "math":25,
       "sci":30,
       "computer":28
   }}

try: # use try catch if we want to add list of data  it checks whether there is any data in file or not
    value=json.load(open("data.json",'r'))  #load is to read the data from  json file
except:
    value=[]
value.append(d)
json.dump(value, open("data.json",'w'))  # dump is to write data in json file
print(value)
