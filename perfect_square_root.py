def isPerfectSquare(num):
    guess = 1
    while guess * guess <= num:
        if guess * guess == num:
            return True
        guess += 1
    return False
num=int(input())
print(isPerfectSquare(num))   

