from main import write_file


def test_write_file_writes_all_content(prepare_output_file):
    file_path = prepare_output_file
    lines = ['Python\n', 'is\n', 'awesome\n', 'and\n', 'powerful']
    write_file(file_path, lines)
    with open(file_path, 'r') as file:
        result = file.readlines()
    assert result == lines
