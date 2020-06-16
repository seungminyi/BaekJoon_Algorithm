def factorial(number:int):
    if number == 1:
        return number
    elif number == 0:
        return 1
    else :
        return number * factorial(number-1)
        
if __name__ ==  "__main__":
    x = int(input())
    print(factorial(x))