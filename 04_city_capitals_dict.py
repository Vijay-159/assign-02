# concept Dictionaries

'''
You will get a dictionary with a state as key and its capital as value, 👇 see the below example
capitals = {"Karnataka":"Bangalore", "Telangana" : "Hyderabad"}
Now your task is to bring a list which should contain like the below one
["Karnataka -> Bangalore", "Telangana -> Hyderabad"]
Return this list
'''

import unittest

def capital_dict(d1):
  str_lst = []
  # write your code here
def capital_dict(d1):
  str_lst = []
  for i in d1.items():
      str_lst.append(i[0]+' -> '+i[1])

  return str_lst
  return str_lst


# DO NOT TOUCH THE BELOW CODE

class Dict_to_list(unittest.TestCase):
  def test_01(self):
    d1 = {"Andhra": "Amaravati", "Madhyapradesh" : "Bhopal", "Maharastra" : "Mumbai" }

    output = ["Andhra -> Amaravati", "Madhyapradesh -> Bhopal", "Maharastra -> Mumbai"]

    self.assertEqual(capital_dict(d1), output)

  def test_02(self):
    d1 = {"J&K": "Srinagar", "Rajastan" : "Jaipur", "Gujarat" : "Gandhinagar" }

    output = ["J&K -> Srinagar", "Rajastan -> Jaipur", "Gujarat -> Gandhinagar"]

    self.assertEqual(capital_dict(d1), output)

if __name__ == '__main__':
  unittest.main(verbosity=2)
