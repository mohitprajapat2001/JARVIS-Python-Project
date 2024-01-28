from jarvis import listen, say
from browser import browseropen
import datetime, os
import wikipedia
from google import search

def mfx(fx):
    def ifx():
        say("Welcome Boss")
        fx()
        say("Thank you")
    return ifx()

@mfx
def main():
    print("Search on Internet\n"
          "Open on Browser\n"
          "Wikipedia\n"
          "Application\n"
          "Music\n"
          "Time")
    task = listen()
    if "browser" in task:
        result = browseropen(task)
        say(result)
    elif "time" in task:
        dt = datetime.datetime.now().strftime("%H Hours and %M Minutes")
        print(dt)
        say(f"Time is {dt}")
    elif "code" in task:
        os.startfile("C:/Users/Mohit Prajapat/AppData/Local/Programs/Microsoft VS Code/Code.exe")
    elif "music" in task:
        os.startfile("link.mp3")
    elif "wikipedia" in task:
        task = task.replace("wikipedia", "")
        result = wikipedia.summary(task, sentences=3)
        print(result)
        say(result)
    elif "search" in task:
        task = task.replace("search", "")
        result = search(task)
        print(result)
        say(result)



