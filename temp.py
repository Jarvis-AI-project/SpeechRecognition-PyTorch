import json

d= {'a':1, 'b':2, 'c':3}
x=json.dumps(d)
with open('temp.json', 'a') as f:
    f.write(x)
    f.write('\n')