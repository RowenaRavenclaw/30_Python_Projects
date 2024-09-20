from fake_useragent import UserAgent
import csv
import requests
from http import HTTPStatus


def get_website(csv_path: str) -> list[str]:
    website: list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[0]:
                website.append(f'https://{row[0]}')
            else:
                website.append(row[0])
        return website


def get_user_agent() -> str:
    ua = UserAgent()
    return ua.firefox


def get_status_description(status_code: int) -> str:
    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}) {value.description}'
            return description

    return "(???) Unknown status code..."


def check_website(website: str, user_agent):
    try:
        code: int = requests.get(website, headers={'USer-Agent': user_agent}).status_code
        print(website, get_status_description(code))
    except Exception:
        print(f'**Could not get Information from the website "{website}"')


def main():
    sites: list[str] = get_website('websites.csv')
    user_agent: str = get_user_agent()

    for site in sites:
        check_website(site, user_agent)


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [1, 2, 3]

    print(a is b)
