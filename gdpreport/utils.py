from typing import List, Dict


def validate_data(data: List[Dict]) -> bool:
    if not data:
        return False
    
    required_fields = {
        'country', 'year', 'gdp', 'gdp_growth', 
        'inflation', 'unemployment', 'population', 'continent'
    }
    
    return all(field in data[0] for field in required_fields)