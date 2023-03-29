import pytest

@pytest.fixture
def input_lines():
    return [
        'this is an example line\n',
        'this is another line\n',
        'yet another line with the example keyword\n',
        'this line has nothing of interest\n'
    ]

@pytest.fixture
def expected_output():
    return [
        'this is an example line\n',
        'yet another line with the example keyword\n'
    ]

@pytest.fixture
def input_file(tmp_path, input_lines):
    file_path = tmp_path / 'input.txt'
    with open(file_path, 'w') as f:
        f.writelines(input_lines)
    return file_path

@pytest.fixture
def output_file(tmp_path):
    return tmp_path / 'filtered.txt'

def test_filter_lines(input_file, output_file):
    keyword = 'example'
    with open(input_file, 'r') as input_file:
        input_lines = input_file.readlines()

    filtered_lines = [line for line in input_lines if keyword in line]

    with open(output_file, 'w') as output_file:
        output_file.writelines(filtered_lines)

    with open(output_file, 'r') as output_file:
        output_lines = output_file.readlines()

    assert output_lines == expected_output


import os
import pytest

def test_filtered_file_created():
    keyword = 'example'
    with open('input.txt', 'w') as input_file:
        input_file.write('this is an example\nthis is not\n')
    with open('input.txt', 'r') as input_file:
        input_lines = input_file.readlines()

    filtered_lines = [line for line in input_lines if keyword in line]

    with open('filtered.txt', 'w') as output_file:
        output_file.writelines(filtered_lines)

    assert os.path.isfile('filtered.txt') == True

def test_filtered_file_content():
    keyword = 'example'
    with open('input.txt', 'w') as input_file:
        input_file.write('this is an example\nthis is not\n')
    with open('input.txt', 'r') as input_file:
        input_lines = input_file.readlines()

    filtered_lines = [line for line in input_lines if keyword in line]

    with open('filtered.txt', 'w') as output_file:
        output_file.writelines(filtered_lines)

    with open('filtered.txt', 'r') as output_file:
        output_lines = output_file.readlines()

    assert len(output_lines) == 1
    assert output_lines[0] == 'this is an example\n'

def test_filtered_file_no_lines_contain_keyword():
    keyword = 'example'
    with open('input.txt', 'w') as input_file:
        input_file.write('this is not\n')
    with open('input.txt', 'r') as input_file:
        input_lines = input_file.readlines()

    filtered_lines = [line for line in input_lines if keyword in line]

    with open('filtered.txt', 'w') as output_file:
        output_file.writelines(filtered_lines)

    with open('filtered.txt', 'r') as output_file:
        output_lines = output_file.readlines()

    assert len(output_lines) == 0
