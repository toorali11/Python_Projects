h=int(input("whats your height? "))

if h>120:
    print("Can ride")
    a=int(input("whats your age? "))
    b=0
    if a<12:
        b+=5
        print(f"Ticket cost {b}")
    elif a<18:
        b+=7
        print(f"Ticket cost {b}")
    elif a>=18:    
        b+=12
        print(f"Ticket cost {b}")
        if input("you want photos")=="yes":
            b+=3
            print(f"The bill will be {b}")
        else:
            print(f"The total bill will be {b}")
else:
    print("Cant ride")
