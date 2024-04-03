from typing import Optional, List, Dict, Any

import requests
from bs4 import BeautifulSoup


def get_page_content(url: str) -> Optional[str]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as err:
        print(err)
        return None
    except requests.exceptions.RequestException as err:
        print(err)
        return None
    except Exception as err:
        print(err)
        return None


def get_lottery_results(content: str) -> List[Dict[str, Any]]:
    res = []

    soup = BeautifulSoup(content, "html.parser")

    table_tag = soup.find("table", class_="dl_wygrane_table")

    tr_tags = table_tag.find_all("tr")

    for i in range(1, len(tr_tags)):
        data = {}

        td_tags = tr_tags[i].find_all("td")

        data["type"] = td_tags[0].text.replace("ó", "o").replace("ą", "a")
        data["count"] = int(td_tags[1].text)
        data["value"] = float(td_tags[2].text.replace(" ", ""))

        res.append(data)

    return res


def parse_content(content: str) -> List[Optional[Dict[str, Any]]]:
    res = []

    soup = BeautifulSoup(content, "html.parser")
    results_div = soup.find("div", class_="lista_ostatnich_losowan")

    if not results_div:
        return res

    results = results_div.find_all("ul")

    if not results:
        return res

    for result in results:
        data = {}
        li_tags = result.find_all("li")

        number = li_tags[0].text.replace(".", "")

        data["number"] = int(number)
        data["date"] = li_tags[1].text

        numbers = []

        for i in range(2, 8):
            numbers.append(int(li_tags[i].text))

        data["numbers"] = numbers

        a_tag = result.find("a")

        if a_tag:
            lottery_result_url = a_tag["href"]
            get_lottery_page = get_page_content(lottery_result_url)
            lottery_result = get_lottery_results(get_lottery_page)
            data["lottery_result"] = lottery_result

        res.append(data)

    print(res)


def main() -> None:
    year = "2024"
    url = f"https://megalotto.pl/wyniki/lotto/losowania-z-roku-{year}"
    content = get_page_content(url)
    parse_content(content)

    return None


if __name__ == "__main__":
    main()
