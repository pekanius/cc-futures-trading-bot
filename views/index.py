from aiohttp import web


async def get(request):
    text = "Dashboard"
    return web.Response(text=text)