import asyncio

from datetime import timedelta

from crawlee import Request, ConcurrencySettings
from crawlee.browsers import BrowserPool
from crawlee.configuration import Configuration
from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightPreNavigationContext

from routes import router

from config.ad_config import AD_CONFIG, get_urls
from utility.CamoufoxPlugin import CamoufoxPlugin

async def main() -> None:
    browser_pool = BrowserPool(
        plugins = [ CamoufoxPlugin(browser_options={
            "timeout": 600000,
        }) ],
        operation_timeout = timedelta(minutes = 10),
        browser_inactive_threshold = timedelta(minutes = 10),
        identify_inactive_browsers_interval = timedelta(minutes = 10),
        close_inactive_browsers_interval = timedelta(minutes = 10)
    )

    configuration = Configuration(
        available_memory_ratio = 0.5,
        internal_timeout = timedelta(minutes = 30)
    )
    
    concurreny_settings = ConcurrencySettings(max_concurrency = 1)

    crawler = PlaywrightCrawler(
        browser_pool=browser_pool,
        request_handler=router,
        request_handler_timeout = timedelta(minutes = 1000),
        configuration = configuration,
        concurrency_settings = concurreny_settings,
    )

    @crawler.pre_navigation_hook
    async def pre_navigation(context: PlaywrightPreNavigationContext) -> None:
        context.log.info(f'Navigating to {context.request.url} ...')
        context.page.set_default_navigation_timeout(0)

    # ADs = AD_CONFIG.keys() 
    ADs = ["Hubei"]
    requests = []

    for division in ADs:
        for list_code in AD_CONFIG[division]['lists'].keys():
            list_config = AD_CONFIG[division]['lists'][list_code]
            ad_name = AD_CONFIG[division]['name']['english']
            max_pages = list_config['max_pages']
            
            user_data = {
                'ad': ad_name,
                'division': division,
                'list_code': list_code,
                "list_name_en": list_config['name']['english'],
                "list_name_cn": list_config['name']['chinese'],
                'list_type': list_config['type'].value,
                'entry_type': list_config['entry_type'].value,
                'max_pages': max_pages,
                'url': list_config.get('url'),
                'category': list_config.get('category').value if list_config.get('category') is not None else None
            }
            
            if division == "Tibet":
                user_data['identifier'] = list_config['identifier']

            if division == "Shanxi":
                user_data['table_name'] = list_config['table_name']
                user_data['table_id'] = list_config['table_id']

            if division == "Anhui":
                user_data['element_number'] = list_config['element_number']
                
            if division == "Hebei":
                user_data['list_number'] = list_config['list_number']
                user_data['element_number'] = list_config['element_number']

            requests.extend([
                Request.from_url(
                    url=url,
                    label=ad_name.upper(),
                    user_data=user_data.copy(),  # Use copy to prevent mutation
                    unique_key=list_code # add unique key to be able to crawl pages with the same URL
                )
                for url in get_urls(division, list_code)
            ])

    print(requests)

    await crawler.run(requests = requests)

if __name__ == '__main__':
    asyncio.run(main())