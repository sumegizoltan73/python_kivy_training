
import os
os.environ['KIVY_NO_CONSOLELOG'] = '0'

cwd = os.getcwd()
os.environ['KIVY_HOME'] = cwd + "/conf"


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_file("kv-files/canvas-demo.kv")

class AlapWidget(FloatLayout):
    pass

class Teszt1App(App):
    def build(self):
        return AlapWidget()

Teszt1App().run()