import os

# Step 1: Create a text file with five lines of text on your Desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
file_path = os.path.join(desktop_path, 'example_file.txt')

with open(file_path, 'w') as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")
    file.write("Line 4\n")
    file.write("Line 5\n")

# Step 2: Open the file and save its content as a variable
with open(file_path, 'r') as file:
    file_content = file.read()
    print("File Content:")
    print(file_content)

# Step 3: Open the file again and write 3 more lines to the existing content
additional_lines = ["Additional Line 1\n", "Additional Line 2\n", "Additional Line 3\n"]

with open(file_path, 'a') as file:
    file.writelines(additional_lines)

# Display the updated content
with open(file_path, 'r') as file:
    updated_content = file.read()
    print("\nUpdated File Content:")
    print(updated_content)
