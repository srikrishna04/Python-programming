names = ['sri','kri','sh','n','ram']
names[3] = 'na'
print(names)
print(names[0])
print(names[-1])
print(names[2:4])
print(names[2:])
print(names[:4])
print(names[:])

matrix = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])
matrix[0][1] = 11
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)

numbers = [5,2,1,2,7]
numbers.append(3)
print(numbers)
numbers.insert(1,10)
print(numbers)
numbers.remove(10)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(1))
print(50 in numbers)
print(numbers.count(2))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers.append(15)
print(numbers2)
numbers.clear()
print(numbers)
extend to add two list

numbers = [1,3,5,1,5,3,3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

coordinates = [1,2,3]
x,y,z = coordinates
print(x)

# tuples : immutable , ordered
tuples= (1,2,3)
p,q,r = tuples
print(p)
print(tuples.count(2))
print(tuples.index(1))

# set : unordered,unindexed,and no duplicate values
utensils = {'fork','spoon','knife'}
dishes = {'bowl','plate','cup','knife'}
utensils.add('napkin')
utensils.remove('fork')
utensils.update(dishes)
# utensils.clear()
for x in utensils:
    print(x)
print(utensils.union(dishes))
print(utensils.difference(dishes))
print(utensils.intersection(dishes))

# dictionary : changeable,unordered,uses hashing
customer = {
    'name': 'john smith',
    'age': 20,
    'is_verified': True
}
customer.update({'city':'karimnagar'})
customer.update({'name':'srikrishna'})
customer.pop(age)
print(customer['name'])
print(customer.get('name'))
print(customer.keys())
print(customer.values())
print(customer.items())
for key,value in customer.items():
    print(key,value)
customer.clear()

christopher = {}
christopher['first'] = 'christopher'
christopher['last'] = 'harison'
susan= {}
susan['first'] = 'susan'
susan['last'] = 'harison'
people = []
people.append(christopher)
people.append(susan)
people.append({
    'first':'bill' , 'last':'gates'
})
print(people)

phone = input('phone: ')
mapping = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four'
}
output = ''
for ch in phone:
    output += mapping.get(ch,'!') + ''
print(output)

message = input('>')
words = message.split(' ')
emojis = {
    ':)' : '😃',
    ':(' : '😔'
}
output = ''
for word in words:
    output += emojis.get(word,word)
print(output)
