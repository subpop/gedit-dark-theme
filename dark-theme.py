from gi.repository import GObject, Gedit, Gtk

class DarkThemePlugin(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "DarkThemePlugin"

    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        settings = Gtk.Settings.get_default()
        settings.set_long_property("gtk-application-prefer-dark-theme",1,"gedit:dark-theme")

    def do_deactivate(self):
        settings = Gtk.Settings.get_default()
        settings.set_long_property("gtk-application-prefer-dark-theme",0,"gedit:dark-theme")

    def do_update_state(self):
        pass
