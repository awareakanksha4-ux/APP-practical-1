import re

text = """
contact us at support@example.com or admin@test.org.
you can also email student123@university.edu.
"""

pattern = r'[a-zA-z0-9._%+-]+@[a-zA-z0-9.-]+\.[a-zA-z]{2,}'

emails = re.findall(pattern, text)

print("email address found:")

for email in emails:
    print(email)
    