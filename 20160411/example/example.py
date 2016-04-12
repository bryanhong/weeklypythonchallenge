'''Write a program to read through the mbox-short.txt 
and figure out who has the sent the greatest number of mail messages. W
The program looks for 'From ' lines and takes the second word of those lins as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''

#fhand = open('mbox-short.txt')
count = 0
emailcount = {}

filename = raw_input('Enter the file name: ')

with open(filename) as f:
	for line in f:
		line = line.rstrip()
		if line.startswith('From: '):
			words = line.split()
			email = words[1]
			if email in emailcount:
				emailcount[email] += 1
			else:
				emailcount[email] = 1
e = emailcount.values()
count = max(e)

for eaddress in emailcount:
	if emailcount[eaddress] >= count:
		print eaddress, emailcount[eaddress]
			
			




	


