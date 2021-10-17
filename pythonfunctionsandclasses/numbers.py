def sum(n,*numbers):
    result = n
    for i in numbers:
        result += i
    return result
if __name__ == '__main__':
    print(sum(2,4,6))
    print(sum(3,6,9,12))
    print(sum(1.5,2.2,7.7))
else:
    print(__name__!='__main__')