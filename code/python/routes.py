from crawlee import Request
from crawlee.playwright_crawler import PlaywrightCrawlingContext
from crawlee.router import Router

from db.DatabaseManager import DatabaseManager
from config.ListType import ListType
from utility.utility import *
from utility.url_builder import *
from utility.pagination_utility import *

from uuid import uuid4

router = Router[PlaywrightCrawlingContext]()

db = DatabaseManager()

def insert_data(data: list, list_type: str):
    if list_type == ListType.BLACKLIST.value:
        db.insert_into_blacklist(data)
    elif list_type == ListType.REDLIST.value:
        db.insert_into_redlist(data)


@router.default_handler
async def default_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'default_handler is processing {context.request.url}')
    context.log.info(f'No handler found for {context.request.url}')
    context.request.no_retry = True

@router.handler('SHANGHAI')
async def shanghai_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'shanghai_handler is processing {context.request.url}')
    max_pages = context.request.user_data['max_pages']

    full_data = []

    for _ in range(1, max_pages):
        await context.page.wait_for_selector('.table')

        data = await read_table_data(context, '.table thead tr td', '.table tbody tr')
        full_data.extend(data)

        await context.page.get_by_text('下一页').click()
        await context.page.wait_for_timeout(2000)

    print(full_data)

    insert_data(full_data, context.request.user_data['list_type'])

    context.request.no_retry = True

@router.handler("BEIJING")
async def beijing_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'beijing_handler is processing {context.request.url}')

    full_data = []

    for _ in range(0, 5):
        await context.page.wait_for_selector('table')
        data = await read_table_data(context, header_locator ='.table_th th', body_locator = 'tr:not(:first-child)')
        full_data.extend(data)
        await context.page.locator('.next_page').click()
        await context.page.wait_for_timeout(2000)

    print(full_data)

    # insert_data(full_data, context.request.user_data['list_type'])

@router.handler('TIANJIN')
async def tianjin_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'tianjin_handler is processing {context.request.url}')

    data = []   
    
    await context.page.wait_for_selector('.table')
    await context.page.select_option('select', value='50')
    await context.page.wait_for_timeout(2500) # Wait for new table to load

    max_pages = context.request.user_data['max_pages']

    for i in range(1, max_pages + 1):
        await context.page.wait_for_timeout(10000)
        await context.page.wait_for_selector('.table')

        new_data = await read_table_data(context, 'thead tr th', '.table tbody tr')
        data.extend(new_data)

        if (i == max_pages):
            break 
        await context.page.locator('.layui-laypage-next').click()

    print(data)

    insert_data(data, context.request.user_data['list_type'])

    context.request.no_retry = True

@router.handler("TIBET")
async def tibet_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'tibet_handler is processing {context.request.url}')

    table_header_element = ".fright.trends-r thead tr th"
    identifier = context.request.user_data['identifier']
    table_body_rows = f"tbody#tbody_{identifier} tr"
    
    print(table_body_rows)
    
    await context.page.wait_for_selector(table_body_rows)
    
    full_data = []
    max_pages = context.request.user_data['max_pages']

    for _ in range(1, max_pages):
        await context.page.wait_for_selector(table_body_rows)
        full_data.extend(await read_table_data(context, table_header_element, table_body_rows))
        await context.page.locator(f'#Pagination_{identifier} .next').click()
        await context.page.wait_for_timeout(1000)

    insert_data(full_data, context.request.user_data['list_type'])

    context.request.no_retry = True

@router.handler("INNER MONGOLIA")
async def inner_mongolia_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'inner_mongolia_handler is processing {context.request.url}')

    full_data = []

    list_code = context.request.user_data['list_code']
    
    if list_code == "Class A Taxpayer":
        class_a_years_options = ["2022", "连续3年A级纳税人名单", "连续5年A级纳税人名单"]
        max_pages = [20, 20, 74]

        for option in class_a_years_options:
            await context.page.select_option('select', value=option)
            await context.page.locator('button').click()
            for _ in range(1, max_pages[class_a_years_options.index(option)]):
                await context.page.wait_for_selector('table')
                data = await read_table_data(context, 'thead tr th', 'tbody tr')
                full_data.extend(data)
                await context.page.get_by_text('下一页').click()
                await context.page.wait_for_timeout(2000)   
    else:
        max_pages = context.request.user_data['max_pages']
        for _ in range(1, max_pages):
            await context.page.wait_for_selector('table')
            header_selector = 'tbody tr:first-child th' if list_code == "Exemplary Cases of Honesty and Trustworthiness" else 'thead tr th'
            data = await read_table_data(context, header_selector, 'tbody tr')
            full_data.extend(data)
            await context.page.get_by_text('下一页').click()
            await context.page.wait_for_timeout(2000)
            
    insert_data(full_data, context.request.user_data['list_type'])

    print(full_data)

