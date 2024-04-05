import pytest

from main import find_lines_with_keyword


@pytest.mark.parametrize('input_data, keyword, expected', [
    ([], 'test', []),
    ([''], 'test', []),
    (['world', 'hello world'], 'hello', ['hello world']),
    (['hello', 'world', 'hello world', 'helloworld'], 'testing', []),
    (['hello', 'world', 'hello world', 'helloworld', 'hell'], 'testing', []),
    (['hello', 'world', 'hello world', 'helloworld'], '', ['hello', 'world', 'hello world', 'helloworld']),
    (['cute', 'world'], '', ['cute', 'world']),
])
def test_get_filtered_lines_returns(input_data: list[str], keyword: str, expected: list[str]):
    result = find_lines_with_keyword(input_data, keyword)
    assert result == expected
