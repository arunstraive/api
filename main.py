from fastapi import FastAPI, HTTPException

app = FastAPI()

data = [{"name":"W7ftAQaJ","marks":38},{"name":"OjmLX","marks":84},{"name":"3p0lqaZ","marks":84},{"name":"8","marks":62},{"name":"C","marks":8},{"name":"UT8oTHElrV","marks":23},{"name":"2","marks":85},{"name":"SqPs","marks":34},{"name":"G0DS","marks":79},{"name":"FUfZi5MwFf","marks":71},{"name":"JeJB1jrGF","marks":22},{"name":"ei","marks":49},{"name":"nfFNm","marks":96},{"name":"2YbnmpGwkU","marks":81},{"name":"EsCTXblJ","marks":75},{"name":"LiMIF","marks":70},{"name":"zoX","marks":85},{"name":"jjY7rIfUG","marks":84},{"name":"00Xxaa","marks":70},{"name":"H","marks":99},{"name":"6PfKDtT","marks":81},{"name":"g","marks":50},{"name":"cX","marks":85},{"name":"dr2vf","marks":25},{"name":"swvfP","marks":96},{"name":"5Aech","marks":55},{"name":"aaivD8","marks":95},{"name":"Wyt","marks":29},{"name":"QL","marks":96},{"name":"nVaalC","marks":96},{"name":"Hg","marks":97},{"name":"Ve","marks":91},{"name":"qKB5R2","marks":14},{"name":"4m4lkhlsQ","marks":30},{"name":"G0Mw0","marks":43},{"name":"B","marks":59},{"name":"8r8n","marks":57},{"name":"gLRRTbe3Hc","marks":30},{"name":"MilAiZw1k","marks":35},{"name":"S1nxX","marks":54},{"name":"9KU6G","marks":59},{"name":"lpKvn1utK","marks":23},{"name":"AmDCFLpCUY","marks":44},{"name":"BIjcUp4ETS","marks":13},{"name":"Q7XqoK","marks":80},{"name":"18PNrvZk","marks":38},{"name":"qFI","marks":72},{"name":"HCW","marks":75},{"name":"uiHnldPBX6","marks":80},{"name":"V","marks":34},{"name":"TihMK","marks":16},{"name":"UmTU","marks":43},{"name":"K","marks":45},{"name":"sQwOYxHbVz","marks":53},{"name":"UfmCpes4A","marks":77},{"name":"Dx","marks":74},{"name":"nFl76dJ9B","marks":24},{"name":"Bebc2G","marks":42},{"name":"ksnO4QFUs","marks":37},{"name":"qFu7Tr","marks":64},{"name":"ogr","marks":50},{"name":"KW","marks":7},{"name":"sf4ZNq543i","marks":92},{"name":"KlPnA5a","marks":47},{"name":"UuWv","marks":97},{"name":"TjllUiwi","marks":12},{"name":"1tY2y","marks":64},{"name":"U8xFdys","marks":34},{"name":"30f5Y7i6I","marks":96},{"name":"hQMUwKqZY","marks":7},{"name":"GL5bkoF","marks":53},{"name":"R0D","marks":39},{"name":"BRYFr6Ff","marks":57},{"name":"D","marks":63},{"name":"aoi3","marks":28},{"name":"4NX","marks":79},{"name":"ioiteq","marks":50},{"name":"GudlSr","marks":33},{"name":"l6jsz","marks":86},{"name":"0DBarb","marks":70},{"name":"nYIJLGG","marks":81},{"name":"4hvMqBJy9","marks":74},{"name":"MFf6nqzA5v","marks":15},{"name":"FwkABY6","marks":76},{"name":"lM251J","marks":69},{"name":"B1g5Ce5o","marks":16},{"name":"MvPPLvv","marks":53},{"name":"LdV2VcJ","marks":49},{"name":"cxXGfCe9","marks":83},{"name":"OLEk","marks":48},{"name":"ZlgaT3CJ","marks":68},{"name":"YFMT","marks":37},{"name":"3r9k","marks":45},{"name":"ijqOhG4r","marks":63},{"name":"GYgbMG","marks":71},{"name":"at9Tl4ey","marks":45},{"name":"NG2LQ","marks":17},{"name":"mlg5","marks":63},{"name":"iKR","marks":84},{"name":"nIl","marks":21}]


@app.get("/api")
async def api(name: list[str] = []): # Use list[str] for type hinting and automatic parsing
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
    return {"marks": data}
