from intervals import overlapping_intervals

def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), )
    assert not overlapping_intervals((2, 5), (7, 10))
    assert overlapping_intervals((0,1), (1,2))
    assert not overlapping_intervals((2,0), (0,2))
    assert overlapping_intervals((3, 6), (1,5))