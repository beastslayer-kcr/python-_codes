import math
global guess

pasw = str(input('Input password: '))
 #only limeted myself to lowercase for simplllicity.
chars = 'abcdefghijklmnopqrstuvwxyz'
base = len(chars)+1

def cracker(pasw):
    guess = ''
    tests = 1
    c = 0
    m = 0

    while True:
        y = tests
        while True:
            c = y % base
            m = math.floor((y - c) / base)
            y = m
            guess = chars[(c - 1)] + guess
           # print(guess)
            if m == 0:
                break

        if guess == pasw:
            print('Got "{}" after {} tests'.format(guess, str(tests)))
            break
        else:
            tests += 1
            guess = ''


cracker(pasw)
input()
