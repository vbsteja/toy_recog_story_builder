from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle, Color, InstructionGroup
from kivy.properties import ListProperty

class GradientWidget(Widget):
    gradient_colors = ListProperty([(0.2, 0.6, 1, 1), (0.8, 0.2, 0.8, 1)])  # Blue to purple

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update_gradient, size=self.update_gradient)

    def update_gradient(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            steps = 32
            for i in range(steps):
                t = i / float(steps - 1)
                r = self.gradient_colors[0][0] * (1 - t) + self.gradient_colors[1][0] * t
                g = self.gradient_colors[0][1] * (1 - t) + self.gradient_colors[1][1] * t
                b = self.gradient_colors[0][2] * (1 - t) + self.gradient_colors[1][2] * t
                a = self.gradient_colors[0][3] * (1 - t) + self.gradient_colors[1][3] * t
                Color(r, g, b, a)
                Rectangle(pos=(self.x, self.y + self.height * i / steps),
                          size=(self.width, self.height / steps))


class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gradient = GradientWidget()
        self.add_widget(self.gradient)

        layout = FloatLayout()
        button_box = BoxLayout(orientation='vertical',
                               spacing=30,
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
        button_box.add_widget(play_btn)
        button_box.add_widget(train_btn)
        layout.add_widget(button_box)
        self.add_widget(layout)

    def on_play(self, instance):
        self.manager.current = 'game'
    def on_train(self, instance):
        self.manager.current = 'train'