@router.handler("NINGXIA")
async def ningxia_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'ningxia_handler is processing {context.request.url}')

    await context.page.wait_for_load_state('domcontentloaded')
    await context.page.wait_for_selector('#pageconterright')
    await context.page.wait_for_selector('table.layui-table')
    
    table_header = 'table.layui-table thead tr th'
    table_rows = 'table.layui-table tbody tr'
    
    await context.page.wait_for_selector(table_header)
    await context.page.wait_for_selector(table_rows)
    
    data = await read_table_data(context, table_header, table_rows)

    insert_data(data, context.request.user_data['list_type'])

    context.request.no_retry = True

@router.handler("XINJIANG")
async def xinjiang_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'xinjiang_handler is processing {context.request.url}')
    context.request.no_retry = True

    max_pages = 10 # Website will block any query after 10 pages

    for i in range(0, max_pages):
        await context.page.wait_for_selector('.table')
        
        detail_page_selector = '.pn-loperator'
        
        for item in await context.page.locator(detail_page_selector).all():
            if await item.is_visible():
                await item.click()
            else:
                continue
                
            await context.page.wait_for_selector('iframe')
            await context.page.wait_for_timeout(2000)
            
            iframes = await context.page.locator('iframe').all()
            for iframe in iframes:
                detail_page_url = await iframe.get_attribute('src')
                if detail_page_url and detail_page_url != "https://www.creditxj.gov.cn/My97DatePicker/My97DatePicker.html":
                    print("Request added")
                    uuid = uuid4().hex
                    detail_request = Request.from_url(
                        url=detail_page_url,
                        label="XINJIANG_DETAIL",
                        user_data=context.request.user_data,
                        unique_key = uuid
                    )
                    await context.add_requests([detail_request])
            
            await context.page.wait_for_timeout(2000)
            await context.page.locator('.layui-layer-close').click()
        if (i != max_pages - 1):
            await context.page.locator('.layui-laypage-next').click()
            await context.page.wait_for_timeout(2000)
    
@router.handler("XINJIANG_DETAIL")
async def xinjiang_detail_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'xinjiang_detail_handler is processing {context.request.url}')

    print("Detail handler called")
    data = [await read_detail_table(context)]

    insert_data(data, context.request.user_data['list_type'])
    print(data)

    context.request.no_retry = True

# Has session related anti-scraping measures for chromium/firefox, see notes for more infos -> Bypassing it via Camoufox 
@router.handler("ANHUI") 
async def anhui_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'anhui_handler is processing {context.request.url}')

    await context.page.wait_for_selector('div.is-main')

    if (context.request.user_data['list_type'] == ListType.BLACKLIST.value):
        await context.page.locator('ul.lists li:nth-child(3)').click()
    elif (context.request.user_data['list_type'] == ListType.REDLIST.value):
        await context.page.locator('ul.lists li:nth-child(4)').click()
    await context.page.wait_for_selector('div.is-main')

    element_number = context.request.user_data['element_number']
    all_items = context.page.locator(f'div.credit-publicity-item:nth-child({element_number})')
    count = await all_items.count()
    
    for i in range(count):
        item = all_items.nth(i)
        if await item.is_visible():
            await item.click()
            break

    table_selector = 'table.bordered.center.color-th'
    await context.page.wait_for_selector(table_selector)

    # Since all cells are clickable, we want to avoid data duplication by only clicking on one element per row
    first_cell_per_row  = await context.page.locator(f'{table_selector} tbody tr td:first-child').all()

    detail_data_all = []

    for item in first_cell_per_row:
        try:    
            await context.page.wait_for_timeout(1500)
            async with context.page.context.expect_page() as new_page_info:
                await item.click()
                
                            
            detail_page = await new_page_info.value
                        
            detail_table_selector = 'table.infor'
            detail_data = await read_detail_table(context, detail_page, detail_table_selector)
            
            print(f"Current detail data: {detail_data} \n")

            detail_data_all.append(detail_data)

            await detail_page.close()
            
            await context.page.wait_for_selector(table_selector)
            
        except Exception as e:
            context.log.error(f"Error processing item: {str(e)}")
            continue
        
    
    print(f"Full data: {detail_data_all}")

    insert_data(detail_data_all, context.request.user_data['list_type'])

    context.request.no_retry = True

