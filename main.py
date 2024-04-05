def read_file(input_file: str) -> list[str]:
    """
    Read the content of an input file.

    Args:
        input_file (str): The path to the input file.

    Returns:
        list[str]: A list that contains each line of the file as a string.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()
        return lines


if __name__ == '__main__':
    try:
        file_data = read_file('data.txt')
    except:
        print('An error occurred')


