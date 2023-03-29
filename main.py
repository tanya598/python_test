
with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

keyword = 'example'

filtered_lines = [line for line in input_lines if keyword in line]

with open('filtered.txt', 'w') as output_file:
    output_file.writelines(filtered_lines)