@router.handler("GANSU")
async def gansu_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'gansu_handler is processing {context.request.url}')
    
    context.request.no_retry = True

    await context.page.wait_for_timeout(25000)
    
    await context.page.wait_for_selector('table')

    data = await read_table_data(context, 'thead th', 'tbody tr')

    insert_data(data, context.request.user_data['list_type'])

@router.handler("GUANGDONG")
async def guangdong_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'guangdong_handler is processing {context.request.url}')
    max_pages = context.request.user_data['max_pages']

    for i in range(1, max_pages + 1):
        await context.page.wait_for_selector('table.tytable')

        await context.page.wait_for_timeout(1500)

        await context.enqueue_links(
            selector = 'td a',
            label = "GUANGDONG_DETAIL",
            user_data = context.request.user_data
        )
        
        if (i == max_pages):
            break
        await context.page.locator('.js-page-next').click()

    context.request.no_retry = True
    
@router.handler("GUANGDONG_DETAIL")
async def guangdong_detail_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'guangdong_detail_handler is processing {context.request.url}')
    
    await context.page.wait_for_timeout(3000)

    data = await read_detail_table(context)

    insert_data([data], context.request.user_data['list_type'])

    context.request.no_retry = True

@router.handler("HAINAN")
async def hainan_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'hainan_handler is processing {context.request.url}')

    table_selector = 'table.table.table-striped.table-bordered.table_col.table-overflow'
    
    max_pages = context.request.user_data['max_pages']

    for _ in range(1, max_pages):
        await context.page.wait_for_selector(table_selector)

        # Detail page logic 
        detail_cells_selector = f'{table_selector} tbody tr td:last-child a'
        detail_items = await context.page.locator(detail_cells_selector).all()
        print(f"Found {len(detail_items)} detail items")

        for detail_item in detail_items:
            # The detail cells contain the onclick event, which contains the parameters for the detail page -> We can reconstruct the URL with these
            onclick = await detail_item.get_attribute('onclick')
            params = await context.page.evaluate("""
                (onclick) => {
                    const match = onclick.match(/showDetail\\('([^']+)','([^']+)','([^']+)'\\)/);
                    return match ? {
                        recid: match[1],
                        recflag: match[2],
                        messageid: match[3]
                    } : null;
                }
            """, onclick)    

            # TODO: Make this URL configurable?
            detail_page_url = f"https://xyhn.hainan.gov.cn/CreditHnExtranetWeb/xygs/showDetail.do?recid={params['recid']}&messageid={params['messageid']}&recflag={params['recflag']}"

            detail_request = Request.from_url(
                url = detail_page_url,
                label = "HAINAN_DETAIL",
                user_data = {
                    **context.request.user_data,
                }
            )
            
            await context.add_requests([detail_request])

        await context.page.locator('.pageDown').click()
        await context.page.wait_for_timeout(2000)

    context.request.no_retry = True
    
@router.handler("HAINAN_DETAIL")
async def hainan_detail_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'hainan_detail_handler is processing {context.request.url}')

    list_code = context.request.user_data['list_code']
    list_type = context.request.user_data['list_type']
    entry_type = context.request.user_data['entry_type']

    metadata = {
        'list_code': list_code,
        'list_type': list_type,
        'entry_type': entry_type,
    }

    detail_data = await read_detail_table(context)

    full_data = detail_data | metadata

    print(full_data)
    
    insert_data([full_data], context.request.user_data['list_type'])
    context.request.no_retry = True

