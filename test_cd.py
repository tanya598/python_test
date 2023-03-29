import os
import pytest

def test_filtered_lines():
    with open('input.txt', 'w') as input_file:
        input_file.write('example line\nnot an example\nexample again\n')

    with open('input.txt', 'r') as input_file:
        input_lines = input_file.readlines()

    keyword = 'example'

    filtered_lines = [line for line in input_lines if keyword in line]

    with open('filtered.txt', 'w') as output_file:
        output_file.writelines(filtered_lines)

    with open('filtered.txt', 'r') as output_file:
        output_lines = output_file.readlines()

    assert len(output_lines) == 2
    assert output_lines[0] == 'example line\n'
    assert output_lines[1] == 'example again\n'

    os.remove('input.txt')
    os.remove('filtered.txt')
