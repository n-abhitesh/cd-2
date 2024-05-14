class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, name, symbol_type, scope):
        if name in self.symbols:
            print(f"Error: Symbol '{name}' already defined in the current scope.")
            return False
        self.symbols[name] = {'type': symbol_type, 'scope': scope}
        return True

    def lookup(self, name):
        return self.symbols.get(name, None)

    def display(self):
        print("Symbol Table:")
        print("-------------")
        for name, info in self.symbols.items():
            print(f"Name: {name}, Type: {info['type']}, Scope: {info['scope']}")

# Example usage:
symbol_table = SymbolTable()

# Insert symbols
symbol_table.insert('x', 'int', 'global')
symbol_table.insert('y', 'float', 'local')
symbol_table.insert('x', 'char', 'local')  # This should print an error

# Lookup symbol
print("Lookup('x'):", symbol_table.lookup('x'))
print("Lookup('z'):", symbol_table.lookup('z'))

# Display symbol table
symbol_table.display()
