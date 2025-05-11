from playwright.async_api import Page
from datetime import datetime
import re
import argostranslate.translate

from_code = "zh"
to_code = "en"

async def read_table_data(context, header_locator: str, body_locator: str = 'tbody tr') -> list:
    header_cells = await context.page.locator(header_locator).all()
    visible_header_cells = [el for el in header_cells if await el.is_visible()]
    if not visible_header_cells:
        raise Exception(f"Unable to find visible header cells for {header_locator}")
    
    headers = []
    for header in visible_header_cells:
        content = clean_text(await header.text_content())
        translation = clean_text(translate(content), isChinese = False)
        if content:
            headers.append(content + "/" + translation)

    print(f"Found headers: {headers}") 

    body_rows = await context.page.locator(body_locator).all()
    data = []
        
    for row in body_rows:
        cells = await row.locator('td').all()
        
        cell_contents = []
        for cell in cells:
            content = clean_text(await cell.text_content())
            cell_contents.append(content)
        
        if any(cell_contents):
            entry = {}
            for i in range(min(len(headers), len(cell_contents))):
                if headers[i]: 
                    entry[headers[i]] = cell_contents[i]
            entry = add_metadata(entry, context.request.user_data) 
            data.append(entry)

    return data

async def read_detail_table(context, page: Page = None,
                            table_locator: str = "table", header_locator: str = "tbody tr td:nth-child(1)", 
                            body_locator: str = "tbody tr td:nth-child(2)", visibility_state: str = "visible",
                            timeout = 1500) -> list:
    if page is None:
        page = context.page

    header_locator = f"{table_locator} {header_locator}"
    body_locator = f"{table_locator} {body_locator}"
    
    await page.wait_for_selector(table_locator)
    await page.wait_for_selector(header_locator, state = visibility_state)
    await page.wait_for_selector(body_locator, state = visibility_state)
    
    await page.wait_for_timeout(timeout)
    
    header_cells = await page.locator(header_locator).all()
    body_cells = await page.locator(body_locator).all()

    print(f"Found {len(header_cells)} headers and {len(body_cells)} body cells")
    data = {}

    for _, (header, body) in enumerate(zip(header_cells, body_cells)):
        header_content = clean_text(await header.text_content())
        header_translated = clean_text(translate(header_content), isChinese = False)
        body_content = clean_text(await body.text_content())

        if header_translated:
            data[header_content + "/" + header_translated] = body_content
                        
    if data != {}:
        data = add_metadata(data, context.request.user_data)
        
    return data

# Hubei specific for now (2 headers per row), might generalize later
async def read_detail_table_overview(context, table_locator: str = "table", page = None) -> list:
    if page is None:
        page = context.page
    
    await page.wait_for_selector(table_locator)

    data = {} 

    for i in range(1, 3):
        row = page.locator(f"{table_locator} tr:nth-child({i})")
        header1 = clean_and_translate_all(await row.locator('td:nth-child(1)').text_content())
        body1 = clean_and_translate_all(await row.locator('td:nth-child(2)').text_content())
        header2 = clean_and_translate_all(await row.locator('td:nth-child(3)').text_content())
        body2 = clean_and_translate_all(await row.locator('td:nth-child(4)').text_content())

        if header1:
            data[header1] = body1
        if header2:
            data[header2] = body2

    # if data != {}:
    #     data = add_metadata(data, context.request.user_data)

    return data

async def read_detail_table_overview_henan(context, table_locator: str = "table", page = None) -> dict:
    if page is None:
        page = context.page
    
    await page.wait_for_selector(table_locator)
    data = {}

    row_index = 1
    while True:
        row = page.locator(f"{table_locator} tr:nth-child({row_index})")
        if await row.count() == 0:
            break

        header1 = await row.locator('th:nth-child(1)').text_content()
        header1 = header1 + "/" + clean_and_translate(header1)
        value1 = await row.locator('td:nth-child(2)').text_content()
        data[header1.strip()] = value1.strip()

        header2_locator = row.locator('th:nth-child(3)')
        if await header2_locator.count() > 0:
            header2 = await header2_locator.text_content()
            header2 = header2 + "/" + clean_and_translate(header2)
            value2 = await row.locator('td:nth-child(4)').text_content()
            data[header2.strip()] = value2.strip()

        row_index += 1

    if data:
        data = add_metadata(data, context.request.user_data)

    return data

async def read_detail_table_overview_hunan(context, table_locator: str = "table", page = None) -> dict:
    if page is None:
        page = context.page
    
    await page.wait_for_selector(table_locator)
    data = {}

    row_index = 1
    while True:
        row = page.locator(f"{table_locator} tr:nth-child({row_index})")
        if await row.count() == 0:
            break

        header1 = await row.locator('th:nth-child(1)').text_content()
        header1 = header1 + "/" + clean_and_translate(header1)
        value1 = await row.locator('td:nth-child(2)').text_content()
        data[header1.strip()] = value1.strip()

        header2_locator = row.locator('th:nth-child(3)')
        if await header2_locator.count() > 0:
            header2 = await header2_locator.text_content()
            header2 = header2 + "/" + clean_and_translate(header2)
            value2 = await row.locator('td:nth-child(4)').text_content()
            data[header2.strip()] = value2.strip()

        row_index += 1

    if data:
        data = add_metadata(data, context.request.user_data)

    return data

def add_metadata(data, user_data):
    data.update({
        'AD': user_data.get('ad'),
        'ListType': user_data.get('list_type'),
        'ListCode': user_data.get('list_code'),
        "English Name": user_data.get('list_name_en'),
        "Chinese Name": user_data.get('list_name_cn'),
        'Category': user_data.get('category'),
        'EntryType': user_data.get('entry_type'),
        'URL': user_data.get('url'),
        'ScrapedAt': datetime.now().isoformat(),
    })
    return data

def clean_text(text: str, isChinese = True) -> str:
    if isChinese:
        text = re.sub(r'\s+', '', text)
    text = text.replace('.', '')
    return text.strip()

def translate(text: str) -> str:
    return argostranslate.translate.translate(text, from_code, to_code).title()

def clean_and_translate(text: str, isChinese = True) -> str:
    cleaned_text = clean_text(text, isChinese)
    return translate(cleaned_text)

def clean_and_translate_all(text: str, isChinese = True) -> str:
    cleaned_text = clean_text(text, isChinese)
    return cleaned_text + "/" + translate(cleaned_text)

async def wait_for_captcha(captcha_selector: str, page: Page):
    await page.wait_for_timeout(1500)
    captcha = page.locator(captcha_selector)
    if await captcha.is_visible():
        print("CAPTCHA detected! Waiting for manual solution...")
        await page.wait_for_timeout(10000)
        while await captcha.is_visible():
            await page.wait_for_timeout(5000)
        print("CAPTCHA appears to be solved, continuing...")
        await page.wait_for_timeout(2000)