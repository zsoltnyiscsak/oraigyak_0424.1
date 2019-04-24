import random

wheel = set(range(0,37))

red = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
black = wheel-red
even = set(range(0,37,2))
odd = wheel-even
small = (set(range(0,19)))
great = wheel-small

wheel.add('00')


prop = {'red':red,'black':black,'even':even,'odd':odd,'small':small,'great':great}
bet = input('Give your bet köcsög: ')

while True:
    if bet not in prop:
        bet = input('Give your bet again paraszt: ')
    else:
        num = random.choice(list(wheel))
        if num == '00':
            print('00 is green')
        else:
            for k in prop:
                if num in prop[k]:
                    print('{} is {}'.format(num,k))
            if num in prop[bet]:
                print('You win Сука блять!')
                break
            else: print('You lose Сука блять!')
print(wheel)
print(num)
