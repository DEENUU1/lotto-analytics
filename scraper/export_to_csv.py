import csv
from typing import List


def export_to_csv(data: List[dict], filename: str) -> None:
    fieldnames = [
        'number',
        'date',
        'numbers',
        'szostka_count',
        'szostka_value',
        'piatka_count',
        'piatka_value',
        'czworka_count',
        'czworka_value',
        'trojka_count',
        'trojka_value'
    ]

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry in data:
            flat_data = {
                'number': entry['number'],
                'date': entry['date'],
                'numbers': ','.join(map(str, entry['numbers'])),
                'szostka_count': 0,
                'szostka_value': 0,
                'piatka_count': 0,
                'piatka_value': 0,
                'czworka_count': 0,
                'czworka_value': 0,
                'trojka_count': 0,
                'trojka_value': 0
            }

            for result in entry.get('lottery_result', []):
                if result['type'].startswith("sz"):
                    flat_data['szostka_count'] = result['count']
                    flat_data['szostka_value'] = result['value']
                elif result['type'].startswith("pi"):
                    flat_data['piatka_count'] = result['count']
                    flat_data['piatka_value'] = result['value']
                elif result['type'].startswith("czw"):
                    flat_data['czworka_count'] = result['count']
                    flat_data['czworka_value'] = result['value']
                elif result['type'].startswith("tr"):
                    flat_data['trojka_count'] = result['count']
                    flat_data['trojka_value'] = result['value']

            writer.writerow(flat_data)
