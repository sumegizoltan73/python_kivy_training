
import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'

cwd = os.getcwd()
os.environ['KIVY_HOME'] = cwd + "/conf"

from kivy.config import Config
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
Config.set('graphics', 'resizable', '0')




from kivy.app import App
from kivy.uix.widget import Widget

class TesztApp(App):
    def build(self):
        return Widget()

TesztApp().run()