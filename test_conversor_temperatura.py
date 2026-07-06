from conversor_temperatura import celsius_para_fahrenheit, fahrenheit_para_celsius


def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32
    assert celsius_para_fahrenheit(100) == 212
    assert celsius_para_fahrenheit(-40) == -40


def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32) == 0
    assert fahrenheit_para_celsius(212) == 100
    assert fahrenheit_para_celsius(-40) == -40
