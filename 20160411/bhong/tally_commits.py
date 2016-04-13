# tally_commits.py

# This script will take a mbox formatted file as input and count the number of emails
# a particular email address sent in. Assumptions are that these emails are sent on
# each commit, we tally the number of "commits" made by email address and print to screen

def file_to_lines(filename):
   'reads the given filename and returns the content as lines'
   with open(filename) as f:
      content = f.read()
      lines = content.splitlines()
      return lines

def build_email_dictionary(lines):
   'reads the given lines and builds a dictionary (email_dict) with email address as key and number of commits as value'
   for line in lines:
      # we assume that a line that starts with From (without a colon) is the start of an email
      if line.startswith('From '):
         email_address = line.split()[1]
         if email_address in email_dict:
            email_dict[email_address] += 1
         else:
            email_dict[email_address] = 1         

def dict_to_list_of_tuples(email_dict):
   'reads the given dictionary and pretty prints the keys and values sorted by the second value of each tuple'
   # convert the dictionary into a list of tuples and store it in order of highest number of emails first
   email_sorted_list = sorted(email_dict.items(), key=lambda tup: tup[1], reverse=True)
   # iterate through the list and unpack the tuples into variables, apply a formatting template, and print to screen
   for item in range(len(email_sorted_list)):
      email_address, commits = email_sorted_list[item]
      print row_template % (email_address, commits)

if __name__ == '__main__':
   # create empty dictionary and list for later use
   email_dict = {}
   email_sorted_list = []
   # printf style template to format the output
   row_template = '%40s %10s'
   # headers for each column
   header = 'email address', 'commits'
   # hard coded filename for now
   filename = '../mbox-short.txt'
   # calls to the functions to process the data and print results
   lines = file_to_lines(filename)
   build_email_dictionary(lines)
   print row_template % header
   print row_template % tuple(['-' * len(h) for h in header])
   dict_to_list_of_tuples(email_dict)
