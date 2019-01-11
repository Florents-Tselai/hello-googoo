#!/usr/bin/env python
# coding: utf-8


from argparse import ArgumentParser

from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


def main():
    arg_parser = ArgumentParser(description='Search Google & Print URLs in the Command Line')
    arg_parser.add_argument('-p', '--pages', default=1, type=int, help='Number of pages', required=False)
    arg_parser.add_argument('-q', '--query', nargs=1, help='Search query string', required=True)

    args = arg_parser.parse_args()
    chrome_options = ChromeOptions()
    chrome_options.headless = True
    chrome_options.add_argument("--disable-logging")

    with Chrome(options=chrome_options) as browser:
        browser.delete_all_cookies()
        browser.get("https://google.com/?q=" + args.query[0])
        browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]').click()
        soup = BeautifulSoup(browser.page_source, 'lxml')

        for div in soup.find_all('div', class_='g'):
            a = div.find('a', recursive=True)
            if not a.get('href', '').startswith('/search?'):
                print(a.get('href'))


if __name__ == '__main__':
    main()
