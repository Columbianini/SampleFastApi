from pydantic import BaseModel
import datetime as dt
import time
import os


class Item(BaseModel):
    inventoryNode: str
    tradeNode: str
    date: dt.date
    addedTradePath: str | None

def generate_a_file_and_return_filename(item: Item)->str:
    file_name = f"{item.inventoryNode}_{item.tradeNode}_{dt.datetime.strftime(item.date, '%Y%m%d')}_{dt.datetime.strftime(dt.datetime.now(), '%Y%m%d_%H%M%S')}.txt"
    fp = os.path.join(r"C:\Users\Anthony\Desktop\FastApi\PostSample\output", file_name)
    result = []
    if item.addedTradePath is not None:
        if os.path.exists(item.addedTradePath):
            with open(rf'{item.addedTradePath}', "r") as f:
                result = f.readlines()
    
    time.sleep(5)

    with open(fp, "w") as f:
        f.write(file_name)
        for res in result:
            f.write(res)
    return fp


    

