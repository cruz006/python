#   this file will be for a password generator using python

import random

#   shuffles the order
def shuffle(string):
  List = list(string)
  random.shuffle(List)
  return ''.join(List)

#   is what actually generates the password
#   had to use ASCII code 
L1 = chr(random.randint(65,90)) 
L2 = chr(random.randint(65,90))
L3 = chr(random.randint(65,90))
L4 = chr(random.randint(65,90))
L5 = chr(random.randint(65,90))
D1 = str((random.randint(0,9)))
D2 = str((random.randint(0,9)))

#   makes whole thing
password = L1 + L2 + L3 + L4 + L5 + D1 + D2
password = shuffle(password)
print(password)