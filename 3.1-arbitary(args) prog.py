def sub(*args):
    result = 0
    for num in args:
        result -= num
    return result
 
print(sub(5,3,7))   
        