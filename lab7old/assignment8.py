import asyncio
from aiohttp import web

async def handle_request(request):
    if request.method == 'GET':
        return web.Response(text=get_form_html(), content_type='text/html')
    elif request.method == 'POST':
        data = await request.post()
        name = data.get('name')
        surname = data.get('surname')
        return web.Response(text=f"{name} {surname}")

def get_form_html():
    return """
        <html>
        <form method="post">
            <input type="text" id="name" name="name"><br>
            <input type="text" id="surname" name="surname"><br>
            <input type="submit" value="Submit">
        </form>
        </html>
    """

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
