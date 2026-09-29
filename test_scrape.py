from src.tools.tools import scrape_url

result = scrape_url.invoke({
    "url": "https://modelcontextprotocol.io/docs/getting-started/intro"
})

print(result[:1500])