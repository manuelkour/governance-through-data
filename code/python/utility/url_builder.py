from .pagination_utility import generate_detail_url

async def shanxi_detail_url_builder(element, context, delimiter, base_url):
    detail_page_id = await generate_detail_url(element, base_url, delimiter)
    table_name = context.request.user_data['table_name']
    table_id = context.request.user_data['table_id']
    table_name_ch = "EB356C9C143C4D070428EB31B99D96AB"
    
    if detail_page_id and table_name and table_id:
        detail_page_url = (
            f"https://creditsx.fgw.shanxi.gov.cn/page/customize_data_detail.html?"
            f"id={detail_page_id}&tableName={table_name}&tableId={table_id}&tableNameCh={table_name_ch}"
        )
        return detail_page_url
    else:
        context.log.error("Missing detail page ID, table name, or table ID for Shanxi")
        return None