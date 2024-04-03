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

def get_lottery_results(content: str) -> Dict[str, Any]:
    res = {}

    soup = BeautifulSoup(content, "html.parser")
    pass



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

            lottery_result = get_lottery_results(lottery_result_url)
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
