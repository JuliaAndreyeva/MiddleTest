import pytest
import os


@pytest.fixture()
def prepare_input_file(tmp_path):
    file_path = os.path.join(tmp_path, 'input.txt')
    with open(file_path, 'w') as file:
        file.write('Python\nis\nawesome\nand\npowerful')
    return file_path


@pytest.fixture()
def prepare_output_file(tmp_path):
    return os.path.join(tmp_path, 'filtered.txt')
