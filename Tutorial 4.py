# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15pYW7JYRPKVIMgnz2L4sZORAr8eniJd2
"""

cards = [13,11,10,9,8,7,5,4,3]

query = 8

output = 5

cards2 = [4,3,2,1]
query = 4
output = 1


cards3 = []
query = 3
output = -1

card4 = [-8 , -7, -5]
query = -6
output = -1

cards5 = [2]
query = 3
output = -1

def find_card(cards, query):
  pass
  # Implement a searching algorithm using the systematic approach discussed in class

result = find_card(cards, query)
print(result)

result == output

testing_cases = {}

testing_cases = {
    'input': {
        'cards': [13,12,11,10,9,8,5,3],
        'query': 8
    },
    'output': 5
}

find_card(testing_cases['input']['cards'], testing_cases['input']['query']) == testing_cases['output']

find_card(**testing_cases['input']) == testing_cases['output']

