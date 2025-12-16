from calculation import Calculator

while True:
    choice = input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n0. Exit\nEnter Your Choice: ")
    
    match choice:
        case "1":
            num = list(map(int, input("Enter numbers separated by spaces: ").split()))
            cal = Calculator(*num)
            print(cal.addition())
        case "2":
            num = list(map(int, input("Enter numbers separated by spaces: ").split()))
            cal = Calculator(*num)
            print(cal.subtraction())
        case "3":
            num = list(map(int, input("Enter numbers separated by spaces: ").split()))
            cal = Calculator(*num)
            print(cal.multiplication())
        case "4":
            num = list(map(int, input("Enter numbers separated by spaces: ").split()))
            cal = Calculator(*num)
            print(cal.division())
        case "0":
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.\n")