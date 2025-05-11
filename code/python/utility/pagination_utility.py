from crawlee import Request
from .utility import wait_for_captcha

async def handle_pagination(context, additional_metadata, next_button_selector,
                            onClick_attribute_name, onClick_element_selector , delimiter, 
                            base_url = None, detail_url_builder = None, should_continue = None,
                            timeout = 0):
    await context.page.wait_for_selector(next_button_selector)
    next_button = context.page.locator(next_button_selector)
    
    while True:
        await context.page.wait_for_timeout(timeout)
        await wait_for_captcha('div#zzcContent', context.page)
        
        onClick_elements = await context.page.locator(onClick_element_selector).all()
        for element in onClick_elements:
            if detail_url_builder:
                detail_url = await detail_url_builder(
                    element, context, delimiter, base_url
                )
            else:
                detail_id = await generate_detail_url(element, base_url, delimiter)
                if detail_id:
                    detail_url = detail_id
                else:
                    detail_url = None

            if detail_url:
                original_label = context.request.label
                await add_detail_request(
                    context,
                    detail_url,
                    f"{original_label}_DETAIL".upper(),
                    additional_metadata
                )
        
        if should_continue:
            continue_pagination = await should_continue(next_button)
        else:
            continue_pagination = await next_button.get_attribute(onClick_attribute_name) is not None
            
        if not continue_pagination:
            break
            
        await next_button.click()
        await context.page.wait_for_timeout(2000)
    
    context.log.info("Reached the end of pagination")
    
async def generate_detail_url(element, base_url = None, delimiter: str = ""):
    row_onClick = await element.get_attribute('onClick') or await element.get_attribute('onclick')
    if row_onClick:
        try:
            element_id = row_onClick.split(delimiter)[1]
            if base_url:
                return f"{base_url}{element_id}"
            return element_id
        except IndexError:
            print("Delimiter not found or incorrect in onClick attribute.")
            return None
    return None

async def add_detail_request(context, url, label, additional_data=None):
    user_data = {**context.request.user_data}
    if additional_data:
        user_data.update(additional_data)
        
    await context.add_requests([
        Request.from_url(
            url=url,
            label=label,
            user_data=user_data.copy()
        )
    ])
    
# AD specific should_continue functions

async def shanxi_should_continue(next_button):
    button_class = await next_button.get_attribute('class')
    return 'layui-disabled' not in button_class