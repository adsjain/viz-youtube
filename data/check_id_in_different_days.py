import csv
from collections import defaultdict



file1 = '/Users/pestefo/Sync/projects/information-visualization-course/proyecto/data/data.csv'
file2 = '/Users/pestefo/Sync/projects/information-visualization-course/proyecto/data/302.csv'

columns1 = defaultdict(list)
columns2 = defaultdict(list)

with open(file1, 'rU') as f:
	reader = csv.DictReader(f) 
	for row in reader:
		for (k,v) in row.items(): 
			columns1[k].append(v)

with open(file2, 'rU') as f:
	reader = csv.DictReader(f) 
	for row in reader:
		for (k,v) in row.items(): 
			columns2[k].append(v)

# related = set(columns1['related_1'])
# related.update(columns1['related_2'])
# related.update(columns1['related_3'])
# related.update(columns1['related_4'])
# related.update(columns1['related_5'])
# related.update(columns1['related_6'])
# related.update(columns1['related_7'])
# related.update(columns1['related_8'])
# related.update(columns1['related_9'])
# related.update(columns1['related_10'])
# related.update(columns1['related_11'])
# related.update(columns1['related_12'])
# related.update(columns1['related_13'])
# related.update(columns1['related_14'])
# related.update(columns1['related_15'])
# related.update(columns1['related_16'])
# related.update(columns1['related_17'])
# related.update(columns1['related_18'])
# related.update(columns1['related_19'])
# related.update(columns1['related_20'])

related = set(columns1['id'])

interseccion = related.intersection(set(columns2['id']))
union = related.union(set(columns2['id']))
print len(interseccion)
print len(union)