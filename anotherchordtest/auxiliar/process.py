import csv
from collections import defaultdict


importedFile = open('data_cat.csv')
exportedFile = 'data2chord.csv'

importedData = []
exportedData = defaultdict(list)

csv_imported = csv.reader(importedFile)
for row in csv_imported:
	importedData.append(row)

print(len(importedData))
print(importedData[0])

processing = defaultdict(lambda: defaultdict(list))

categories = ['Autos & Vehicles', 'Comedy', 'Entertainment', 'Film & Animation', 'Gadgets & Games', 'Howto & DIY', 'Music', 'News & Politics', 'People & Blogs', 'Pets & Animals', 'Sports', 'Travel & Places']

for cat in categories:
	for related in categories:
		processing[cat][related].append(0)

for cat in categories:
	for rowie in importedData:
		if rowie[0]==cat:
			for related in categories:
				processing[cat][related][0]+=rowie.count(related)
print(processing['Comedy']['Comedy'])
print(len(processing['Comedy']))
print(len(processing['Comedy'][0]))

for cat in categories:
	for related in categories:
		print (cat + '->' + related + str(processing[cat][related][0]))

exportedData['category'].append('category')
exportedData['related'].append('related')
exportedData['count'].append('count')

for cat in categories:
	for related in categories:
		exportedData['category'].append(cat)
		exportedData['related'].append(related)
		exportedData['count'].append(processing[cat][related][0])

print(exportedData['category'][0] + '->' + exportedData['related'][0] + ':' + exportedData['count'][0])
print(exportedData['category'][1] + '->' + exportedData['related'][1] + ':' + str(exportedData['count'][1]))

itera=0

with open(exportedFile, 'w', newline='') as f:
	writer = csv.writer(f, delimiter=',') 
	while (itera < len(exportedData['category'])):
		writer.writerow([exportedData['category'][itera], exportedData['related'][itera], exportedData['count'][itera]])
		itera+=1

importedFile.close()