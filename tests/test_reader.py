import tempfile
import os
from gdpreport.reader import read_csv_file


def test_read_csv_file_basic():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("""country,year,gdp,gdp_growth,inflation,unemployment,population,continent
USA,2023,1000,2.1,3.4,3.7,339,North America
USA,2022,900,1.5,2.0,4.0,338,North America""")
        tmp = f.name
    
    try:
        data = read_csv_file(tmp)
        
        assert len(data) == 2
        assert data[0]['country'] == 'USA'
        assert data[0]['gdp'] == 1000.0
        assert data[0]['continent'] == 'North America'
    finally:
        os.unlink(tmp)


def test_read_csv_file_types():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("""country,year,gdp,gdp_growth,inflation,unemployment,population,continent
Germany,2023,4000,2.1,3.0,4.0,83,Europe""")
        tmp = f.name
    
    try:
        data = read_csv_file(tmp)
        
        assert isinstance(data[0]['year'], int)
        assert isinstance(data[0]['gdp'], float)
        assert isinstance(data[0]['gdp_growth'], float)
        assert isinstance(data[0]['inflation'], float)
        assert isinstance(data[0]['continent'], str)
    finally:
        os.unlink(tmp)