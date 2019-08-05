import requests, re, xlrd, xlwt
from bs4 import BeautifulSoup
import time, os.path, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from random import choice
from multiprocessing import Pool

def read_file(URL):
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get(URL)
    time.sleep(5)



def main():
    count = input('Кол-во потоков ')
    rb = xlrd.open_workbook('photo_list.xlsx')
    sheet = rb.sheet_by_index(0)
    vals = [i for rownum in range(sheet.nrows) for i in sheet.row_values(rownum) if len(i)>=1]

    with Pool(int(count)) as p:
        p.map(read_file, vals)












if __name__ == '__main__':
    main()