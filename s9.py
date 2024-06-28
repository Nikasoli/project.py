import os
num=int(input('type num1 '))
num2=int(input('type num2 '))
javab=num+num2
print(javab)
def clear():
    input()
    os.system('cls')
    
while True:
    a=input('do you want add num? yes-no ')
    if a=='yes':
        num3=int(input('type num '))
        javab+=num3
        print(javab)
        clear()
        
    else:
        break




    