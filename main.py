from fastapi import FastAPI
from model import Item, generate_a_file_and_return_filename


app = FastAPI()


@app.post("/items")
async def create_item(item: Item):
    return generate_a_file_and_return_filename(item)