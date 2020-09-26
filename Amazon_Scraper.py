from mechanize import Browser
from bs4 import BeautifulSoup
import sys
import re

br = Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4275.0 Safari/537.36")]

def product_search(keyword):
    br.open("https://www.amazon.co.jp/", timeout=10.0)
    br.select_form(action="/s/ref=nb_sb_noss")
    search_box = br.form.find_control(id="twotabsearchtextbox")
    search_box.value = keyword
    ret = br.submit()
    bs = BeautifulSoup(ret, 'html.parser')
    URLs = bs.select(".a-size-base.a-link-normal.a-text-normal")
    items = bs.select(".a-size-base-plus.a-color-base.a-text-normal")
    fees = bs.select(".a-size-base.a-link-normal.a-text-normal")
    images = bs.select(".a-section.aok-relative.s-image-square-aspect")

    url_list = []
    item_list = []
    fee_list = []
    image_list = []

    for image in images:
        image_list.append(image.find("img").get('src'))

    for item in items:
        item_list.append(item.string)

    for fee in fees:
        fee_list.append(fee.find("span", class_="a-price-whole").string)

    for URL in URLs:
        try:
            URL = re.search(r'dp(?:%2Fproduct-description)?%2F([0-9a-zA-Z]{10})', URL.get('href')).group().replace('%2F', '/')
            url_list.append(re.sub('^', 'https://www.amazon.co.jp/', URL))
        except:
            URL = re.search(r'dp(?:%2Fproduct-description)?/([0-9a-zA-Z]{10})', URL.get('href')).group()
            url_list.append(re.sub('^', 'https://www.amazon.co.jp/', URL))

    product_list = list(zip(item_list,fee_list,url_list,image_list))
    print(product_list)

product_search(sys.argv[1])
