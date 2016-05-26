#Requires Python 2...

import mechanize
import getpass
from bs4 import BeautifulSoup


def main():
    username = raw_input("Salesforce.com Username: ")
    password = getpass.getpass("Password: ")

    browser = mechanize.Browser()
    browser.open(r'https://login.salesforce.com')
    browser.select_form("login")
    browser.form['username'] = username
    browser.form['pw'] = password
    browser.submit()

    dom = BeautifulSoup(browser.response().read())
    all_divs = dom.find_all('div')
    print(all_divs)

if __name__ == '__main__':
    main()