@router.handler("HEILONGJIANG")
async def heilongjiang_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'heilongjiang_handler is processing {context.request.url}')

    await context.page.wait_for_selector('#resUl')

    entries = await context.page.locator('#resUl li a').all()
    
    detail_data_all = []
    
    for entry in entries:
        async with context.page.context.expect_page() as new_page_info:
            await entry.click()
                        
        detail_page = await new_page_info.value
                    
        detail_data = await read_detail_table(context, detail_page, header_locator = "tr td:nth-child(1)", body_locator = "tr td:nth-child(2)")
        
        detail_data_all.append(detail_data)

        await detail_page.close()
        
        await context.page.wait_for_selector('#resUl')

    insert_data(detail_data_all, context.request.user_data['list_type'])

# Manual handling of Captchas is needed, run browser in non-headless mode 
@router.handler("HENAN")
async def henan_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'henan_handler is processing {context.request.url}')

    max_pages = context.request.user_data['max_pages']

    captcha_selector = '.layui-layer-iframe'
    
    context.request.no_retry = True

    for i in range(0, max_pages + 1):
        print(i)
        await wait_for_captcha(captcha_selector, context.page)
        await context.page.wait_for_selector('table')
        await context.page.wait_for_selector('table tr td a') # since table loads dynamically, we have to wait for the elements to load
        await context.page.wait_for_timeout(4000)
        
        # Print number of tbody tr:first-child td a elements
        count = await context.page.locator('tbody tr td a').count()
        print(f"Number of tbody tr td a elements: {count}")

        await context.enqueue_links(
            selector = 'tbody tr td a',
            label = "HENAN_DETAIL",
            user_data = context.request.user_data,
        )

        if (i <= max_pages - 1):
            next_button = context.page.locator('.layui-laypage-next')
            await context.page.wait_for_timeout(1000)        
            await next_button.click()
    
@router.handler("HENAN_DETAIL")
async def henan_detail_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'henan_detail_handler is processing {context.request.url}')
    
    captcha_selector = '.layui-layer-iframe'
    await wait_for_captcha(captcha_selector, context.page)
    
    await context.page.wait_for_selector('table')
    captcha_selector = '.layui-layer-iframe'
    await wait_for_captcha(captcha_selector, context.page)
    data = await read_detail_table_overview_henan(context)
    print(data)
    insert_data([data], context.request.user_data['list_type'])

@router.handler("HUBEI")
async def hubei_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'hubei_handler is processing {context.request.url}')

    await context.page.wait_for_selector('div.xzxk-box')

    table_class_selector = ".xzls-lis"

    await context.enqueue_links(
        selector = f"{table_class_selector} a",
        label = "HUBEI_DETAIL",
        user_data = context.request.user_data
    )

@router.handler("HUBEI_DETAIL")
async def hubei_detail_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'hubei_detail_handler is processing {context.request.url}')
    context.request.no_retry = True

    await wait_for_captcha('.layui-layer', context.page)

    detail_base_table_selector = ".basetable"
    general_detail_data = await read_detail_table_overview(context, detail_base_table_selector)
    print(general_detail_data)

    list_tab_selector = "ul.tab-title li"
    
    valid_list_tabs = ["诚实守信", "严重失信"]

    await context.page.wait_for_selector(list_tab_selector)

    list_tab_locator = await context.page.locator(list_tab_selector).all()
    
    print("going through list tabs")
    
    # Create a list to store all entries that will be inserted into the database
    all_entries_to_insert = []

    for list_tab in list_tab_locator:
        if (await list_tab.locator('em').count() > 0):
            list_tab_name = clean_text(await list_tab.text_content())
            enum_text = await list_tab.locator('em').text_content()
            list_tab_name = list_tab_name.replace(enum_text, '')
            
            if (list_tab_name not in valid_list_tabs):
                continue
            print(list_tab_name)
            await list_tab.click()
            await context.page.wait_for_timeout(10000)

            parent_div = ".result-tab2" if (list_tab_name == "诚实守信") else ".result-tab3"
            result_table_selector = f"{parent_div} div.result-table"
            if (await context.page.locator(result_table_selector).count() == 0):
                continue
            await context.page.wait_for_selector(result_table_selector)
            result_tables = await context.page.locator(result_table_selector).all()
            list_types = await context.page.locator("#cssxCatalog li").all()
            print(await context.page.locator(result_table_selector).count())
            
            for i, _ in enumerate(result_tables):
                print(f"Processing table {2*i + 2} with selector: {result_table_selector}")
                table_selector = f"{parent_div} div.result-table:nth-child({2*i + 2}) table"
                result_table_data = await read_detail_table(context, table_locator=table_selector)
                
                # Create a new entry that combines the general data with this specific table data
                entry = general_detail_data.copy()  # Create a copy of the general details
                entry['list_tab_name'] = list_tab_name  # Add which tab this data came from
                entry['table_index'] = i  # Add index to track which table within the tab
                
                # Merge the table data with the entry
                entry.update(result_table_data)
                
                # Add this entry to our list of entries to insert
                all_entries_to_insert.append(entry)
                
                print(f"Processing table {i+1} with selector: {table_selector}")
                print(result_table_data)

    print(f"Total entries to insert: {len(all_entries_to_insert)}")
    
    print(all_entries_to_insert)
    
    # Insert all entries as individual items in the database
    # insert_data(all_entries_to_insert, context.request.user_data['list_type'])
    
