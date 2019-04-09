import re

with open('Json.txt') as file:
   text = file.read()

numbers = re.findall(r'(-*\d+)', text)

def summary(input):
   return sum([int(n) for n in input])

print(summary(numbers))