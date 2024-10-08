def calc():
    while True:
        num1 = int(input("enter num1: "))
        num2 = int(input("enter num2: "))
        operator = input("choose +, -, *, / or 0 to exit: ")
        match operator:
            case "+":
                print(num1 + num2)
            case "-":
                print(num1 - num2)
            case "*":
                print(num1 * num2)
            case "/":
                if num2 != 0:(
                    print(float(num1 / num2)))
                else: 
                    print("division by 0 unavalible")
            case "0":
                break
            case _: 
                print("error")
calc()