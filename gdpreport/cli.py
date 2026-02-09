import argparse
from .reports import generate_report
from .reader import read_csv_files


def main():
    parser = argparse.ArgumentParser(
        description="генератор отчетов по экономическим данным из csv файлов"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="пути к csv файлам"
    )
    parser.add_argument(
        "--report",
        choices=["average-gdp"],
        required=True,
        help="тип отчета для генерации"
    )
    
    args = parser.parse_args()
    
    data = read_csv_files(args.files)
    
    report_table = generate_report(data, args.report)
    
    print(report_table)


if __name__ == "__main__":
    main()