class Instruction:
    def __init__(self, operation, arg1=None, arg2=None, result=None):
        self.operation = operation
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

# Example list of instructions
instructions = [
    Instruction('ADD', 'x', 'y', 't1'),
    Instruction('SUB', 't1', 'z', 't2'),
    Instruction('MUL', 't2', 'w', 't3'),
    Instruction('ADD', 't3', 'x', 't4'),
    Instruction('MUL', 't4', 'y', 't5'),
    Instruction('ADD', 't5', 'z', 't6'),
    Instruction('ADD', 't3', 'x', 't7'),  # Redundant common subexpression
    Instruction('MUL', 't7', 'y', 't8'),  # Redundant common subexpression
    Instruction('ADD', 't6', 'w', 't9'),
    Instruction('MUL', 't9', 'x', 't10'),
    Instruction('ADD', 't10', 'y', 't11'),
    Instruction('STORE', 't11', None, 'result')
]

# Dead Code Elimination
def dead_code_elimination(instructions):
    used_results = set()
    new_instructions = []
    for instr in instructions:
        if instr.result and instr.result not in used_results:
            used_results.add(instr.result)
            new_instructions.append(instr)
    return new_instructions

# Common Subexpression Elimination
def common_subexpression_elimination(instructions):
    expressions = {}
    new_instructions = []
    for instr in instructions:
        if instr.operation == 'ADD' or instr.operation == 'SUB' or instr.operation == 'MUL':
            expr = (instr.operation, instr.arg1, instr.arg2)
            if expr in expressions:
                instr.result = expressions[expr]
            else:
                expressions[expr] = instr.result
                new_instructions.append(instr)
        else:
            new_instructions.append(instr)
    return new_instructions

# Apply optimizations
optimized_instructions = dead_code_elimination(instructions)
optimized_instructions = common_subexpression_elimination(optimized_instructions)

# Print optimized instructions
print("Optimized Instructions:")
for instr in optimized_instructions:
    if instr.operation == 'STORE':
        print(f"{instr.operation} {instr.result}")
    else:
        print(f"{instr.operation} {instr.arg1}, {instr.arg2} -> {instr.result}")
