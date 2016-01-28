#!/usr/bin/python

from itertools import repeat
values = input("How many variables do you want to create : ")

var = []
for i in repeat(None, values):
	space = " : " 
	userinput = raw_input("Variable name : ")
	var.append(userinput + space)

definition = []
for i in repeat(None, values):
	definition.append(raw_input("Variable definition : "))
    

samplesize = input("What is sufficient sample size for analysis : ")

print("codebook was created with details : ")
print(var, definition, samplesize)

sample = open("sample.txt", "r")
codebookmem = []

for i in repeat(None, samplesize):
	snippet = sample.readline()
		
	print("\n")
	print(snippet)
	print("\n")
   	
	row = []
	
	for item in var:
		input = raw_input((item))
		row.append(input)
	
	codebookmem.append(row)
	rowstring = str(codebookmem)
	codebook = open('codebook.txt', 'w')
	codebook.write(rowstring)
	codebook.close()

print("\n")
print("Gongratulations, you've met the sample size target succesfully! :)")
print("\n")
