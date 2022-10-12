
def sum(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y    
def div(x,y):
    try:
        return x/y
    except ZeroDivisionError as e:
        print("Invalid compute ZeroDivisionError")

counter = 0
action = None
while action != "exit":
    try:
        x = float(input("Enter first number:"))
        y = float(input("Enter Second number:"))
    except Exception as e:
        print(f'Invaild input {e}')
        continue

    print("Choice the Operation:")
    print("1. addition(+)")
    print("2. substration(-)")
    print("3. multiplication(*)")
    print("4. division(%)")
    try:
        choice = int(input("Enter the choice : ")) 
    except Exception as e:
        print(f'Invaild choice {e}')
        continue
    if choice == 1:
            result = sum(x,y)
            print(f'Addition of {x} and {y} is : {result}')
            counter +=1
    elif choice == 2:
            result = sub(x,y)
            print(f'substraction of {x} and {y} is : {result}')
            counter +=1
    elif choice == 3:
            result = mul(x,y)
            print(f'multiplication of {x} and {y} is : {result}')
            counter +=1
    elif choice == 4:
            result = div(x,y)
            print(f'division of {x} and {y} is : {result}')
            counter +=1
    else:
        print("Invalid choice")
        continue
    action = input("Do you want to continue (yes/exit) : ").lower()
    if action == "exit":
        print(f'Total Number of calculations: {counter}')
        exit()
    