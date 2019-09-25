# Write a program that prompts for a file name, then opens that file
# and reads through the file, and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.pythonlearn.com/code/words.txt
#


"""
# I changed the solution to include getting the remote file via a URL

import urllib2

url = input("Enter URL: ")
page = urllib2.urlopen(url)

content = page.read()
print(content.upper().rstrip())
"""

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
red = fh.read()
final = red.rstrip()
print(final.upper())

