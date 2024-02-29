firstname='srikrishna'
print(firstname)
last_name='bairi'
print(firstname+last_name)
print('hello '+firstname+' '+last_name)
message = firstname + ' [' + last_name + '] is a coder'
msg = f'{firstname} [{last_name}] is a coder'
print(message)
print(msg)

sentance='The dog is named sammy'
print(len(sentance))
print(sentance.find('o'))
print(sentance.upper())
print(sentance.lower())
print(sentance.capitalize())
print(sentance.count('a'))
print(sentance.replace('dog','cat'))
print('cat' in sentance)
print(sentance.title())
print(sentance.isdigit())
print(sentance.isalpha())
print(sentance * 3)
first_name=input('what is your first name? ')
last_name=input('what is your last_name?')
print('Hello ' +first_name.capitalize()+' '+last_name.capitalize())

n1=2
n2=4
sum = n1 +n2
print("the sum of {1} and {0} is {2}".format(n1,n2,sum))  #positional argument
print('the numbers are {p} and {q}'.format(p=9,q=1)) #keyword argument
text = 'the sum of {} and {} is {}'
print(text.format(n1,n2,sum))
name = 'krish'
print('hello,my name is {}'.format(name))
print('hello,my name is {:10}.Nice to meet you'.format(name))
print('hello,my name is {:<10}.Nice to meet you'.format(name))
print('hello,my name is {:>10}.Nice to meet you'.format(name))
print('hello,my name is {:^10}.Nice to meet you'.format(name))
number = 1000
print('the number is {:.2f}'.format(number))
print('the number is {:,}'.format(number))
print('the number is {:b}'.format(number))
print('the number is {:o}'.format(number))
print('the number is {:E}'.format(number))

name = 'start stopstep'
first_name = name[:5]
last_name = name[6:]
funky_name = name[::2]
reverse = name[::-1]
print(first_name)
print(last_name)
print(funky_name)
print(reverse)
website = 'http://google.com'
slice = slice(7,-4)
print(website[slice])