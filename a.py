import json


a = {1: "1", 2: "2", 3: "3"}

with open("a.json", "w") as f:
    json.dump(a, f)

    f.write()


