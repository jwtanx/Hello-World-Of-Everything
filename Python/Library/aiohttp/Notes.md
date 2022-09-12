# Aiohttp
For non-fullstack REST api call
[Github](https://github.com/aio-libs/aiohttp)
[Documentation](https://docs.aiohttp.org/en/stable/)
[Demos](https://github.com/aio-libs/aiohttp-demos)

## Notes
```py
# pip install aiohttp
import aiohttp
```

### BASIC
```py
from aiohttp import web
import json

async def handle(request):
    response = {"status" : "success"}
    return web.Response(text=json.dumps(response), status=200)

async def predict(request):
    try:
        url = request.query["url"]
        response = {"status": "success", "message": f"{url} api call is accepted"}
        return web.json_response(response) # Returning the information in json format
        # return web.Response(text=json.dumps(response), status=200)
    except Exception as e:
        response = {"status": "failed", "message": str(e)}
        return web.Response(text=json.dumps(response), status=500)

app = web.Application()
app.router.add_get("/", handle)
app.router.add_get("/predict", predict)
# http://localhost:8899/predict?url=http://www.google.com

web.run_app(app, host=8899)
```

### BASIC EXAMPLE 2
```py
from aiohttp import web
import logging, asyncio, yaml

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def wshandle(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.text:
            await ws.send_str("Hello, {}".format(msg.data))
        elif msg.type == web.WSMsgType.binary:
            await ws.send_bytes(msg.data)
        elif msg.type == web.WSMsgType.close:
            break

    return ws


logging.basicConfig(level=logging.DEBUG)
loop = asyncio.get_event_loop()

with open("config.yml", 'rt') as f:
    conf = yaml.load(f)

app = web.Application()
host, port = conf['host'], conf['port']
web.run_app(app, host=host, port=port)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/echo', wshandle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)

```

### ROUTES DECORATORS
```py
routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")

@routes.get('/user')
async def get_user(request):
    try:
        name = request.query["name"]
        response = {"status": "success", "message": f"Found {name}"}
        return web.Response(text=json.dumps(response), status=200)
    except Exception as e:
        response = {"status": "failed", "message": str(e)}
        return web.Response(text=json.dumps(response), status=500)

app = web.Application()
app.add_routes(routes)
web.run_app(app)
```

Other than `get` ...
```py
@routes.get('/')
async def get_handler(request):
    ...

@routes.post('/post')
async def post_handler(request):
    ...

@routes.put('/put')
async def put_handler(request):
    ...

app.add_routes(routes)
```

### RESPONSE IN HTML
[Reference](https://stackoverflow.com/questions/54165443/how-to-return-html-response-from-aiohttp-web-server)
```py
from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def index_handler(request):
    return web.Response(
        text='<h1>Hello!</h1>',
        content_type='text/html')

app = web.Application()
app.add_routes(routes)
# or instead of using RouteTableDef:
# app.router.add_get('/', index_handler)

web.run_app(app)
```