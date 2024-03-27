first = int(input("enter the no"))
second = int(input("enter the no"))
print(first)
print(second)
for i in range(5):
    third = first+second
    print(third)
    first = second
    second = third
    
