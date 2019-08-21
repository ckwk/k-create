import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

#Config.set('graphics', 'resizable', '0')

class WeaponPage(BoxLayout):
    def __init__(self, **kwargs):
        super(WeaponPage, self).__init__(**kwargs)
        self.orientation = 'vertical'


class KCreateApp(App):
    def build(self):
        return WeaponPage()


if __name__ == '__main__':
    KCreateApp().run()