@router.handler("HUNAN")
async def hunan_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'hunan_handler is processing {context.request.url}')
    context.request.no_retry = True
    
    general_table_rows_selector = 'div.default_pgContainer table tr'
    
    isBlacklist = context.request.user_data['list_type'] == ListType.BLACKLIST
    
    if (isBlacklist):
        await context.page.wait_for_selector(general_table_rows_selector)
        await context.page.select_option('select#first', value='湖南省')
        await context.page.locator('.searchBtn2:first-of-type').click()
        await context.page.wait_for_timeout(2500)  
    
    for _ in range(0, 10):  
        
        await wait_for_captcha('div#check', context.page)
    
        for i in range (2, 11):
            row = context.page.locator(f'{general_table_rows_selector}:nth-child({i})')
            
            clickable_element = row.locator("td:nth-child(1)")
            
            async with context.page.context.expect_page() as list_page_info:
                await clickable_element.click()
                
            await context.page.wait_for_timeout(2000)
                
            list_page = await list_page_info.value
            
            table_selector = "table.xzcf_bg"

            await list_page.wait_for_selector(table_selector)
            
            data = {}

            row_index = 1
            while True:
                row = list_page.locator(f"{table_selector} tr:nth-child({row_index})")
                if await row.count() == 0:
                    break

                header1 = await row.locator('td:nth-child(1)').text_content()
                header1 = header1 + "/" + clean_and_translate(header1)
                value1 = await row.locator('td:nth-child(2)').text_content()
                data[header1.strip()] = value1.strip()

                header2_locator = row.locator('td:nth-child(3)')
                if await header2_locator.count() > 0:
                    header2 = await header2_locator.text_content()
                    header2 = header2 + "/" + clean_and_translate(header2)
                    value2 = await row.locator('td:nth-child(4)').text_content()
                    data[header2.strip()] = value2.strip()

                row_index += 1

            if data:
                data = add_metadata(data, context.request.user_data)
                
            if (isBlacklist):
                reasons_for_inclusions = await list_page.locator('#heimd_lrmdsy').text_content()
            
                data['列入事由/Reason for Inclusion'] = reasons_for_inclusions.strip()
            
            print(data)
            insert_data([data], context.request.user_data['list_type'])
            
            await list_page.close()    
            
        next_button_selector = '.default_pgNext'
        await context.page.locator(next_button_selector).click()
    
    
