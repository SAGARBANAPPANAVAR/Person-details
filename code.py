


import csv
b=input('enter phone number or name of the person: ')
c=b.lower()
with open('project.csv','r') as csvfile:
	reader= csv.DictReader(csvfile)

	for i in reader:
		if (b in i.values() or c in i.values()):
			print(i)
			#break	
	else:
		if b not in i:
			print('details not found')
	
				
