# f=open('poems.txt')
# data=f.read()
# if 'twinkle' in data:
#     print('twinkle is present')
# else:
#     print('twinkle is not present')
# f.close()


def game():
    return 7888
score=game()
with open('hiscore.txt')as f:
    hiscorestr=f.read()
if hiscorestr=="":
     with open('hiscore.txt','w')as f:
       f.write(str(score))
elif int(hiscorestr)<score :
     with open('hiscore.txt','w')as f:
       f.write(str(score))