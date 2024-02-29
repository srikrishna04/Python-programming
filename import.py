import random

x = random.randint(1,6)
y = random.random()
print(x)
print(y)
mylist = ['rock','paper','scissor']
z = random.choice(mylist)
print(z)
cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)
print(cards)

while True:
    lists = ['rock','paper','scissor']
    computer = random.choice(lists)
    player = None
    while player not in lists:
        player = input('rock,paper,scissor?: ').lower()
    if player == computer:
        print('computer: ',computer)
        print('player:',player)
        print('tie!')
    elif player == 'rock':
        if computer == 'scissor':
            print('computer: ',computer)
            print('player:',player)
            print('you won!')
        if computer == 'paper':
            print('computer: ',computer)
            print('player:',player)
            print('you lose!')
    elif player == 'paper':
        if computer == 'rock':
            print('computer: ',computer)
            print('player:',player)
            print('you won!')
        if computer == 'scissor':
            print('computer: ',computer)
            print('player:',player)
            print('you lose!')
    elif player == 'scissor':
        if computer == 'paper':
            print('computer: ',computer)
            print('player:',player)
            print('you won!')
        if computer == 'rock':
            print('computer: ',computer)
            print('player:',player)
            print('you lose!')
    play_again = input('play again? (yes/no):').lower()
    if play_again != 'yes':
        break
print('bye')
           


         
             
    