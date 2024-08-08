first_value:float =float(input("please enter first value\n"))
second_value:float =float(input("please enter second value\n"))
operations: str = input("enter the operation (+, -, x, /):")
match operations:
    case "+":
        print(f"sum of {first_value} and {second_value} is {first_value + second_value}" )
    case "-":
        print(f"difference of {first_value} and {second_value} is {first_value-second_value}" )
    case "x":
        print(f"product of {first_value} and {second_value} is {first_value * second_value}")
    case"/":
        print(f"divison of {first_value} and {second_value} is {first_value / second_value}")    