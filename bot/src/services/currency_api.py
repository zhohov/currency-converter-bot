import logging

import requests

from dto.convert_currency import ConvertInfo


def get_convert_currency(data: ConvertInfo) -> int:
    url = _get_convert_currency_url(
        currency_from=data.currency_from, currency_to=data.currency_to
    )

    return _convert_currency(url=url, data=data)


def _convert_currency(url: str, data: ConvertInfo) -> int:
    try:
        response = requests.get(url=url)
        currency_course = _parse_convert_currency_info(
            convert_info=response.json(), currency_to=data.currency_to
        )

        return currency_course * data.amount

    except Exception as e:
        logging.info(f"Exception {e}")


def _get_convert_currency_url(currency_from: str, currency_to: str) -> str:
    api_url = (
        "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/"
    )
    url = api_url + f"{currency_from}/{currency_to}.json"
    return url


def _parse_convert_currency_info(convert_info: dict, currency_to: str) -> int:
    return convert_info[currency_to]
