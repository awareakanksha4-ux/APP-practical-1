with open("input.txt", "r")as file:

    lines =file.readlines()



line_count = len(lines)

first_two_lines = lines[:2]
print("total number of lines:", line_count)

print("\nfirst two lines:")
for line in first_two_lines:
    print(line.strip())

with open("output.txt", "w") as file:

    file.writelines(first_two_lines)
    print("\nfirst two lines have been written to output.txt")