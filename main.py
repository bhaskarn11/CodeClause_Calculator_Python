import math

class Calculator:

    def calculate(self, cal_sign, a, b):
        if cal_sign == "+":
            return a + b
        if cal_sign == "-":
            return a - b
        if cal_sign == "/":
            return a / b
        if cal_sign == "*":
            return a * b


def calc():
    try:
        inp = input("Enter inputs seperated by comma, e.g: 2,6 -> ").split(",")
        cal_sign = input("Enter operation (+, -, / , *) -> ")
        signs = ["+", "-", "/", "*"]
        if (len(inp) != 2 or (len(cal_sign) != 1 and cal_sign in signs)):
            print("Enter valid inputs!")
            return
        
        a, b = None, None
        try:
            a = float(inp[0])
            b = float(inp[1])
            
        except TypeError as e:
            print("Invalid input")
            return
        
        cal = Calculator()
        res = cal.calculate(cal_sign, a, b)
        print(res)
        op = input("Want to calculate another? Y or N -> ")
        if op.upper() in ["Y", "YES"]:
            calc()
        else:
            print("Adios!")
            exit(0)
    except KeyboardInterrupt as ke:
        return


if __name__ == "__main__":
    calc()
