import functions as f

def test_subtract_list_length():
    assert f.subtract(5, 3) == 2
    assert f.list_length(["a", "b", "c", "d"]) == 4