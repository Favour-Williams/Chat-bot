from functions.run_python_file import run_python_file

# Wrap in print() to see the output!
print("--- Test 1: Run a valid Python file ---")
print(run_python_file("calculator", "main.py"))

print("\n--- Test 2: Run a Python file with arguments ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))


print("\n--- Test 3: Attempt to run a non-Python file ---")
print(run_python_file("calculator", "tests.py") )

print("\n--- Test 4: Attempt to run a file outside the working directory ---")
print(run_python_file("calculator", "../main.py") )

print("\n--- Test 5: Attempt to run a non-existent file ---")
print(run_python_file("calculator", "nonexistent.py") )

print("\n--- Test 6: Attempt to run a directory instead of a file ---")
print(run_python_file("calculator", "lorem.txt") )

