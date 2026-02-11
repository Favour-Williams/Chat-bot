from functions.get_files_info import get_files_info

# Wrap in print() to see the output!
print("--- Test 1: Root ---")
print(get_files_info("calculator", "."))

print("\n--- Test 2: Sub-directory ---")
print(get_files_info("calculator", "pkg"))

print("\n--- Test 3: Absolute Path Security Check ---")
print(get_files_info("calculator", "/bin"))

print("\n--- Test 4: Parent Directory Security Check ---")
print(get_files_info("calculator", "../"))
