def polish(polish_expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    tokens = polish_expression.split()

    for token in reversed(tokens):
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(token)
        elif token in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            expression = "({} {} {})".format(operand1, token, operand2)
            stack.append(expression)

    return stack[0]

polish_ifade = input("ifade:")
infix_ifade = polish(polish_ifade)
print(eval(infix_ifade))
