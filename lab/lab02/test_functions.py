import functions

def test_energy():
    # test table
    t = [
        # inputs, expected
        (1, 90000000000000000),
        (2, 180000000000000000),
        (3, 270000000000000000),
        (4, 360000000000000000),
    ]
    for mass, expected in t:
        result = functions.energy(mass)
        assert (result - expected) < 0.0001 # floating point comparison


def test_story():
    # test table
    t = [
        # inputs, expected
        ("princess", "castle", "Once upon a time, there was a princess who lived in a castle."),
        ("prince", "palace", "Once upon a time, there was a prince who lived in a palace."),
        ("queen", "kingdom", "Once upon a time, there was a queen who lived in a kingdom."),
        ("king", "country", "Once upon a time, there was a king who lived in a country."),
    ]
    for noun, place, expected in t:
        result = functions.story(noun, place)
        assert result == expected

def test_emojis():
    # test table
    tt = [
        # inputs, expected
        ("hello :)", "hello 😊"),
        ("I am sad :(", "I am sad ☹"),
        ("you are happy :D", "you are happy 😃"),
        (":P", "😛"),
    ]
    for s, expected in tt:
        result = functions.emojis(s)
        assert result == expected

def test_sum_nums():
    # test table
    t = [
        # inputs, expected
        ((1, 2), 3),
        ((2, 3), 5),
        ((3, 4), 7),
        ((4, 5), 9),
    ]
    for (a, b), expected in t:
        result = functions.sum_nums(a, b)
        assert result == expected
    
def test_add_nums():
    # test table
    t = [
        # inputs, expected
        (([1, 2], [2, 3]), [3, 5]),
        (([2, 3], [3, 4]), [5, 7]),
        (([3, 4], [4, 5]), [7, 9]),
        (([4, 5], [5, 6]), [9, 11]),
    ]
    for (a, b), expected in t:
        result = functions.add_nums(a, b)
        assert result == expected