#!/usr/bin/python3

options='''
press 1 to view the contents of a file
press 2 cat -n => to show line numbers  
press 3 cat -e => to add $ sign at the end of the line
press 4 to view multiple files at once
'''
print(options)
opt=input("Enter your choice")
if (opt==1):
	i=input("Enter your file name") 
	f=open(i,'r')
	data=f.read()
	print(data)
	f.close()
	
if (opt==2):	
	i=input("Enter your file name") 
	f=open(i,'r')
	data=f.read()
	a=data.split('\n')
	line_no=1
	for i in a:
		print(str(line_no)+" "+i)
		line_no=line_no+1

if (opt==3):
	i=input("Enter your file name") 
	f=open(i,'r')
	data=f.read()
	a=data.split('\n')
	for i in a:
		print(i+"$")	

if (opt==4):		
	noOfFiles=int(input('Enter no. of files :'))
	filenames=[]
	print("Press enter after writing a file name")
	print('Enter name of files :')
	for i in range(noOfFiles):
		name=input() 
		filenames.append(name)

	for i in filenames:
		f=open(i,'r')
		print(f.read())
		f.close()	
