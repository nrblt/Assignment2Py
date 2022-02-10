from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from .models import Address


def index(request):
    Address.objects.all().delete()
    url = 'https://etherscan.io/accounts'
    driver = webdriver.Firefox(executable_path=r'/Users/macbook/node_modules/geckodriver/geckodriver')
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ddlRecordsPerPage"]/option[4]').click()
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    attrs = soup.find_all('a')
    addresses = []
    for i in attrs:
        if "0x" in str(i) and "Donate" not in str(i):
            address = str(i)
            start = address.find("0x")
            x = slice(start, start + 42)
            addresses.append(address[x])
    api = 'https://api.etherscan.io/api?module=account&action=balancemulti&address='
    arr = []

    for i in range(101):
        if i == 20 or i == 40 or i == 60 or i == 80 or i == 100:
            api += '&tag=latest&apikey=XED6G9XDWAU6PJN16WXCTKWCW4JAFA41MR'
            arr.append(requests.get(api).json())
            api = 'https://api.etherscan.io/api?module=account&action=balancemulti&address='
        if i < 100:
            api += addresses[i] + ','

    for i in arr:
        for address in i['result']:
            ether = int(address['balance']) // 100000000000000
            a = Address(account=address['account'], balance=ether)
            a.save()

    addresses = Address.objects.all()
    responses = {
        'addresses': addresses
    }
    return render(request, 'index.html', responses)
