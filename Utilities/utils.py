import time
import requests
from Base.base_driver import BaseDriver

def check_broken_link(driver,locator):
    base_page=BaseDriver(driver)
    links = base_page.find_elements(locator)
    broken_links =[]
    for link in links:
        url = link.get_attribute("href")
        if url:
            time.sleep(10)
            try:
                response = requests.get(url)
                if response.status_code == 404:
                    broken_links.append(url)
            except requests.exceptions.RequestException as e:
                broken_links.append(url)
    return broken_links
