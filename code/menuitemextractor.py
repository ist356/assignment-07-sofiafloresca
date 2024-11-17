if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price:str) -> float:
    price = price.replace('$','')
    price = price.replace(',','')
    cleaned = float(price)
    return cleaned

def clean_scraped_text(scraped_text: str) -> list[str]:
    scraped_text_list = scraped_text.split('\n')
    cleaned_list = []
    unwanted = ["", "NEW", "NEW!", "GS", "V", "P", "S"]
    for item in scraped_text_list:
        if item not in unwanted:
            cleaned_list.append(item)
    return cleaned_list

def extract_menu_item(title:str, scraped_text: str) -> MenuItem:
    scraped_text_list = clean_scraped_text(scraped_text)
    name = scraped_text_list[0]
    price = clean_price(scraped_text_list[1])
    if len(scraped_text_list) < 3:
        description = "No description available."
    else:
        description = scraped_text_list[2]
    item = MenuItem(name=name, price=price, category=title, description=description)
    return item



if __name__=='__main__':
    text = '''
NEW!

Tully Tots

$11.79

Made from scratch with shredded potatoes, cheddar-jack cheese and Romano cheese all rolled up and deep-fried. Served with a spicy cheese sauce.
        '''

    item = extract_menu_item("Appetizers", text)