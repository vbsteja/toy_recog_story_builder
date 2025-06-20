### add docstring here
"""
Webcam App using Kivy
"""


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.home_screen import HomeScreen


class WebcamApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        return sm

    def on_stop(self):
        pass

if __name__ == "__main__":
    WebcamApp().run()

