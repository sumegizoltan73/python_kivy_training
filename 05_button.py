
import os
os.environ['KIVY_NO_CONSOLELOG'] = '0'

cwd = os.getcwd()
os.environ['KIVY_HOME'] = cwd + "/conf"


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class AlapWidget(Widget):
    def __init__(self):
        super().__init__()
        gomb1 = Button(text="Gomb 1", size=(100, 50), pos=(0,0))
        gomb1.bind(on_press=self.hello_gomb)
        self.add_widget(gomb1)

        gomb2 = Button(text="Gomb 2", size=(100, 50), pos=(100, 100))
        gomb2.bind(on_press=self.hello_gomb)
        self.add_widget(gomb2)

    def hello_gomb(self, instance):
        if (instance.text == "Gomb 1"):
            print("Hello Gomb 1!")
        elif (instance.text == "Gomb 2"):
            print("Hello Gomb 2!")

class TesztApp(App):
    def build(self):
        return AlapWidget()

TesztApp().run()