import containers

def test_convert():
    # Convert two lists into a dictionary
    # test table
    tt = [
        # input, expected
        ([1, 2, 3], ['a', 'b', 'c'], {1: 'a', 2: 'b', 3: 'c'}),
        (['a', 'b', 'c'], [1, 2, 3], {'a': 1, 'b': 2, 'c': 3}),
        ([], [], {}),
        ([1, 2], ['a'], {1: 'a'}),
        ([1], ['a', 'b'], {1: 'a'}),
    ]
    for l1, l2, expected in tt:
        assert containers.convert_lists_to_dict(l1, l2) == expected


def test_merge():
    # Merge two dictionaries
    # test table
    tt = [
        # input, expected
        ({1: 'a'}, {2: 'b'}, {1: 'a', 2: 'b'}),
        ({1: 'a', 2: 'b'}, {3: 'c', 4: 'd'}, {1: 'a', 2: 'b', 3: 'c', 4: 'd'}),
        ({1: 'a', 2: 'b'}, {2: 'c', 4: 'd'}, {1: 'a', 2: 'c', 4: 'd'}),
        ({}, {2: 'b'}, {2: 'b'}),
        ({1: 'a'}, {}, {1: 'a', 2: 'b'}),
    ]
    for d1, d2, expected in tt:
        assert containers.merge_dicts(d1, d2) == expected