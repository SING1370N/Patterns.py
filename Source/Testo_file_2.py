x = 25
run = True
while run:
    q = int(input("In: "))
    if q == x:
        print("Good")
        run = False
    elif q > x:
        print(f"X < {q}")
    else:
        print(f"X > {q}")
else:
    print("asd")
