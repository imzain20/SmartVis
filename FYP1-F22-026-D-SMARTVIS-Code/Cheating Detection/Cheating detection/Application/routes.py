from starlette.templating import Jinja2Templates
from starlette.routing import Route
from starlette.responses import RedirectResponse
from starlette.endpoints import WebSocketEndpoint
from CDApp.controller import Controller
import asyncio

import os
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

template = Jinja2Templates(directory=dir_path+'/templates')


async def startAll(request):
    Controller.generatePose = True
    Controller.detectCheat = True
    return RedirectResponse(url='/')


async def stopAll(request):
    Controller.generatePose = False
    Controller.detectCheat = False
    return RedirectResponse(url='/')


async def startGeneratePose(request):
    Controller.generatePose = True
    return RedirectResponse(url='/')


async def stopGeneratePose(request):
    Controller.generatePose = False
    return RedirectResponse(url='/')


async def startCheatDetection(request):
    Controller.detectCheat = True
    return RedirectResponse(url='/')


async def stopCheatDetection(request):
    Controller.detectCheat = False
    return RedirectResponse(url='/')


class Echo(WebSocketEndpoint):
    encoding = "text"

    async def on_connect(self, websocket):
        await websocket.accept()

        # while True:
        #     while Controller.test:
        #         message = Controller.test.popleft()
        #         await websocket.send_text(f"Gamay kag: {message}")
        #         await asyncio.sleep(0.01)
        #     await asyncio.sleep(0.01)

    async def on_receive(self, websocket, data):
        Controller.title = data
        await websocket.send_text(f"Cheating detections are now titled: {data}")
