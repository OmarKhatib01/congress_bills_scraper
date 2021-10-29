import requests
from bs4 import BeautifulSoup

# senate bills
for congress_num in range(77, 118):
    for year in range(1941, 2022):
        for bill_num in range(1, 2000):
            url = 'https://www.govtrack.us/congress/votes/' + str(congress_num) + '-' + str(year) + '/s' + str(bill_num)\
                  + '/export/csv'
            page = requests.get(url)
            url_soup = BeautifulSoup(page.content, 'html.parser')
            r = requests.head(url)
            if "text/html" in r.headers["content-type"]:
                continue
            else:
                r = requests.get(url, allow_redirects=True)
                open('./csv_senate/congress_votes_' + str(congress_num) + '-' + str(year) + '_s' + str(bill_num) +
                     '.csv', 'wb').write(r.content)

# house bills
for congress_num in range(77, 118):
    for year in range(1941, 2022):
        for bill_num in range(1, 2000):
            url = 'https://www.govtrack.us/congress/votes/' + str(congress_num) + '-' + str(year) + '/h' + str(bill_num)\
                  + '/export/csv'
            page = requests.get(url)
            url_soup = BeautifulSoup(page.content, 'html.parser')
            r = requests.head(url)
            if "text/html" in r.headers["content-type"]:
                continue
            else:
                r = requests.get(url, allow_redirects=True)
                open('./csv_house/congress_votes_' + str(congress_num) + '-' + str(year) + '_h' + str(bill_num) +
                     '.csv', 'wb').write(r.content)