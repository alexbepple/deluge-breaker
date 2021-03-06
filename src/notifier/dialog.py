import pygtk
import gtk

def deluge_paused():
    show("We are safe from the Deluge for now.")

def deluge_resumed():
    show("The Deluge resumes.")

def show(message):
    dialog = gtk.MessageDialog(buttons=gtk.BUTTONS_OK)
    dialog.set_title("Deluge Breaker")
    dialog.set_markup(message)

    theme = gtk.icon_theme_get_default()
    icon = theme.load_icon("deluge", 16, 0)
    dialog.set_icon(icon)

    dialog.run()
    dialog.destroy()

