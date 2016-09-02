def while_for(number, steep):
    i = 0
    numbers = []
    while i < number:
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + steep
        print("Numbers now:", number)
        print("At the bottom i is %d" % i)
    print("The numbers:")
    for num in numbers:
        print(num)
def for_while(number):
    i = 0
    numbers = []
    for i in range(number):
        print("At the top i is %d" % i)
        numbers.append(i)
        print("Number now:", number)
        print("At the bottom i is %d" % i)
    print("The numbers")
    for num in numbers:
        print(num)
        
i = int(input("this is while loop:"))
while_for(i,2)
print()
i = int(input("this is for loop:"))
for_while(i)
