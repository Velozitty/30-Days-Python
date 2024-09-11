"""Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries"""

dog = {}

dog['name'] = 'Doug'
dog ['color'] = 'brown'
dog ['breed'] = 'German Sheperd'
dog ['legs'] = 4
dog ['age'] = 10

student = {
    'first_name': "Kelvin",
    'last_name': "Veloz",
    'gender' : 'Male',
    'age': 23,
    'martital_status' : "Single",
    'skills': ["CS", 'Gaming', 'Driving', 'Sports'],
    'country' : "USA",
    'city' : 'Port Chester',
    'address':{
        'street':'Parkway Drive',
        'zipcode':'10573'
        }
}
print(len(student)) #9
print(student.get('skills')) #['CS', 'Gaming', 'Driving', 'Sports']
print(type(student.get('skills'))) #<class 'list'>
student ['skills'].append('coding')
print(student.get('skills')) #['CS', 'Gaming', 'Driving', 'Sports', 'coding']
keys = student.keys()
print(keys) #dict_keys(['first_name', 'last_name', 'gender', 'age', 'martital_status', 'skills', 'country', 'city', 'address'])
values = student.values()
print(values)#dict_values(['Kelvin', 'Veloz', 'Male', 23, 'Single', ['CS', 'Gaming', 'Driving', 'Sports', 'coding'], 'USA', 'Port Chester', {'street': 'Parkway Drive', 'zipcode': '10573'}])
print(student.items())#dict_items([('first_name', 'Kelvin'), ('last_name', 'Veloz'), ('gender', 'Male'), ('age', 23), ('martital_status', 'Single'), ('skills', ['CS', 'Gaming', 'Driving', 'Sports', 'coding']), ('country', 'USA'), ('city', 'Port Chester'), ('address', {'street': 'Parkway Drive', 'zipcode': '10573'})])
student.popitem()
print(student) #deletes address dictionary
del dog
print(dog) #NameError: name 'dog' is not defined