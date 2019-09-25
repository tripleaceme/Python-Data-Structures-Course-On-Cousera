# Write a program to read through the mbox-short.txt
# and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word
# of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's
# mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the
# dictionary using a maximum loop to find the most prolific committer.

file = input("Enter file:")
email_text = open(file)

from_lines = []
emails = {}

for mail in email_text:
    
    mail = mail.rstrip()
    
    if mail.find('From ') == 0:
        
        mail = mail.split(' ')
        
        email_recieved = mail[1]
        
        if email_recieved not in emails:
            
            emails[email_recieved] = 1
            
        else:
            
            emails[email_recieved] += 1

email_recieved = ''
count = 0

for user in emails:
    if emails[user] > count:
        count = emails[user]
        email_recieved = user

print("%s %s" % (email_recieved, str(count)))