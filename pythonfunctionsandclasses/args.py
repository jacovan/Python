def multiply(n,*args):
    product = n
    for i in args:
        product *= i
    print(product)
    return;
multiply(23,3)
multiply(7,6)
multiply(1,2,3,4,5,6,7,8,9,10)