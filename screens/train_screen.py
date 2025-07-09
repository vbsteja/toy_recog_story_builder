# python
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TrainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        label = Label(
            text='Train Game AI',
            font_size=32,
            size_hint=(.6, .2),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        back_btn = Button(
            text='Back',
            size_hint=(.3, .1),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            on_press=self.go_back
        )

        layout.add_widget(label)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'home'