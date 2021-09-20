
import os
os.environ['KIVY_NO_CONSOLELOG'] = '0'

cwd = os.getcwd()
os.environ['KIVY_HOME'] = cwd + "/conf"


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

kv_string = """
<AlapWidget>:
    Button:
        text:"Gomb 1"
        size_hint:0.2, 0.5
        pos_hint:{"top":1}

    Button:
        text:"Gomb 2"
        size_hint:0.2, 0.5
        pos_hint:{"right":1, "top":1}
"""

#Builder.load_string(kv_string)
Builder.load_file("kv-files/simple-app.kv")

class AlapWidget(FloatLayout):
    pass

class Teszt1App(App):
    def build(self):
        return AlapWidget()

Teszt1App().run()