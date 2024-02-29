people = {'christopher','susan'}
for name in people:
    print(name)

for item in 'python':
    print(item)

for figure in ['triangle','circle','square']:
    print(figure)

for num in range(10):
    if num == 4:
        pass
    print(num)

for design in range(5,10,2):
    print(design)

import time
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print('wish u happy new year')

prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f'Total: {total}')

for x in range(4):
    for  y in range(3):
        print(f"({x},{y})", end='')
    print()    

numbers =[4,2,5,1,8]
for stars in numbers:
    print('*'* stars)

numbers = [4,2,5,1,8]
for count in numbers:
    output = ''
    for stars in range(count):
        output += '*'
    print(output)    

name = ''
while len(name) == 0:
    name = input('enter your name:')
print(name)

people = {'christopher','susan'}
index = 0
while index < len(people):
    print(people[index])
    index = index + 1

phone__number = "123-456-789"
for i in phone__number:
    if i =='-':
        continue
    print(i,end='')

secret_number = 9
guess_count = 0
while guess_count < 3:
    guess = int(input('guess: '))
    guess_count + = 1
    if guess == secret_number:
        print('you won!')
else:
    print('sorry,you failed!')