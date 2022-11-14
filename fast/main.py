from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import base64
from crawling import Get_amedas_station


app = FastAPI()


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# NOTE: 1. python scraping.py
# NOTE: 2. python graph.py
# NOTE: 3. server起動 -> csvがある->画像がある -> 故に画像をbase64に変換してresponseできる

@app.get("/api")
async def graph():
            return Get_amedas_station.data_arange

@app.get("/api1")
def read_item():
    with open('./precipitation.png', 'rb') as imgFile:
        image = base64.b64encode(imgFile.read()).decode("utf-8")
        return { "path": ('data:image/jpeg;base64,' + image) }

@app.get("/api2")
def read_item():
    with open('./precipitation.png', 'rb') as imgFile:
        image = base64.b64encode(imgFile.read()).decode("utf-8")
        return { "path": ('data:image/jpeg;base64,' + image) }

@app.get("/api3")
def read_item():
    with open('./precipitation.png', 'rb') as imgFile:
        image = base64.b64encode(imgFile.read()).decode("utf-8")
        return { "path": ('data:image/jpeg;base64,' + image) }


@app.get("/api4")
def read_item():
    with open('./precipitation.png', 'rb') as imgFile:
        image = base64.b64encode(imgFile.read()).decode("utf-8")
        return { "path": ('data:image/jpeg;base64,' + image) }

@app.get("/api5")
def read_item():
    with open('./temp.png', 'rb') as imgFile:
        image = base64.b64encode(imgFile.read()).decode("utf-8")
        return { "path": ('data:image/jpeg;base64,' + image) }