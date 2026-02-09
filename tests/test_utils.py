from gdpreport.utils import validate_data


def test_validate_data_good():
    data = [{'country': 'x', 'year': 1, 'gdp': 1.0, 'gdp_growth': 1.0,
             'inflation': 1.0, 'unemployment': 1.0, 'population': 1.0,
             'continent': 'x'}]
    
    assert validate_data(data)


def test_validate_data_bad():
    data = [{'country': 'x'}]
    
    assert not validate_data(data)