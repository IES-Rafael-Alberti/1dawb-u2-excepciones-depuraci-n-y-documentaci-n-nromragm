import pytest
from src.actividad_01 import años_cumplidos

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (4, "1\n2\n3\n4\n"),
        (1, "1\n"),
        (-7, "")
    ]
)
def test_años_cumplidos_params(input_n, expected):
    assert años_cumplidos(input_n) == expected
