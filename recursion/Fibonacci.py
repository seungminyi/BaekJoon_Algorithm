def fibonacci(number:int):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-2) + fibonacci(number-1)

if __name__ == "__main__":
    x = int(input())
    print(fibonacci(x))
    