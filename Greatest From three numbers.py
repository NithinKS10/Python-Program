a = 5
b = int(input("Enter the number : "))
c = int(input("Enter the number : "))
if a>b:
    if a>c:
        print("a is greater")
    else:
        print("c is greater")
elif b>c:
    print("b is greater")
elif c>b:
    print("c is greater")
else:
    print("a,b,c are equal")