from typing import List, Dict
from collections import defaultdict
from tabulate import tabulate


def generate_report(data: List[Dict], report_type: str) -> str:
    if report_type == "average-gdp":
        return generate_average_gdp_report(data)
    else:
        raise ValueError(f"неизвестный тип отчета: {report_type}")


def generate_average_gdp_report(data: List[Dict]) -> str:
    country_gdp = defaultdict(list)
    
    for row in data:
        country_gdp[row['country']].append(row['gdp'])
    
    averages = []
    for country, gdp_values in country_gdp.items():
        avg_gdp = sum(gdp_values) / len(gdp_values)
        averages.append((country, avg_gdp))
    
    averages.sort(key=lambda x: x[1], reverse=True)
    
    table_data = []
    for i, (country, avg_gdp) in enumerate(averages, 1):
        table_data.append([i, country, f"{avg_gdp:.2f}"])
    
    headers = ["", "country", "gdp"]
    return tabulate(table_data, headers=headers, tablefmt="pipe")