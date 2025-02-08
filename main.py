# main.py
from fastapi import FastAPI

app = FastAPI()
with open("data.json", "r") as f:
    data = json.load(f)

@app.get("/api")
async def api(name: list[str] = []):
    marks = []
    for n in name:
        found = False
        for item in data:
            if item['name'] == n:
                marks.append(item['marks'])
                found = True
                break
        if not found:
            marks.append(None)
    return {"marks": marks}
