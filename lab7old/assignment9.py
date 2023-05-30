import asyncio
from aiohttp import web

async def handle_request(request):
    if request.method == 'GET':
        name, surname = get_cookie_data(request)
        return web.Response(text=get_form_html(name, surname), content_type='text/html')
    elif request.method == 'POST':
        data = await request.post()
        name = data.get('name')
        surname = data.get('surname')
        response = web.Response(text=f"Name: {name}, Surname: {surname}")
        set_cookie_data(response, name, surname)
        return response

def get_cookie_data(request):
    name = request.cookies.get('name')
    surname = request.cookies.get('surname')
    return name, surname

def set_cookie_data(response, name, surname):
    response.set_cookie('name', name)
    response.set_cookie('surname', surname)

def get_form_html(name=None, surname=None):
    return f"""
        <html>
        <form method="post">
            <input type="text" id="name" name="name" value="{name or ''}"><br>
            <input type="text" id="surname" name="surname" value="{surname or ''}"><br>
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
