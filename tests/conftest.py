import pytest
from pathlib import Path

from bs4 import BeautifulSoup


@pytest.fixture
def test_files_dir():
    return Path("tests/test_files")


def validate_html(output_path, expected_path):
    with open(output_path) as output, open(expected_path) as expected:
        output_soup = BeautifulSoup(output.read(), "html.parser")
        expected_soup = BeautifulSoup(expected.read(), "html.parser")
        return output_soup.prettify() == expected_soup.prettify()