@router.handler("JIANGSU")
async def jiangsu_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'jiangsu_handler is processing {context.request.url}')
    
    # Metadata: Differs throughout lists, could be limit of shown elements, but also total # of records + date of last update
    try:
        additional_metadata = clean_text(
            await context.page.locator('span.limit').text_content(timeout=5000)
        )
    except Exception:
        additional_metadata = None   
     
    list_name = context.request.user_data['list_code']
    
    list_name = context.request.user_data.get('list_code', '')
    full_data = []
    
    filter_selectors = {
        "Eligible for Trustworthiness Incentives": '.searchBox div.box-nav',
        "General Redlist": 'span#abb'
    }
        
    if (list_name in filter_selectors):
        filter_items = await context.page.locator(filter_selectors[list_name]).all()
        
        for filter in filter_items:
            await filter.click()
            await context.page.wait_for_timeout(3000)
            redlist_name = await filter.text_content()
            
            if (list_name == "General Redlist"):
                detail_page_base_url = "https://credit.jiangsu.gov.cn/credit/credit/p/common/integrity_cite/webCiteDetail.do?uk="
                await handle_pagination(
                    context,
                    { 'specific_redlist_name': redlist_name + "/" + translate(redlist_name)  },
                    'div.pageDown',
                    'onclick',
                    'tbody tr',
                    delimiter = '"',
                    base_url = detail_page_base_url
                )
            else:
                data = await read_table_data(context, 'thead tr th', 'tbody tr')
                full_data.extend(data)
    else: 
        # The page loads all table entries at once, so we can directly extract the data
        if (list_name == "Railway Violations"):
            rows = await context.page.locator('tbody tr').all()
            detail_page_base_url = "https://credit.jiangsu.gov.cn/credit/credit/p/common/illegal_travel/webDetail.do?uk="
            for row in rows:
                detail_url = await generate_detail_url(row, detail_page_base_url, delimiter = "'")
                if detail_url:
                    await add_detail_request(
                        context,
                        detail_url,
                        "JIANGSU_DETAIL",
                    )
        else:
            data = await read_table_data(context, 'thead tr th', 'tbody tr')
            print(data)
            for item in data:
                item['additional_metadata'] = additional_metadata
            full_data.extend(data)
    
    if (full_data.__len__ != 0):
        insert_data(full_data, context.request.user_data['list_type'])

    context.request.no_retry = True
    
@router.handler("JIANGSU_DETAIL")
async def jiangsu_detail_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'jiangsu_detail_handler is processing {context.request.url}')

    detail_data = await read_detail_table(context, header_locator = 'tbody tr th', 
                                            body_locator = 'tbody tr td', visibility_state = 'attached')


    num_of_clicks = await context.page.locator('.content label').text_content()
        
    extra_metadata = {
        "num_of_clicks": num_of_clicks,
    }
    
    if (context.request.user_data.get('specific_redlist_name') != None):
        extra_metadata.update(
            "specific_redlist_name", context.request.user_data['specific_redlist_name'],
        )
        
    detail_data.update(extra_metadata)
    
    insert_data([detail_data], context.request.user_data['list_type'])

    context.request.no_retry = True
        
@router.handler("SHAANXI")
async def shaanxi_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'shaanxi_handler is processing {context.request.url}')
    
    max_pages = context.request.user_data['max_pages']
    
    for _ in range(1, max_pages):
        await context.page.wait_for_selector('table')
        await context.page.wait_for_timeout(1000)
        await context.enqueue_links(
            selector = 'tbody tr td a',
            label = "SHAANXI_DETAIL",
            user_data = context.request.user_data
        )
        await context.page.get_by_text('下一页').click()

    context.request.no_retry = True
    
@router.handler("SHAANXI_DETAIL")
async def shaanxi_detail_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'shaanxi_detail_handler is processing {context.request.url}')

    data = await read_detail_table(context, table_locator = 'table#table_list', header_locator = 'tbody tr th', body_locator = 'tbody tr td')

    insert_data([data], context.request.user_data['list_type'])
        
@router.handler("SHANXI")
async def shanxi_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'shanxi_handler is processing {context.request.url}')

    await context.page.wait_for_selector('table#myTable')
    
    await handle_pagination(
        context=context,
        additional_metadata = context.request.user_data,
        next_button_selector = '.layui-laypage-next',
        onClick_attribute_name = 'onclick',
        onClick_element_selector = 'table#myTable tbody tr td:first-child',
        delimiter = "'",
        detail_url_builder = shanxi_detail_url_builder,
        should_continue = shanxi_should_continue,
        timeout = 2000
    )

    context.request.no_retry = True
    
