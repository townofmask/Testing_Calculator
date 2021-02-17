operands = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.')
znaki = ('+', '-', '*', '/','(', ')')

class Calculator:
    def calculate(self, s):
        buffer = ''
        sign = 1
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
            
            def calc(znak,a,b):
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
            result = calc(znak,a,b) 
            stack_num.append(result)
        result = stack_num.pop()
        return result

print("Launching...")
calc = Calculator()
user_input = ""
ch = ""
while user_input not in ["exit"]:
    user_input = input("> ")
    if user_input == 'exit':
        break
    else:
        for m in user_input:
            if m not in znaki and m not in operands:
                print('Please write an expression!')
                break
            elif m in operands:
                for m in user_input:
                    if m in znaki:
                        ch=1
                        break
                    else:
                        ch=0
                        continue
            if ch == 1:
                print(user_input + ' - ...Launching')
                output = calc.calculate(user_input)
                print(output)
                break
            elif ch == 0:    
                print(user_input + ' - Please write an expression!')
                break
print("Closing...")
