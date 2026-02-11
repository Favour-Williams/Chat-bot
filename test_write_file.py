from functions.write_file import write_file


# Wrap in print() to see the output!
print("--- Test 1: Write to a new file ---")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print("\n--- Test 2: Write to a file in a sub-directory ---")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print("\n--- Test 3: Absolute Path Security Check ---")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))