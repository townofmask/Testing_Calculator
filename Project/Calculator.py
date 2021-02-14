a,znak,b = map(int,input().split())

class Calc:
    def plus(self, a, b):
            return a + b

    def minus(self, a, b):
            return a - b

    def mult(self, a, b):
            return a*b 

    def divis(self, a, b):
            if b==0:
                return 'zero division'
            else:
                return a/b
    
    def step(self, a, b):
        try:
            return a**b

def priority(znak):
    if znak == '*' or znak =='/':
        return 1
    elif znak == '+' or znak == '-':
        return 2
    elif znak == '^':
        return 0
    else:
        return -10

def return_res(znak,a,b):
    if znak == '+':
        return result.plus(a,b)
    elif znak == '-':
        return result.minus(a,b)
    elif znak == '*':
        return result.mult(a,b)
    elif znak == '/':
        return result.divis(a,b) 
    elif znak == '^':
        return result.step(a,b)

def checking(inp):
  inp = inp.replace(' ', '')
  inp = inp.replace(',', '.')
  oper = 0
  operands = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.')
  znaki = ('+', '-', '*', '/', '^','(', ')')

  for m in inp:                                       #если в строке нет чисел, то она нам не подходит
        if m in operands:
              oper += 1          
  if oper == 0:
        return False            


  for m in inp:                                       #если в строке нет ни операций, ни операндов, то она нам не подходит
    if m not in znaki and m not in operands:
        return False  

  br_c = 0                                            #проверяем совпадает ли количество открывающих и закрывающих скобок
  for m in inp: 
        if m == '(':
              br_c += 1
        elif m == ')':
              br_c -=1
        if br_c < 0:
              return False

  znaki_wo_br = ('+', '-', '*', '/', '^')
  znaki_wo_min = ('+', '/', '*')
  znaki_wo_op_br = ('+', '-', '*', '/', '^', ')')
  inp = inp.replace('(-', '(0-')                                              #делаем автозамену для удобства подсчета
  inp = inp.replace('(((', '(1*(1*(') 
  inp = inp.replace('((', '(1*(')    
  if inp[0] == '-' and (inp[1] in operands or inp[1] == '('):                 #если строка начинается с -, то добавлем в начало 0 для удобства подсчета
    if len(inp) >= 2:
      inp = inp[:0] + '0' + inp[0:]
  
  if inp[len(inp)-1] in znaki_wo_br or inp[len(inp)-1] == '(':                #если последний символ - это операция, либо открывающая скобка, то отбрасываем строку
          return False

  count = 0
  for m in inp:
        if m =='(':
              count +=1
  if count >= 2:
      for m in range(1,len(inp)-1): 
              if inp[m] == '(' and inp[m-1] not in znaki_wo_br:
                    return False  
  
  if len(inp)>=3:
        for m in range(len(inp)-1):   
          if inp[m] == '(' and inp[m+1] in znaki_wo_min:
            return False
          elif inp[m] in znaki_wo_br and (inp[m+1] in znaki_wo_br or inp[m+1] == ')'):               
            return False
          elif inp[m] in operands and inp[m+1] == '(':
            return False
          elif inp[m] == ')' and inp[m+1] not in znaki_wo_op_br : 
            return False      
        return inp 
  else:
      return inp
      
result = Calc()
print(result)