@router.handler("SHANXI_DETAIL")
async def shanxi_detail_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'shanxi_detail_handler is processing {context.request.url}')
    
    await context.page.wait_for_timeout(1000)

    data = await read_detail_table(context, table_locator = 'table#contentTable', header_locator = 'tr td:nth-child(1)', body_locator = 'tr td:nth-child(2)')

    # print(data)
    insert_data([data], context.request.user_data['list_type'])
        
@router.handler("SICHUAN")
async def sichuan_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'sichuan_handler is processing {context.request.url}')

    searchButtonSelector = 'span#searchHmd'
    await context.page.wait_for_selector(searchButtonSelector)
    await context.page.locator(searchButtonSelector).click()
    
    await wait_for_captcha('div#tianai-captcha', context.page)

    await context.page.wait_for_selector('table')

    max_pages = context.request.user_data['max_pages']
    data = []
    
    for _ in range(0, max_pages):
        await wait_for_captcha('div#tianai-captcha', context.page)
        base_data = await read_table_data(context, 'thead tr th', 'tbody tr')
        print(base_data)
            
        data.extend(base_data)
        
        await context.page.locator('.layui-laypage-next').click()
        await context.page.wait_for_timeout(5000)

    # print(data) 
    insert_data(data, context.request.user_data['list_type'])
    
    context.request.no_retry = True
    
# TODO: Possibly handle difference between national and provincial lists
@router.handler('ZHEJIANG')
async def zhejiang_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'zhejiang_handler is processing {context.request.url}')

    await context.page.wait_for_selector('div.tabs')
    
    tab_number = 1
    list_number = 1
    
    tab = context.page.locator(f'div.tabs > span:nth-child({tab_number})')
    await context.page.wait_for_selector('div#redList')
    await context.page.wait_for_selector('div.gs_list')
    lists = await context.page.locator('div.gs_list p.p1').all()
    print(f'Found {len(lists)} lists')
    specific_list = lists[list_number]
    
    print(tab)
    print(specific_list)
    
    await context.page.wait_for_timeout(1500)
    # async with context.page.context.expect_page() as new_page_info:
    #     await tab.click()
        
    # await context.page.wait_for_timeout(20000)
        
    async with context.page.context.expect_page() as list_page_info:
        await specific_list.click()
        
    await context.page.wait_for_timeout(20000)
        
    list_page = await list_page_info.value
    
    table_header_selector = 'div.ivu-table-header'
    table_body_selector = 'div.ivu-table-body table'
    list_data = await read_table_data(context, f'{table_header_selector} thead tr th', f'{table_body_selector} tbody tr')

    print(list_data)

    await list_page.close()
        
    # await tab.click()
    # await specific_list.click()
    # await context.page.wait_for_timeout(20000)
    # await specific_list.click()
    
    # table_header_selector = 'div.ivu-table-header'
    # table_body_selector = 'div.ivu-table-body table'
    # data = await read_table_data(context, f'{table_header_selector} thead tr th', f'{table_body_selector} tbody tr')

    # print(data)

    # insert_data(data, context.request.user_data['list_type'])

    context.request.no_retry = True

@router.handler("LIAONING")
async def liaoning_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'liaoning_handler is processing {context.request.url}')

    max_pages = context.request.user_data['max_pages']
    
    full_data = []
    for _ in range(1, max_pages):
        table_selector = 'table#table_list'
        await context.page.wait_for_selector(table_selector)
        data = await read_table_data(context, f'{table_selector} tbody tr th', f'{table_selector} tbody tr:not(:first-of-type)')
        full_data.extend(data)
        next_button_selector = context.page.get_by_text('下一页')
        await next_button_selector.click()
        await context.page.wait_for_timeout(2000)

    print(full_data)

    insert_data(full_data, context.request.user_data['list_type'])
    
@router.handler("SHANDONG")
async def shandong_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'shandong_handler is processing {context.request.url}')

    max_pages = context.request.user_data['max_pages']

    full_data = []
    for _ in range(1, max_pages):
        await context.page.wait_for_timeout(1500)
        table_selector = '.table'
        await context.page.wait_for_selector(table_selector)
        
        await context.enqueue_links(
            selector = 'tr td:first-child a',
            label = "SHANDONG_DETAIL",
            user_data = context.request.user_data
        ) 
        
        next_button_selector = context.page.get_by_text('下一页')
        await next_button_selector.click()
        await context.page.wait_for_timeout(2000)
        
