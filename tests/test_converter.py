import pytest
from pathlib import Path
from conftest import validate_html

from conversor_de_arquivos.md2html import convert_md2html


@pytest.mark.parametrize(
    "input_file, expected_file", [
        ("simple.md", "simple.html")
    ]
)
def test_conversion(tmp_path, input_file, expected_file):
    input_path = str(Path("tests/test_files/input") / input_file)
    output_path = str(tmp_path / f"output.{input_file.split('.')[1]}")
    expected_path = str(Path("tests/test_files/expected") / expected_file)

    convert_md2html(input_path, output_path)

    assert validate_html(output_path, expected_path)
