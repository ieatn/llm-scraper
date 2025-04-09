import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, DefaultMarkdownGenerator
import requests
from bs4 import BeautifulSoup

async def main():
    browser_config = BrowserConfig(headless=True, verbose=True)
    async with AsyncWebCrawler(config=browser_config) as crawler:
        crawler_config = CrawlerRunConfig(
            markdown_generator=DefaultMarkdownGenerator()
        )
        result = await crawler.arun(
            url="http://quotes.toscrape.com", config=crawler_config
        )
        print(result.markdown.raw_markdown)  

asyncio.run(main())
