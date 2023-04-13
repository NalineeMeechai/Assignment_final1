from function import calculate
import pytest

@pytest.mark.validate  
def test_input_a():
    input = "a"
    expected_result = "กรุณากรอกเป็นตัวเลข"
    actual_result = calculate(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_input_0():
    input = 0
    expected_result = "กรุณากรอกตั้งแต่ 1 ฟองขึ้นไป"
    actual_result = calculate(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_input_1_point_1():
    input = 1.1
    expected_result = "กรุณากรอกเป็นจำนวนเต็มบวก"
    actual_result = calculate(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_input_minus_1_point_1():
    input = -1.1
    expected_result = "กรุณากรอกเป็นจำนวนเต็มบวก"
    actual_result = calculate(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_input_1():
    input = 1
    expected_result = 4
    actual_result = calculate(input)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_input_12():
    input = 12
    expected_result = 36
    actual_result = calculate(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_input_15():
    input = 15
    expected_result = 48
    actual_result = calculate(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_input_24():
    input = 24
    expected_result = 72
    actual_result = calculate(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_input_26():
    input = 26
    expected_result = 80
    actual_result = calculate(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_input_60():
    input = 60
    expected_result = 175
    actual_result = calculate(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_input_63():
    input = 63
    expected_result = 187
    actual_result = calculate(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_input_100():
    input = 100
    expected_result = 296
    actual_result = calculate(input)
    assert expected_result == actual_result