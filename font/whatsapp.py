#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, Gdk, GLib, GObject, WebKit2

window = Gtk.Window()
window.set_title("Whatsapp for Linux")
window.set_icon_from_file("/usr/local/bin/whatsapp/icons/whatsapp.ico")
window.set_size_request(800, 400)
window.connect('delete-event', Gtk.main_quit)

webview = WebKit2.WebView.new()

with open("/usr/local/bin/whatsapp/static/whatsapp.html", "rb") as code_html:
    arquivo = code_html.read()
webview.load_html('''<html>
        <body>
        <h1>Whatsapp Web</h1>
        <p>{}</p>
        </body></html>'''.format(arquivo.decode("utf8")))

window.add(webview)
window.show()
window.show_all()

if __name__=='__main__':
    Gtk.main()
