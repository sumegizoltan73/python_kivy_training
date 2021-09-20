
import os
os.environ['KIVY_NO_CONSOLELOG'] = '0'

cwd = os.getcwd()
os.environ['KIVY_HOME'] = cwd + "/conf"


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class AlapWidget(FloatLayout):
    pass

class TesztApp(App):
    def build(self):
        return AlapWidget()

TesztApp().run()