@router.handler("SHANDONG_DETAIL")
async def shandong_detail_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'shandong_detail_handler is processing {context.request.url}')

    data = await read_detail_table(context, table_locator = 'table#table_list', header_locator = 'tbody tr th', body_locator = 'tbody tr td')
    
    print(data)

    insert_data([data], context.request.user_data['list_type'])
    
@router.handler("JILIN")
async def jilin_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f"jilin_handler is processing {context.request.url}")
    context.request.no_retry = True
    
    await context.page.wait_for_selector('tbody')
    
    await context.page.locator('.el-pagination__sizes input').click()
    await context.page.locator('.el-select-dropdown__item:nth-child(3)').click()
    await context.page.wait_for_timeout(3000)
    
    data = await read_table_data(context, header_locator = 'thead tr th', body_locator = 'tbody tr')
    
    print(data)
    
    insert_data(data, context.request.user_data['list_type'])

    # clickable_elements  = await context.page.locator(f'tbody tr td:nth-child(2)').all()
    
    # await context.enqueue_links_by_clicking_elements(
    #     selector = "tbody tr td:nth-child(2)", 
    #     label = "JILIN_DETAIL", 
    #     user_data = context.request.user_data
    # )
    
    # test  = context.page.locator(f'tbody tr:first-child td:nth-child(2)')
    # await test.click()
    # await context.page.wait_for_timeout(3000)
    # print(await context.page.title())
    
    # await context.page.wait_for_selector('.el-col')
    # print(await context.page.locator('.left-tabs-title').text_content())
    # await context.page.go_back()
    
    # await context.page.wait_for_timeout(10000)
    
    # async with context.page.context.expect_page(timeout=60000) as new_page_info:
    #     await test.click()
    # new_page = await new_page_info.value
    # print(new_page.title())
    # await new_page.wait_for_load_state('networkidle')

    # detail_data_all = []

    # for item in clickable_elements:
    #     try:    
    #         async with context.page.context.expect_page() as new_page_info:
    #             await item.click()
                        
    #         print("test")
                        
    #         detail_page = await new_page_info.value
            
    #         await detail_page.wait_for_selector('.el-col')
    #         detail_rows = await detail_page.locator('.el-col').all()
            
    #         print(detail_rows)
            
    #         detail_data = {}
            
    #         for row in detail_rows:
    #             header = await row.query_selector('.el-form-item__label').text_content()
    #             body = await row.query_selector('.el-form-item__content label').text_content()
    #             print(f"{header}: {body}")
    #             detail_data[header] = body
            
    #         print(f"Current detail data: {detail_data} \n")
            

    #         # detail_data_all.append(detail_data)

    #         # await new_page_info.page.go_back()
            
    #             # await context.page.wait_for_selector(table_selector)
            
    #     except Exception as e:
    #         context.log.error(f"Error processing item: {str(e)}")
    #         continue
    
    # full_data = []    
    
    
@router.handler("HEBEI")
async def hebei_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'hebei_handler is processing {context.request.url}')
    
    list_number = context.request.user_data['list_number']
    await context.page.locator(f'div.con a:nth-child({list_number})').click()
    
    await context.page.wait_for_selector('span.bin-tag')
    specific_list_number = context.request.user_data['element_number']
    await context.page.locator(f'span.bin-tag:nth-child({specific_list_number})').click()
    
    await context.page.wait_for_selector('div.bin-table')
    
    for _ in range(1, context.request.user_data['max_pages']):
        await context.enqueue_links(
            selector = 'td a',
            label = "HEBEI_DETAIL",
            user_data = context.request.user_data
        ) 
        
        await context.page.locator('.bin-page-next').click()
        await context.page.wait_for_timeout(2000)
    
    await context.page.wait_for_timeout(5000)
    
@router.handler("HEBEI_DETAIL")
async def hebei_detail_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'hebei_detail_handler is processing {context.request.url}')
    
    data = await read_detail_table(context)
    
    insert_data([data], context.request.user_data['list_type'])