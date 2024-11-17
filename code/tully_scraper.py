import re
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tullysgoodtimes.com/menus/")

    titles = page.query_selector_all('h3.foodmenu__menu-section-title')
    scraped = []
    for title in titles:
        title_text = title.inner_text()
        print("MENU SECTION:", title_text)
        row = title.query_selector("~ *").query_selector("~ *")
        items = row.query_selector_all("div.foodmenu__menu-item-wrapper")
        for item in items:
            item_text = item.inner_text()
            scraped_item = extract_menu_item(title_text, item_text)
            print(f"  MENU ITEM: {scraped_item.name}")
            scraped.append(scraped_item.to_dict())

    df = pd.DataFrame(scraped)
    df.to_csv("cache/tullys_menu.csv", index=False)
        
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    tullyscraper(playwright)
