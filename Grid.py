
warning=1
green =[1,6,7,12,17,20,28,33]
red=[2,11,13,18,19,24,29,32]
blue=[3,10,14,23,25,30,31,36]
orange=[4,9,15,22,26,35]
grey=[5,8,16,21,27,34]
number=set()
win=0
i=1

while i <=5:
    num1=int(input(f'Enter a number between 1 and 36, Round{i} : '))
    num2=int(input(f'Enter a number between 1 and 36, Round {i}: '))
    if num1 >36 or num2> 36:
        print('Number greater than 36 are not allowed!')
        continue 
    
    if warning == 4:
        print('Game terminated!')
        break
    
    if num1 and num2 in number:
        print(f'Warning: {warning}: numbers already Entered ')
        warning+=1
        continue
    
    number.add(num1)
    number.add(num2)
    
    if num1 in green and num2 in green:
        print('Same Colour!')
        win+=1
        i+=1
    elif num1 in red and num2 in red:
        print('Same Colour!')
        win+=1
        i+=1
    elif num1 in blue and num2 in blue:
        print('Same Colour!')
        win+=1
        i+=1
    elif num1 in orange and num2 in orange:
        print('Same Colour!')
        win+=1
        i+=1
    elif num1 in grey and num2 in grey:
        print('Same Colour!')
        win+=1
        i+=1
    else:
        i+=1
    
    
    if win==3 :
        print('You won!')
        break
print('\n')           
            