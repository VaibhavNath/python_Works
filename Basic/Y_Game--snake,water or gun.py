import random
#snake water gun or paper scissor stone

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False

print('Comp turn:Snake(s),water(w),gun(g)?')
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

you=input('your turn:Snake(s),water(w),gun(g)?')
a=gameWin(comp,you)

print(f'comp chose {comp}')
print(f'you chose {you}')
if a==None:
    print('the game is tie')
elif a:
    print('you win')
else:
    print('you loose')