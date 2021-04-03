from app import (lowest_temp, most_fluctuation, most_fluctuation_in_range,
                 remap, total_fluc_degree)

test_file = "data_test.csv"


def test_lowest_temp():
    assert lowest_temp(test_file) == (98, 2000.375)


def test_most_flucation():
    assert most_fluctuation(test_file) == 98


def test_most_flucation_in_range():
    assert most_fluctuation_in_range(test_file, 2000.375, 2000.958) == 68
    assert most_fluctuation_in_range(test_file, 2000.375, 2000.575) == 98
    assert most_fluctuation_in_range(test_file, 2000.375, 2000.968) == 98
    assert most_fluctuation_in_range(test_file, 2000.375, 2000.375) == -1
    assert most_fluctuation_in_range(test_file, 6000.375, 2000.375) == -1
    assert most_fluctuation_in_range(test_file, 2000.375, 2000.376) == -1
    assert most_fluctuation_in_range(test_file, 2000.968, 2000.375) == -1


def test_remap():
    assert remap(test_file) == {
        68: {
            "date": [2000.375, 2000.542, 2000.958, 2000.968],
            "temp": [5.0, 0.0, 5.0, 1.0],
        },
        78: {"date": [2001.125], "temp": [20.4]},
        98: {"date": [2000.375, 2000.575, 2000.968], "temp": [-13.3, 10.4, 21.8]},
    }


def test_total_fluc_degree():
    assert total_fluc_degree([0]) == 0
    assert total_fluc_degree([5]) == 5
    assert total_fluc_degree([5, 5]) == 0
    assert total_fluc_degree([0, 5]) == 5
    assert total_fluc_degree([5, 0]) == 5
    assert total_fluc_degree([5, 0, 5]) == 10
    assert total_fluc_degree([5, 5, 0]) == 5
    assert total_fluc_degree([0, 5, 0]) == 10
    assert total_fluc_degree([5, 5, 5]) == 0
    assert total_fluc_degree([5, 0, 5, 1]) == 14
