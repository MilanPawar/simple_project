

from  selenium import webdriver
browser=webdriver.Edge("/Users/jay/Downloads/edgedriver_win64 (1)/msedgedriver")
browser.get("https://www.seleniumhq.org")
elem=browser.find_element_by_link_text('Downloads')
elem.click()
search=browser.find_element_by_id('docsearch')
search.click()

search=browser.find_element_by_id('docsearch-input')
search.send_keys('hi')