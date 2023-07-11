import pytest
from utils import operations


def test_read_json():
    with pytest.raises(FileNotFoundError):
        operations.read_json()

