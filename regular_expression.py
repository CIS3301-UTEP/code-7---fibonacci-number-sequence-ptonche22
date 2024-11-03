import re

file = open('social_media_users.csv')
file_as_text = open('social_media_users.csv').read()
#print(text_from_file)
emails = re.findall('[a-z]+@[a-z]{4,}\.com', file_as_text)
print (emails)
print(len(emails))