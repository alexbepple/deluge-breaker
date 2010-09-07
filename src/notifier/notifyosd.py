import pynotify

def deluge_paused():
    show("We are safe from the Deluge for now.")

def deluge_resumed():
    show("The Deluge resumes.")

def show(message):
    pynotify.Notification("Deluge Breaker", message, "deluge").show()

