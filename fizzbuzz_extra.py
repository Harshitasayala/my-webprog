for x in range(1, 101):
    if (x % 15 == 0) or x%35==0 or x%53==0:
        print("Fizzbuzz")
    elif x % 3 == 0 or x%10==3 or (x>=30 and x<40):
        print("Fizz")
    elif x % 5 == 0 or x%10==5 or (x>=50 and x<60):
        print("Buzz")
    else:
        print(x)

