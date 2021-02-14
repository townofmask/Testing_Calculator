import re
import operator

OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

class Calculator:
    def calculate(self, s):
        stack = []
        stack2 = []
        lst = list(s)
        # stack = input().split()
        for element in s:
            if element.isdigit():
                stack.append(element)
                lst.remove(element)
            elif element in '+-*/':
                stack2.append(element)
                lst.remove(element)
            
        cnt1, cnt2 = stack.pop(), stack.pop()
        operation = stack2.pop()
        stack.append(OPERATORS[operation](int(cnt2), int(cnt1)))
            # else:
            #     cnt1, cnt2 = stack.pop(), stack.pop()
            #     stack.append(OPERATORS[element](int(cnt2), int(cnt1)))
            #     lst.remove(element)
        return stack.pop()

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
            
        # result = 0
        # current = 0
        # sign = 1
        # stack = []
        # mul = 0
        # for ss in s:
        #     if ss.isdigit():
        #         current = int(ss)
        #     elif ss in ["*", "/"]:
        #         if ss == "*":
        #             result = sign * current
        #             current = 0
        #             mul = 1
        #         elif ss == "/":
        #             result = current // sign
        #             current = 0
        #             mul = 2
        

        #     elif ss in ["-", "+"]:
        #         result += sign * current
        #         current = 0
        #         mul = 0
        #         if ss == "+":
        #             sign = 1
        #         else:
        #             sign = -1
        #     elif ss == "(":
        #         stack.append(result)
        #         stack.append(sign)
        #         sign = 1
        #         result = 0
        #     elif ss == ")":
        #         result += current * sign
        #         result *= stack.pop()
        #         result += stack.pop()
        #         current = 0
        
        # if mul == 1:
        #     return result * current
        
        # elif mul == 2:
        #     return result // current

        # else:       
        #     return result + current * sign
