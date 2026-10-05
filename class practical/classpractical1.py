import re

text = "My phone number is 9876543210 and my email is mahesh@gmail.com"

# Search for a 10-digit phone number
phone = re.search(r'\b\d{10}\b', text)

# Search for an email address
email = re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)

# Match a word at the beginning of the string
match = re.match(r'My', text)

if phone:
    print("Phone Number:", phone.group())

if email:
    print("Email:", email.group())

if match:
    print("Match found:", match.group())
