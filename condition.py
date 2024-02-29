price = input('how much did you pay')
price = float(price)
if price >= 1.00 :
    tax = 0.7
else:
    tax = 0
print(tax)
print('tax rate is: ' +str(tax))

province = input('what province do you live in?')
if province == 'alberta' or province == 'nunavut':
    tax=0.05
elif province == 'ontario':
    tax = 0.13
else :
    tax=0.15
print(tax)

country = input('what country do you live in?')
if country == 'canada':
    province = input('what province do you live in?')
    if province in ('alberta','nunavut','yukon'):
        tax=0.05
    elif province == 'ontario':
        tax = 0.13
    else :
        tax = 0.15
else:
    tax = 0
print(tax)

gpa = float(input('what was your grade point average'))
if gpa >= .85:
 lowest_grade = float(input('what was you lowest grade?'))
 if lowest_grade >= .70:
     print('well done')

gpa = float(input('what was your grade point average'))
lowest_grade = float(input('what was you lowest grade?'))
if gpa >=.85 and lowest_grade >= .70:
    honour_roll = True
else: 
    honour_roll = False
if honour_roll:
    print('you made honour roll')
print('only true condition')

is_hot = False
is_cold = False
if is_hot:
    print("it's a hot day")
elif is_cold:
    print("it's cold day")
else:
    print("it's lovely day")
print('have a nice day')

weight = int(input('weight'))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    print(weight*0.45)
else:
    print(weight/0.45)