class Compiler:
    def __init__(self):
        self.temp_count = 0
        self.ls = []

    def generate_temp(self):
        temp_name = f"t{self.temp_count}"
        self.temp_count += 1
        return temp_name

    def compile_expression(self, expression):
        tokens = expression.split()
        result = tokens[0]

        for i in range(1, len(tokens), 2):
            flag = 0
            if len(tokens[i+1]) == 2 and tokens[i+1][0] == '-':
                flag = 1
                temp1 = self.generate_temp()
                print(f"{temp1} = {tokens[i+1]}")
                self.ls.append(f"{temp1} = {tokens[i+1]}")
            else:
                flag = 0  # Reset flag for each iteration
            op = tokens[i] 
            operand = tokens[i+1]
            temp = self.generate_temp()
            if flag == 1:
                operand = temp1
            print(f"{temp} = {result} {op} {operand}")
            self.ls.append(f"{temp} = {result} {op} {operand}")
            result = temp

        return result

    def compile_assignment(self, assignment):
        var, expr = assignment.split(' = ')
        result = self.compile_expression(expr)
        print(f"{var} = {result}")
        self.ls.append(f"{var} = {result}")

    def compile(self, code):
        statements = code.split(';')
        for statement in statements:
            if '=' in statement:
                self.compile_assignment(statement.strip())
            elif statement.strip():
                self.compile_expression(statement.strip())

    def convertToAsm(self):
        for i in self.ls:
            var, expr = i.split(' = ')
            tokens = expr.split()
            if len(tokens) == 1:
                print(f"MOV {var} {expr}")
            else:
                if tokens[1] == '+':
                    print(f"ADD {var} {tokens[0]} {tokens[2]}")
                elif tokens[1] == '*':
                    print(f"MUL {var} {tokens[0]} {tokens[2]}")

compiler = Compiler()
code = """
x = 2 * -y + z * -w ;
"""

compiler.compile(code)
print("---")
compiler.convertToAsm()
