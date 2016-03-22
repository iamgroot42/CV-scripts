import json
from operator import itemgetter


with open('Graphs/points.json') as data_file:    
    data = json.load(data_file)

y = sorted(data, key=itemgetter('time'))

for x in y:
	faces = sorted(x['data'], key=itemgetter('y'))
	print faces