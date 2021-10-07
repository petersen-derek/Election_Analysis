from typing import SupportsAbs


Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
>>> type(3)
<class 'int'>
>>> type(2019)
<class 'int'>
>>> ballots = 1,341
>>> ballots
(1, 341)
>>> type(ballots)
<class 'tuple'>
>>> type(73.81)
<class 'float'>
>>> type("Hello World")
<class 'str'>
>>> type("")
<class 'str'>
>>> type(True)
<class 'bool'>
>>> type("True")
<class 'str'>
>>> num_candidates = 3
>>> winning_percentage = 73.81
>>> candidate = "Diane"
>>> won_election = True
>>> 5 + 2 *3
11
>>> 8//5-3
-2
>>> 8+22*2-4
48
>>> 16-3/2+7-1
20.5
>>> 3**3%5
2
>>> 5+9*3/2-4
14.5
>>> (5 + 2) *3
21
>>> counties = ["Arapahoe", "Denver", "Jefferson"]
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[0]
'Arapahoe'
>>> print(counties[2])
Jefferson
>>> print(counties[-1])
Jefferson
>>> len(counties)
3
>>> counties[1:2]
['Denver']
>>> counties[0:2]
['Arapahoe', 'Denver']
>>> counties[1:]
['Denver', 'Jefferson']
>>> counties.append("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.insert(2,"El Paso")
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
>>> counties.remove("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.pop(-1)
'El Paso'
>>> counties.pop(-2)
'Denver'
>>> counties.pop(1)
'Jefferson'
>>> counties
['Arapahoe']
>>> counties.append("Denver")
>>> counties.append("Jefferson")
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[2] = "El Paso"
>>> counties
['Arapahoe', 'Denver', 'El Paso']
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties.append("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties[2] = "El Paso"
>>> counties[3] = "Denver"
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Denver']
>>> counties[1] = "El Paso"
>>> counties
['Arapahoe', 'El Paso', 'El Paso', 'Denver']
>>> counties[2] = "Denver"
>>> counties[3] = "Jefferson"
>>> counties
['Arapahoe', 'El Paso', 'Denver', 'Jefferson']
>>> counties.remove("Arapahoe")
>>> counties
['El Paso', 'Denver', 'Jefferson']
>>> counties = "El Paso", "Jefferson", "Denver", "Arapahoe"
>>> counties
('El Paso', 'Jefferson', 'Denver', 'Arapahoe')
>>> my_Tuple = tuple()
>>> counties_tuple = ("Arapahoe", "Denver", "Jefferson")
>>> counties
('El Paso', 'Jefferson', 'Denver', 'Arapahoe')
>>> counties_tuple
('Arapahoe', 'Denver', 'Jefferson')
>>> len(counties_tuple)
3
>>> counties_tuple[1]
'Denver'
>>> my_dictionary = dict()
>>> counties_dict = {}
>>> counties_dict["Arapahoe"] = 422829
>>> counties_dict
{'Arapahoe': 422829}
>>> counties_dict["Denver"] = 463353
>>> counties_dict["Jefferson"] = 432438
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
>>> len(counties_dict)
3
>>> counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
>>> counties_dict.keys
<built-in method keys of dict object at 0x0000016DF8121548>
>>> counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
>>> counties_dict.values()
dict_values([422829, 463353, 432438])
>>> counties_dict.get("Denver")
463353
>>> voting_data = []
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> voting_data[1] =( {"county":"El Paso", "registered_voters": 461149})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> voting_data.remove({'county': 'Arapahoe', 'registered_voters': 422829})
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}]
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]
>>>counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])


# What is the score?
score = int(intput("What is your test score? "))

#Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

#Module 3.2.8 Decision Support up next