from app.binary_search import BinarySearch

def test_binary_search():
    bs = BinarySearch()
    assert bs.binary_search([1, 3, 5, 7, 9], 7) == 3
    assert bs.binary_search([1, 3, 5, 7, 9], 1) == 0
    assert bs.binary_search([1, 3, 5, 7, 9], 9) == 4
    assert bs.binary_search([1, 3, 5, 7, 9], 10) == -1
