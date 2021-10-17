import sys
list=[]
Entering_numbers = True
print('Enter a number and press the Enter key. When done entering numbers, press the Enter key a second time.')
while Entering_numbers:
    num = input()
    if num!='':
        try:
            value=int(num)
            list.append(value)
        except:
            value=float(num)
            list.append(value)
    else:
        Entering_numbers = False

def multiply(n,*args):
    product = n
    for i in args:
        product *= i
        return(product)
print(multiply(list))
print(list)