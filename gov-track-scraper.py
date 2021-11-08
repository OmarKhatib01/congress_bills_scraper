import requests
from bs4 import BeautifulSoup

dict1 = {
    77: [1941, 1942],
    78: [1943, 1944],
    79: [1945, 1946],
    80: [1947, 1948],
    81: [1949, 1950],
    82: [1951, 1952],
    83: [1953, 1954],
    84: [1955, 1956],
    85: [1957, 1958],
    86: [1959, 1960],
    87: [1961, 1962],
    88: [1963, 1964],
    89: [1965, 1966],
    90: [1967, 1968],
    91: [1969, 1970],
    92: [1971, 1972],
    93: [1973, 1974],
    94: [1975, 1976],
    95: [1977, 1978],
    96: [1979, 1980],
    97: [1981, 1982],
    98: [1983, 1984],
    99: [1985, 1986],
    100: [1987, 1988],
    101: [1989, 1990],
    102: [1991, 1992],
    103: [1993, 1994],
    104: [1995, 1996],
    105: [1997, 1998],
    106: [1999, 2000],
    107: [2001, 2002],
    108: [2003, 2004],
    109: [2005, 2006],
    110: [2007, 2008],
    111: [2009, 2010],
    112: [2011, 2012],
    113: [2013, 2014],
    114: [2015, 2016],
    115: [2017, 2018],
    116: [2019, 2020],
    117: [2021, 2022]
}

# progress bar function
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end="\r")
    # Print New Line on Complete
    if iteration == total:
        print()

# scrape csv's
for key in dict.keys(dict1):
    for year in dict1[key]:
        for bill_num in range(1, 2000):
            printProgressBar(bill_num, 2000, prefix=year, printEnd="\r\n")
            url_s = 'https://www.govtrack.us/congress/votes/' + str(key) + '-' + str(year) + '/s' + str(bill_num) \
                    + '/export/csv'
            r_s = requests.head(url_s)

            url_h = 'https://www.govtrack.us/congress/votes/' + str(key) + '-' + str(year) + '/h' + str(bill_num) \
                    + '/export/csv'
            r_h = requests.head(url_h)

            if "text/html" in r_s.headers["content-type"]:
                continue
            else:
                r_s = requests.get(url_s, allow_redirects=True)
                open('./csv_senate/congress_votes_' + str(key) + '-' + str(year) + '_s' + str(bill_num) +
                     '.csv', 'wb').write(r_s.content)

            if "text/html" in r_h.headers["content-type"]:
                continue
            else:
                r_h = requests.get(url_h, allow_redirects=True)
                open('./csv_house/congress_votes_' + str(key) + '-' + str(year) + '_h' + str(bill_num) +
                     '.csv', 'wb').write(r_h.content)


