### add docstring here
"""
Webcam App using Kivy
"""


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.home_screen import  MainMenuScreen
from screens.game_screen import GameScreen
from screens.train_screen import TrainScreen

class WebcamApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='home'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(TrainScreen(name='train'))
        return sm

    def on_stop(self):
        pass

if __name__ == "__main__":
    WebcamApp().run()

