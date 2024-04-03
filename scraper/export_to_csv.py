import csv
from typing import List


def export_to_csv(data: List[dict], filename: str) -> None:
    fieldnames = [
        'number',
        'date',
        'numbers',
        'szóstka_count',
        'szóstka_value',
        'piątka_count',
        'piątka_value',
        'czwórka_count',
        'czwórka_value',
        'trójka_count',
        'trójka_value'
    ]

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry in data:
            flat_data = {
                'number': entry['number'],
                'date': entry['date'],
                'numbers': ','.join(map(str, entry['numbers'])),
                'szóstka_count': 0,
                'szóstka_value': 0,
                'piątka_count': 0,
                'piątka_value': 0,
                'czwórka_count': 0,
                'czwórka_value': 0,
                'trójka_count': 0,
                'trójka_value': 0
            }

            for result in entry.get('lottery_result', []):
                if result['type'].startswith("sz"):
                    flat_data['szóstka_count'] = result['count']
                    flat_data['szóstka_value'] = result['value']
                elif result['type'].startswith("pi"):
                    flat_data['piątka_count'] = result['count']
                    flat_data['piątka_value'] = result['value']
                elif result['type'].startswith("czw"):
                    flat_data['czwórka_count'] = result['count']
                    flat_data['czwórka_value'] = result['value']
                elif result['type'].startswith("tr"):
                    flat_data['trójka_count'] = result['count']
                    flat_data['trójka_value'] = result['value']

            writer.writerow(flat_data)
