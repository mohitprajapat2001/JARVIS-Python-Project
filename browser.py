import webbrowser
import json

link = open("links.json", "r")
obj = json.load(link)
def browseropen(task):
    for i in obj["links"]:
        print(i)
        if i in task:
            print(i)
            webbrowser.open(obj["links"][i])
            return f"Opening {i}"





