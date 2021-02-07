import re

class Calculator:
    def calculate(self, s):
        result = 0
        current = 0
        sign = 1
        stack = []
        mul = 0
        for ss in s:
            if ss.isdigit():
                current = int(ss) + 10*current
            elif ss in ["*", "/"]:
                if 
                result = sign * current
                current = 0
                mul = 1
                if ss == "*":
                    sign = 1
                else:
                    sign = -1
        

            elif ss in ["-", "+"]:
                result += sign * current
                current = 0
                mul = 0
                if ss == "+":
                    sign = 1
                else:
                    sign = -1
            elif ss == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif ss == ")":
                result += current * sign
                result *= stack.pop()
                result += stack.pop()
                current = 0
        
        if mul == 1:
            return result * current * sign

        else:       
            return result + current * sign


print("Launching...")
calc = Calculator()
user_input = ""
while user_input not in ["exit"]:
    regex = re.search('[a-zA-Z]', user_input)
    if regex != None:
        print("Please write an expression.")
    user_input = input("> ")
    output = calc.calculate(user_input)
    print(output)
print("Closing...")