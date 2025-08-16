from kivy.graphics import Color, Rectangle
from kivy.properties import ListProperty
from kivy.uix.widget import Widget


# a color widget that creates a silver background, ususally used for the main menu screen
class SilverBackgroundWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update_background, size=self.update_background)

    def update_background(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.8, 0.8, 0.8, 1)  # Silver color
            Rectangle(pos=self.pos, size=self.size)


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
