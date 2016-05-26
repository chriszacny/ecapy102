__author__ = 'czacny'

import mechanize



def main():
    browser = mechanize.Browser()
    response = browser.open('https://diamond.treasury-factory.com/kiwi')

    browser.select_form('formlogin')
    browser.form['user'] = 'kbugayong'
    browser.form['companyname'] = 'Expedia'
    browser.form['k_password'] = r'test'
    submit_response = browser.submit()
    print(submit_response.read())

    input()


if __name__ == '__main__':
    main()



