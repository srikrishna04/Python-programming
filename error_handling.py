x=200
try:
    y = int(input('age: '))
    result = x/y
except ValueError as e:
    print(e)
    print('enter only a number')
except ZeroDivisionError as e:
    print(e)
    print('u cannot divide by zero')
except Exception as e:
    print(e)
    print('something went wrong')
else:
    print(result)
finally:
    print('this is our cleaup code')


