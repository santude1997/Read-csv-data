import csv
with open('file.csv','r') as f:
	r=csv.reader(f)
	data=list(r)
	for row in data:
		for col in row:
			print(col,'\t',end="")
		print()
print('reading successfull visit again thank you')