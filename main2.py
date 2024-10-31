from selenium_driverless import webdriver
from selenium_driverless.types.by import By
import asyncio


async def main():
    options = webdriver.ChromeOptions()
    async with webdriver.Chrome(options=options) as driver:
        await driver.get(
            "https://www.khmertimeskh.com/501583112/cambodia-urges-cooperation-between-local-and-international-researchers/",
            wait_load=True,
        )
        await driver.sleep(0.5)
        # wait 10s for elem to exist
        await driver.find_element(By.ID, "mobilemenu", timeout=10)
        html_content = await driver.page_source
        with open("content.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print(await driver.title)

asyncio.run(main())
