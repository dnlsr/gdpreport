from unittest.mock import patch, MagicMock
from gdpreport.cli import main


def test_cli_calls_functions():
    with patch('sys.argv', ['script', '--files', 'test.csv', '--report', 'average-gdp']):
        with patch('gdpreport.cli.read_csv_files') as mock_read:
            with patch('gdpreport.cli.generate_report') as mock_report:
                mock_read.return_value = []
                mock_report.return_value = "table"
                
                main()
                
                mock_read.assert_called_once_with(['test.csv'])
                mock_report.assert_called_once()