from selenium import webdriver

browser =  browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
browser.get('http://localhost:8000')

assert 'Django' in browser.title