from scraper.merge_csv import merge_csv


def main() -> None:
    merge_csv("./scraped_data/lottoplus", output_filename="merged_lottoplus.csv")
    merge_csv("./scraped_data/lotto", output_filename="merged_lotto.csv")
    merge_csv("./scraped_data/minilotto", output_filename="mini_lotto.csv")


if __name__ == "__main__":
    main()
