import os
from typing import Final

import pandas as pd

OUTPUT_DIRECTORY_NAME: Final[str] = "./output/"

if not os.path.exists(OUTPUT_DIRECTORY_NAME):
    os.makedirs(OUTPUT_DIRECTORY_NAME)
    print(f"Directory '{OUTPUT_DIRECTORY_NAME}' created successfully!")
else:
    print(f"Directory '{OUTPUT_DIRECTORY_NAME}' already exists.")


def merge_csv(directory: str, output_filename: str) -> None:
    csv_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.csv')]
    if not csv_files:
        print("No CSV files found in the directory.")
        return

    merged_df = pd.DataFrame()

    for file in csv_files:
        df = pd.read_csv(file)
        merged_df = pd.concat([merged_df, df])

    output_path = f"{OUTPUT_DIRECTORY_NAME}{output_filename}"
    merged_df.to_csv(f"{output_path}", index=False)

    print(f"Merged data saved to {output_path}")
