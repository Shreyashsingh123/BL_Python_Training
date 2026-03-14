# nested dictionary practice
students = {
    "Alice": {"math": 20, "sci": 30},
    "Bob": {"math": 2, "sci": 2},
    "Charlie": {"math": 18, "sci": 22}
}
avg=0
dict_avg={}
for name,val in students.items():
    avg=0
    for sub,marks in val.items():
        avg+=marks
    avg/=len(val)
    dict_avg[name]=avg
print(dict_avg)
s=list(map(lambda x :x>5,dict_avg.values()))
print(s)
name=[name if avg>10 else avg for name,avg in dict_avg.items()]
n2=[name for name,avg in dict_avg.items() if avg>10]
print(n2)
print(name)


