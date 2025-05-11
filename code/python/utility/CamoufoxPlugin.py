from camoufox import AsyncNewBrowser
from typing_extensions import override

from crawlee.browsers import PlaywrightBrowserController, PlaywrightBrowserPlugin

class CamoufoxPlugin(PlaywrightBrowserPlugin):

    @override
    async def new_browser(self) -> PlaywrightBrowserController:
        if not self._playwright:
            raise RuntimeError('Playwright browser plugin is not initialized.')

        return PlaywrightBrowserController(
            browser = await AsyncNewBrowser(self._playwright, headless=False, **self._browser_options),
            max_open_pages_per_browser = 5,
            header_generator = None,  # This turns off the crawlee header generation. Camoufox has its own.
        )