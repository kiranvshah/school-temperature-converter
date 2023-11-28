from convert import convert_temp
import pytest


class TestConvertTemp:
    def test_from_celsius(self):
        assert convert_temp(4.9, 'celsius', 'fahrenheit') == 40.82
        assert convert_temp(0, 'celsius', 'kelvin') == 273.15
        assert convert_temp(-10, 'celsius', 'rankine') == 473.67

    def test_from_fahrenheit(self):
        assert convert_temp(21, 'fahrenheit', 'celsius') == pytest.approx(-6.11111, abs=0.00001)
        assert convert_temp(10, 'fahrenheit', 'kelvin') == pytest.approx(260.92777, abs=0.00001)
        assert convert_temp(-40, 'fahrenheit', 'rankine') == 419.67

    def test_fom_kelvin(self):
        assert convert_temp(0, 'kelvin', 'celsius') == -273.15
        assert convert_temp(34, 'kelvin', 'fahrenheit') == pytest.approx(-398.47, abs=0.01)
        assert convert_temp(104, 'kelvin', 'rankine') == pytest.approx(187.2, abs=0.00001)

    def test_from_rankine(self):
        assert convert_temp(192, 'rankine', 'celsius') == pytest.approx(-166.483, abs=0.01)
        assert convert_temp(43, 'rankine', 'fahrenheit') == -416.67
        assert convert_temp(24, 'rankine', 'kelvin') == pytest.approx(13.33, abs=0.01)

    def test_erroneous(self):
        with pytest.raises(ValueError) as error:
            convert_temp(93, 'apples', 'celsius')
        assert str(error.value) == 'Provided original_unit was not known'

        with pytest.raises(ValueError) as error:
            convert_temp(21, 'celsius', 'bananas')
        assert str(error.value) == 'Provided destination_unit was not known'
