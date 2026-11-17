from console import ascii_chef, welcome, instruction1, question1
from data import cuisines, restaurant_data

print(ascii_chef)
print(welcome)
print(instruction1)
print(question1)
answer = str(input().strip()).lower()

matches = [c for c in cuisines if c.startswith(answer)]

if matches:
  print(matches)
else:
  print("Sorry, we did not find matching cuisines. Please try again with a different cuisine.")
