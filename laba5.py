class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def evaluate(expression, a, b, c, d):
    stack = Stack()
    operators = '+-/*'

    for symbol in expression:
        if symbol.isdigit() or symbol.isalpha():
            if symbol == 'a':
                stack.push(a)
            elif symbol == 'b':
                stack.push(b)
            elif symbol == 'c':
                stack.push(c)
            elif symbol == 'd':
                stack.push(d)
        elif symbol in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = eval(str(operand1) + symbol + str(operand2))
            stack.push(result)

    return stack.pop()

# введення значень a, b, c, d
a = 1
b = 2
c = 3
d = 4

# зчитування виразу з файлу
with open('expression.txt', 'r') as file:
    expression = file.readline().strip()

# обрахування результату
result = evaluate(expression, a, b, c, d)

# виведення результату
print(f"Результат: {result}")
