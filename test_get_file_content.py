print("Testing get_file_content function...")

from functions.get_file_content import get_file_content

# Test 1: Valid file path
print("\nTest 1: Valid file path")
print(get_file_content("calculator", "main.py"))

# Test 2: File outside working directory
print("\nTest 2: File outside working directory")
print(get_file_content("calculator", "pkg/calculator.py"))

# Test 3: Non-existent file
print("\nTest 3: Non-existent file")
print(get_file_content("calculator", "/bin/cat"))

# Test 4: Directory instead of file
print("\nTest 4: Directory instead of file")
print(get_file_content("calculator", "pkg/does_not_exist.py"))