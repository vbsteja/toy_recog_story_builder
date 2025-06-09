from kivy.uix.scatter import Scatter
from kivy.uix.camera import Camera
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from models.image_process import texture_to_numpy

class HomeScreen(Screen):
    message = StringProperty('Hello!')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        scatter = Scatter(do_scale=False, do_translation=False, do_rotation=False)
        scatter.size_hint = (None, None)
        scatter.size = (600, 800)
        scatter.pos_hint = {'right': 1, 'y': 0}
        scatter.rotation = 90
        camera = Camera(play=True, resolution=(1600, 1200))
        camera.size_hint = (None, None)
        camera.size = (800, 600)
        # Mirror the camera feed by flipping horizontally
        camera.canvas.before.clear()
        with camera.canvas.before:
            from kivy.graphics import PushMatrix, Scale
            PushMatrix()
            Scale(x=-1, y=1, z=1, origin=camera.center)
        with camera.canvas.after:
            from kivy.graphics import PopMatrix
            PopMatrix()
        scatter.add_widget(camera)
        layout.add_widget(scatter)
        self.add_widget(layout)

    def on_button_click(self):
        self.message = 'Button Clicked!'

    def get_camera_numpy(self):
        # Access the camera widget
        camera = None
        for child in self.walk():
            if isinstance(child, Camera):
                camera = child
                break
        if camera and camera.texture:
            return texture_to_numpy(camera.texture)
        return None
