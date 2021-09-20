
import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'

cwd = os.getcwd()
os.environ['KIVY_HOME'] = cwd + "/conf"


from kivy.app import App
from kivy.uix.label import Label

class TesztApp(App):
    def build(self):
        return Label(text="[color=ff0000]Hello[/color] [color=00ff00]world[/color]", font_size=60, italic=True,
                     underline=True, color=(0.7, 0.5, 0.2, 1), bold=True,
                     font_name='fonts/QuirkyRobot.ttf', markup=True)

TesztApp().run()