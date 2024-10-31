import Lab2 as lab2

def test_min_max():
    result = []
    test_arr = [1,2,3,4,5]
    test=[1,5]
    result = lab2.find_min_max(test_arr)

    assert(result==test)

def test_calc_average():
    result = []
    test_arr = [1,2,3,4,5]
    test=3
    result=lab2.calc_average(test_arr)

    assert(result==test)

def test_calc_median_temp():
    result = []
    test_arr = [1,2,3,4,5]
    test=3
    result=lab2.cal_median_temperature(test_arr)

    assert(result==test)