



import csv
fields=['name','phone number','gender','account type','last seen','address']
rows=({'name':'vishal','phone number':'9941751298','gender':'male','account type':'active','last seen':'06:30pm','address':'hubballi'},
	 {'name':'sagar','phone number':'9742601738','gender':'male','account type':'active','last seen':'01:05pm','address':'hubballi'},
	 {'name':'veeresh','phone number':'9742601544','gender':'male','account type':'inactive','last seen':'10:37am','address':'goa'},
	 {'name':'prajwal','phone number':'998671794','gender':'male','account type':'inactive','last seen':'09:35am','address':'kolapur'},
	 {'name':'prajwal','phone number':'9789456217','gender':'male','account type':'active','last seen':'09:55pm','address':'bengaluru'},
	 {'name':'sagar','phone number':'9535951913','gender':'male','account type':'active','last seen':'04:11pm','address':'hubballi'},
	 {'name':'prashant','phone number':'8880140556','gender':'male','account type':'active','last seen':'12:00pm','address':'old hubballi'})


      


with open('project.csv','w',newline='') as csvfile:
	writer=csv.DictWriter(csvfile, fieldnames=fields)
	writer.writeheader()
	for row in rows:
		writer.writerow(row)
