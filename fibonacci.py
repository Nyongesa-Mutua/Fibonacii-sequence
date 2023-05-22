print("The fibonacci sequence begins with 0 and 1. The next number is the sum of the previous two numbers.")
print("It has many applications in stock prices prediction and music compostion.")
print("This program determines the nth number of the sequence for giures less than 10,000.")
invitation = input("Do you want to use the above program. Type yes(y) to use and no(n) to quit.").lower()
if invitation.startswith("y"):
    fibonacci = [0,1]
    next_number = 0
    n = int(input("Enter the number of times you want the number position of the sequence you want to find. "))
    n = n-2
    while n>0:
        n-=1
        next_number = fibonacci[-1]+fibonacci[-2]
        fibonacci.append(next_number)

    print(next_number)
    print(fibonacci)
else:
    quit
    

