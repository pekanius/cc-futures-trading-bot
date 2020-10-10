from aiohttp import web
from views import index


def setup():
    app = web.Application()
    app.add_routes([web.get('/', index.get)])
    web.run_app(app)


if __name__ == '__main__':
    setup()
