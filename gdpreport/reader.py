import csv
from typing import List, Dict


def read_csv_file(file_path: str) -> List[Dict]:
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['year'] = int(row['year'])
            row['gdp'] = float(row['gdp'])
            row['gdp_growth'] = float(row['gdp_growth'])
            row['inflation'] = float(row['inflation'])
            row['unemployment'] = float(row['unemployment'])
            row['population'] = float(row['population'])
            data.append(row)
    return data


def read_csv_files(file_paths: List[str]) -> List[Dict]:
    all_data = []
    for file_path in file_paths:
        try:
            data = read_csv_file(file_path)
            all_data.extend(data)
        except FileNotFoundError:
            print(f"предупреждение: файл {file_path} не найден")
            raise
    return all_data