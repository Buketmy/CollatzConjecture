def collatz(number):
    while number != 1:
        print(number)
        if number % 2 == 0:
            number:int = int(number // 2)
        else:
            number:int = int(3 * number + 1)
    else:
        print(number)
        print("Finished")
        
def num():
    number:int = int(input("Number:"))
    collatz(number)
num()