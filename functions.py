from datetime import datetime
def print_time(task_name):
    print(task_name)
    print(datetime.now())
first_name = 'krish'
print_time('printed first name')
for x in range(0,10):
    print(x)
print_time('completed for loop')

def get_initial(name):
    initial = name[0:1].upper()
    return initial
first_name = input('enter your first name:')
first_name_initial = get_initial(first_name)
middle_name = input('enter your mmiddle name')
middle_name_initial = get_initial(middle_name)
last_name = input('enter your last name')
last_name_initials = last_name[0:1]
print('your initials are:' +first_name_initial +middle_name_initial +last_name_initials)

def keyword(first,middle,last):
    print('hello'+first+' '+middle+' '+last)
keyword('sri',last='dude',middle='krishna')

print(round(abs(float(input('enter a number: ')))))

# *args = varying arguments into tuple
def add(*args_any):
    args_any = list(args_any)
    args_any[0] = 0
    sum = 0
    for i in args_any:
        sum += i
    return sum
print(add(1,2,3,4))

# **kwargs = parameter that pack args into a dictionary usefull to accept varying amount of keyword arguments
def hello(**kwargs):
    print('hello '+kwargs['first']+' '+kwargs['last'])
    print('hello',end=' ')
    for key,value in kwargs.items():
        print(value,end=' ')
hello(title='mr',first='srikrishna',middle='bairi',last='dude')

def hello():
    print('hello')
hi = hello
hi()
hello()
say = print
say('assigning the memory address')

# higher order function : 1.accept a function as an argument, 2.returns a function
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    result = func('Hello')
    print(result)
hello(loud)
hello(quiet)

def divisor(x):
    def divident(y):
        return y / x
    return divident
divide = divisor(2)
print(divide(10))
    
# lambda function = accepts any number of arguments , but only has one expression(arg:exp)
def double(x):
    return x*2
print(double(5))
double = lambda x:x * 2
print(double(5))
multiply = lambda x,y,z: x * y * z
print(multiply(1,2,4))
full_name = lambda first_name,last_name: first_name+" "+last_name
print(full_name('sri','krishna'))
age_check = lambda age:True if age >= 18 else False
print(age_check(12))


# sort() method for lists,sorted() function with literables
students = ['krish','ram','raju','prasad','bobby']
students.sort(reverse=True)
for i in students:
    print(i)
tuple = ('krish','ram','raju','prasad','bobby')
sorted_tuple = sorted(tuple,reverse=True)
for i in sorted_tuple:
    print(i)

students = [('jack','F',35),('bitu','C',67),('hany','B',23),('nani','A',43),('potter','D',36)]
grade = lambda grades:grades[1]
students.sort(key=grade,reverse=True)
for i in students:
    print(i)
students = (('jack','F',35),('bitu','C',67),('hany','B',23),('nani','A',43),('potter','D',36))
age = lambda ages:ages[2]
sorted_students = sorted(students,key=age)
for i in sorted_students:
    print(i)

# map(func,iterable) = apply function to iterable
store = [('shirts',20.00),('pants',25.00),('jackets',50.00),('socks',20.00)]
to_euros = lambda data: (data[0],data[1]*0.82)
# to_dollars = lambda data: (data[0],data[1]/0.82)
store_euros = list(map(to_euros,store))
for i in store_euros:
    print(i)

# filter(func,iterable) = elements from iterable for which function return
friends = [('jam',13),('bittu',23),('goju',19),('fazil',22)]
age = lambda data:data[1] >= 18
Drinking_buddies = list(filter(age,friends))
for i in Drinking_buddies:
    print(i)

# reduce(func,iterable) = apply function to iterable and reduce to single value
import functools
letters = ['H','E','L','L','O']
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)
factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y,:x*y,letters)
print(result)

# list comprehension = to create a new list with less syntax
squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)
squares = [i*i for i in range(1,11)]
print(squares)

students = [100,90,80,70,60,50,40,30,20,10,0]
passed_student = list(filter(lambda x:x >= 60,students))
print(passed_student)
passed_student = [i for i in students if i >= 60]
print(passed_student)
passed_student = [i if i >= 60 else 'Failed' for i in students]
print(passed_student)

# dictionary comprehension = create dictionary using expression replace for loops, lambda func 
cities_in_f = {'new york':32,'boston':75,'los angles':100,'chicago':50}
cities_in_c = {key: round((value-32)*(5/9)) for (key,value) in cities_in_f.items()}
print(cities_in_c)
weather = {'new york':'snowing','boston':'sunny','los angles':'sunny','chicago':'cloudy'}
sunny_weather = {key: value for (key,value) in weather.items() if value=='sunny'}
print(sunny_weather)
cities = {'new york':32,'boston':75,'los angles':100,'chicago':50}
desc_cities = {key:('warm' if value>=40 else 'cold') for (key,value) in cities.items()}
print(desc_cities)
def check_temp(value):
    if value >= 70:
        return 'hot'
    elif 69 >= value >=49:
        return 'warm'
    else:
        return 'cold'
cities = {'new york':32,'boston':75,'los angles':100,'chicago':50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)

# zip(*iterable) = aggregate two iterables
usernames = ['krish','ram','srinu']
passwords = ('p@ssw0rd','abc123','guest')
users = dict(zip(usernames,passwords))
print(type(users))
for key,value in users.items():
    print(key+':'+value)

usernames = ['krish','ram','srinu']
passwords = ('p@ssw0rd','abc123','guest')
login_date = ['1/1/2021','1/2/2021','1/3/2021']
users = list(zip(usernames,passwords,login_date))
print(type(users))
for i in users:
    print(i)