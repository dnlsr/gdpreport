from gdpreport.reports import generate_average_gdp_report


def test_average_gdp_simple():
    data = [
        {"country": "USA", "gdp": 1000},
        {"country": "USA", "gdp": 2000},
        {"country": "China", "gdp": 500},
        {"country": "China", "gdp": 700},
    ]
    
    result = generate_average_gdp_report(data)
    
    assert "USA" in result
    assert "China" in result
    
    assert "1500" in result
    assert "600" in result


def test_average_gdp_sorting():
    data = [
        {"country": "Small", "gdp": 100},
        {"country": "Big", "gdp": 1000},
    ]
    
    result = generate_average_gdp_report(data)
    
    assert "Small" in result
    assert "Big" in result
    
    result_lower = result.lower()
    big_index = result_lower.find("big")
    small_index = result_lower.find("small")
    
    if big_index != -1 and small_index != -1:
        assert big_index < small_index
    else:
        pass