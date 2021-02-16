import re

class Calculator:
    def parse(self, s):
        buffer = ''
        sign = 1
        operands = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.')
        znaki = ('+', '-', '*', '/','(', ')')
        s = s.replace(' ', '')
        s = s.replace(',', '.')
        stack_num = []
        stack_znaki = []
        
        for element in s:
            if element in operands:
                if sign == -1:
                    element = int(element) * int(sign)
                    element = str(element)
                    sign = 1
                if buffer == '':
                    buffer = element
                else:
                    buffer += element
            elif element in znaki:
                if element in ["-"]:
                        sign = -1
                        element = "+"
                stack_num.append(buffer)
                buffer = ''
                stack_znaki.append(element)

        if buffer != '':
            stack_num.append(buffer)
        while stack_znaki != []:
            a, b = stack_num.pop(), stack_num.pop()
            znak = stack_znaki.pop()
            a, b = float(b), float(a)
            
            def calculate(znak,a,b):
                if znak == '+':
                    return a + b
                elif znak == '-':
                    return a - b
                elif znak == '*':
                    return a*b
                elif znak == '/':
                    if b==0:
                        return 'Деление на ноль!'
                    else:
                        return a/b 
            result = calculate(znak,a,b) 
            stack_num.append(result)
        result = stack_num.pop()
        return result

print("Launching...")
calc = Calculator()
user_input = ""
while user_input not in ["exit"]:
    regex = re.search('[a-zA-Z]', user_input)
    if regex != None:
        print("Please write an expression.")
    user_input = input("> ")
    output = calc.parse(user_input)
    print(output)
print("Closing...")
