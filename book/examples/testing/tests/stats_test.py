import pytest
from pytest import approx

import ds.stats as stats

@pytest.mark.parametrize("input_list, expected", [
    ([4, 4, 4], 4.0),
    ([1, 2, 3], 2.0),
    ([1, 2, 3, 4], 2.5),
    ([-1, 0, 1], 0.0),
])
def test_mean(input_list, expected):
    assert stats.mean(input_list) == approx(expected)

@pytest.mark.parametrize("input_list, expected", [
    ([4, 4, 4], 0.0),
    ([1, 2, 3], 0.8164965809),
    ([1, 2, 3, 4], 1.1180339887),
    ([-1, 0, 1], 0.816497),
])
def test_std(input_list, expected):
    assert stats.std(input_list) == approx(expected)