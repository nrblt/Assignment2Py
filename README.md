# Django with API




<h2>Installation</h2>

```
pip3 install  django
pip3 install requests
pip3 install beautifulsoup4
pip3 install selenium
```
Or you can just use 

```
pip3 install -r requirements.txt
```

And also you should download geckdriver it is needed to use selenium

<h2>Usage </h2>

```

from selenium import webdriver
url = 'https://etherscan.io/accounts'
driver = webdriver.Firefox(executable_path=r'/Users/macbook/node_modules/geckodriver/geckodriver')
driver.get(url)

```

<h2>Examples</h2>
By writing it you can scrap information from sites.
