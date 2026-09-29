from src.tools.tools import web_search

result = web_search.invoke({
    "query": "What is Model Context Protocol MCP?"
})

print(result)