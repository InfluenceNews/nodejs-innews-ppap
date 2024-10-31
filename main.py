import undetected_chromedriver as uc

driver = uc.Chrome()
driver.get(
    "https://www.khmertimeskh.com/501583112/cambodia-urges-cooperation-between-local-and-international-researchers/"
)

print(driver.title)

driver.quit()
