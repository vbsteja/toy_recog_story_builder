import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2

class OpenCVImage(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.img_path = 'data/images.jpeg'  # Update with your image path
        Clock.schedule_interval(self.update_image, 1.0)  # 1 FPS

    def update_image(self, dt):
        frame = cv2.imread(self.img_path)
        if frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            buf = frame.tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
            self.texture = texture

class TestApp(App):
    def build(self):
        return OpenCVImage()

if __name__ == '__main__':
    TestApp().run()
# This code creates a simple Kivy application with a label and an image.
# Make sure to replace 'path/to/your/image.png' with a valid image path.
# The application will display "Hello, Kivy!" and the specified image.
# Ensure you have Kivy installed in your Python environment.
# You can install Kivy using pip:
# pip install kivy
# Ensure you have the necessary dependencies installed:
# pip install kivy[base] kivy[full] kivy[media]