def test_set():
    assert set([-3, -3, 3, 3, -2, 1, 2, -1, 0, 0]) == {-3, -2, -1, 0, 1, 2, 3}
    assert set('1230003212312312002000120') == {'0', '1', '2', '3'}
    assert set(['a', 'a', 'b', 'c']) == {'a', 'b', 'c'}
    assert {0, -3, 10000} == {10000, -3, 0}
    assert {-3, -3} == {-3}
    set1 = {0}
    set1.add(1)
    assert set1 == {0, 1}
    assert len(set1) == 2