import asyncio
from aiohttp import web

async def handle_request(request):
    return web.Response(text="Piotr Jurek")

async def start_server():
    app = web.Application()
    app.router.add_route('*', '/', handle_request)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8000)
    await site.start()
    print("Server started at http://localhost:8000")
    await asyncio.Event().wait()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server())
