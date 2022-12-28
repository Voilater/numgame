import random

def randomgen():
    ran = random.randint(0,10)
    return ran

def main():
    num1 = randomgen()
    num2 = randomgen()
    result = int(num1) * int(num2)
    ans = input(f"guess {num1} divide {num2} >> ")
    if (int(ans) == result):
       print("your correct")
    else:
       print("no wrong")

print(main())
