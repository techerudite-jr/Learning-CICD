# app.py

def add_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Sum of 2 and 3 is:", add_numbers(2, 3))
    print("Division of 6 by 3 is:", divide_numbers(6, 3))