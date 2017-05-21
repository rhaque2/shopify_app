# IT WORKS! Still working on JS phantom though
# Run to get product and order details
import shopify
import requests
import json
import urllib2
import sys
import time
import unittest
import urlparse
import yaml
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from json import JSONEncoder
from urlparse import urlparse


API_KEY = 'ff190765308cc34365729a21cf057433'
SHARED_SECRET = '55e4f9544f3c7790ff9830ee34094084'

shop_url = "https://%s:%s@test-store-1-863.myshopify.com/admin" % (API_KEY, SHARED_SECRET)
shopify.ShopifyResource.set_site(shop_url)

shopify.Session.setup(api_key=API_KEY, secret=SHARED_SECRET);    """supply two parameters"""
session = shopify.Session("test-store-1-863.myshopify.com");     """instantiate session object"""
scope=["read_products","write_orders"]

permission_url = session.create_permission_url(scope, "http://unioncrate.com/")
print permission_url
post_to_perm = requests.post(permission_url)
print ''
print post_to_perm


driver = webdriver.Chrome('C:\Users\Ruhul\Web Drivers\chromedriver.exe')
#driver = webdriver.PhantomJS(executable_path='C:\PhantomJs\place\phantomjs\phantomjs.exe')
driver.get(permission_url)
login_page='https://test-store-1-863.myshopify.com/admin/auth/login'
correct_page='https://test-store-1-863.myshopify.com/admin'

email = driver.find_element_by_id( "login-input" )
password = driver.find_element_by_id( "password" )
submit = driver.find_element_by_name( "commit" )

email.send_keys("justruhul94@gmail.com")
password.send_keys("teststore1")

submit.click()

# After App is installed, the rest of the code runs

while True:
    if "code=" in driver.current_url:
        print (driver.current_url)
        parsed_url = urlparse(driver.current_url)
        query = parsed_url.query
        code = query[5:37]
        print code
        post_code = requests.post('https://test-store-1-863.myshopify.com/admin/oauth/access_token?client_id=ff190765308cc34365729a21cf057433&client_secret=55e4f9544f3c7790ff9830ee34094084&code='+code)
        print post_code
        print ''
        print ''
        print post_code.content
        token = post_code.content  # content is in a string
        token = json.loads(token)  # convert content into a dictionary/json
        print type(token)
        print ''
        token = token['access_token']  # store the access_token
        print token
        print ''  # After here we start applying the token
        headers = {'content-type': 'application/json', 'X-Shopify-Access-Token': token}
        get_products = requests.get('https://test-store-1-863.myshopify.com/admin/products.json', headers=headers)
        print get_products
        print ''
        print get_products.content  # List of products obtained
        print type(get_products.content)
        print ''
        products = json.loads(get_products.content)  # convert content into a dictionary/json
        print type(products)
        print ''
        print products
        print ''
        print ''
        get_orders = requests.get('https://test-store-1-863.myshopify.com/admin/orders.json', headers=headers)
        print get_orders
        print ''
        print get_orders.content    # List of orders obtained
        break
    else:
        time.sleep(5)

driver.quit()


















'''
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:\Users\Ruhul\Chrome Driver\chromedriver.exe')
driver.get('https://test-store-1-863.myshopify.com/admin/auth/login')
time.sleep(5)
login_page='https://test-store-1-863.myshopify.com/admin/auth/login'
correct_page='https://test-store-1-863.myshopify.com/admin'

try:
    element = driver.find_element_by_id( 'login' )
except NoSuchElementException:
    self.fail( "found: %s" % 'login' )

try:
    element = driver.find_element_by_id( 'remember-me' )
except NoSuchElementException:
    self.fail( "found: %s" % 'remember-me' )


# Fetch username, password input boxes and submit button
# This time I'm now testing if the elements were found.
# See the previous exmaples to see how to do that.
email = driver.find_element_by_id( "login-input" )
password = driver.find_element_by_id( "password" )
submit = driver.find_element_by_name( "commit" )

# Input text in username and password inputboxes
email.send_keys("justruhul94@gmail.com")
password.send_keys("teststore1")

# Click on the submit button
submit.click()

# Create wait obj with a 5 sec timeout, and default 0.5 poll frequency
wait = WebDriverWait(driver, 5)

# Test that login was successful by checking if the URL in the browser changed
try:
    page_loaded = wait.until_not(
        lambda driver: driver.current_url == login_page
    )
except TimeoutException:
    self.fail("Loading timeout expired")

# Assert that the URL is now the correct post-login page
def URL_is_correct_page(self):
    self.assertEqual(
    driver.current_url,
    correct_page,
    msg="Successful Login"

'''