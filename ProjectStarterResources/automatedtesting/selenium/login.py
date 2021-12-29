# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime

# define the Chrome options and webdriver
options = ChromeOptions()
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Start the browser and login with standard_user
def login (user, password):
    print (datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ' Starting the browser...')
    # --uncomment when running in Azure DevOps.
    # driver = webdriver.Chrome('/Users/simonkearn/Documents/NanoDegree/chromedriver')
    url = 'https://www.saucedemo.com/'
    print (datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ' Browser started successfully. Navigating to the demo page to login.')
    print (datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ' Accessing web site ' + url)
    driver.get(url)

    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ' Successfully logged in as ' + user )

def add_all_items_to_cart():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ' Adding all the items to the cart')
#    products = driver.find_elements(By.CSS_SELECTOR, "button[class='btn btn_primary btn_small btn_inventory']").text
    products = driver.find_elements(By.CLASS_NAME, 'btn_inventory')
#    products = driver.find_elements_by_class_name('btn_inventory')

    for items in products:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ' Adding item ' + items.get_property("name") + ' to the cart')
        items.click()

    print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ' All items added to the cart')
    shop_cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ' Total items in Shopping cart: ' + shop_cart.text)

def remove_all_items_from_cart():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ' Removing all items from the cart')

    products = driver.find_elements(By.CLASS_NAME, 'btn_inventory')

    for items in products:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ' Removing item ' + items.get_property("name") + ' from the cart')
        items.click()

    print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ' All items removed from the cart')
    assert not len(driver.find_elements(By.CLASS_NAME, 'shopping_cart_badge'))
    print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ' Shopping cart empty')


login('standard_user', 'secret_sauce')
add_all_items_to_cart()
remove_all_items_from_cart()

driver.quit()
