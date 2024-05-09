from splinter import Browser
import time as t
browser = Browser('chrome')


GOOGLE_FORM = "https://forms.gle/7iXfpovxBXKLArSV7"

browser = Browser('chrome')

browser.visit('https://appbrewery.github.io/Zillow-Clone/?')

address_listings= []

addresses = browser.find_by_tag('address')

for address in addresses:
    address_listings.append(address.text)

price_listings = []

prices = browser.find_by_css('.PropertyCardWrapper__StyledPriceLine')

for price in prices:
    stripped_price = price.text.replace("/mo", "").split("+")[0]
    price_listings.append(stripped_price)


link_listings = []

link_wrapper = browser.find_by_css('.StyledPropertyCardDataWrapper')

for link_wrapper in link_wrapper:
    link = link_wrapper.find_by_tag('a')
    link_listings.append(link['href'])



browser2 = Browser('chrome')




for address in range(len(address_listings)):
    browser2.visit(GOOGLE_FORM)
    address_input = browser2.find_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = browser2.find_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = browser2.find_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = browser2.find_by_text('Submit')
    address_input.fill(address_listings[address])
    price_input.fill(price_listings[address])
    link_input.fill(link_listings[address])
    submit.click()
    t.sleep(2)
    if "submit another response" in browser.url:
        # Handle this case, e.g., navigate back to the form page
        browser.back()


while True:
    pass

