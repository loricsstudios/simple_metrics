from itertools import product

def generate_expressions(digits, target):
    def evaluate(expr):
        try:
            
            return eval(expr)
        except:
            return None

    def generate(digits, expr=''):
        if not digits:
            if evaluate(expr) == target:
                yield expr
            return
        
        for i in range(1, len(digits)+1):
            curr = digits[:i]
            if len(curr) > 1 and curr[0] == '0':
                # continue
                break
            
            if expr:
                for op in ['+', '-', '*']: # ,''
                    yield from generate(digits[i:], expr + op + curr)
            else:
                yield from generate(digits[i:], curr)

    return list(generate(digits))

# Parse input
# digits, target = "548860139721", 80
# digits, target = "123", 6
# data = ["296469831", 89]
# data = ["8768413001", -76]
# data = ["10184956957", -58] 
data =  ["898389021", 77]
digits, target = data[0], data[1]

# Generate and filter valid expressions
valid_expressions = generate_expressions(digits, target)

# Print result
with open("output2.txt","w") as fw:
    fw.write("[")
    for entry in valid_expressions:
        fw.write(f'"{entry}",')
    fw.write("]")
print(valid_expressions)
# print(len(valid_expressions))