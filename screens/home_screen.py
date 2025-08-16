from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle, Color, InstructionGroup
from kivy.properties import ListProperty

from screens.custom_widgets import SilverBackgroundWidget





class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #add a silver background widget
        self.background = SilverBackgroundWidget()
        self.add_widget(self.background)

        layout = FloatLayout()
        # Text label at the top that says "welcome to Kidsy!"
        text_label = Label(text='Welcome to Kidsy!',
                           # size_hint=(.8, .2),
                           # pos_hint={'center_x': 0.5, 'top': 0.9},
                           font_size=36,
                           # font_name='fonts/RobotoMono-Regular.ttf',
                           color=(0, 0, 0, 1))
        button_box = BoxLayout(orientation='horizontal',
                               spacing=10,
                               size_hint=(.5, .4),
                               pos_hint={'center_x': 0.5, 'center_y': 0.5})
        play_btn = Button(
            text='Play Game',
            size_hint=(1, None),
            height=60,
            background_normal='',
            background_color=(0.1, 0.7, 0.4, 1),
            color=(1, 1, 1, 1),
            font_size=24,
            border=(20, 20, 20, 20),
            on_press = self.on_play
        )
        train_btn = Button(
            text='Train Game AI',
            size_hint=(1, None),
            height=60,
            background_normal='',
            background_color=(0.9, 0.5, 0.2, 1),
            color=(1, 1, 1, 1),
            font_size=24,
            border=(20, 20, 20, 20),
            on_press= self.on_train
        )
        layout.add_widget(text_label)
        button_box.add_widget(play_btn)
        button_box.add_widget(train_btn)
        layout.add_widget(button_box)
        self.add_widget(layout)

    def on_play(self, instance):
        self.manager.current = 'game'
    def on_train(self, instance):
        self.manager.current = 'train'
