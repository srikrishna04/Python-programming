import mod1
print(mod1.kg_to_lbs(70))
print(mod1.lbs_to_kg(120))

from mod1 import kg_to_lbs
print(kg_to_lbs(70))

from mod1 import *
print(kg_to_lbs(70))
print(lbs_to_kg(120))

# __name__ == '__main__' if initial module being run
import mod1
print(__name__)
print(mod1.__name__)
def hello():
    print('hello')
def main():
    print('main')
if __name__ == '__main__':
    main()
    print('running this module directly')
else:
   print('running other module indirectly')