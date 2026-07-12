# Local vs Global variable



x = 20  # Global variable

def show():
    x = 10  # Local variable
    print(f"Inside: {x}")

show()

print(f"Outside: {x}")

# x = 20 is a global variable because it is declared outside the function.
# x = 10 is a local variable because it is declared inside the function show().
# Inside the function, Python uses the local variable (10).
# Outside the function, Python uses the global variable (20).


