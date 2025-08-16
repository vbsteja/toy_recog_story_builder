 import  sys
from loguru import logger
from kivy.uix.scatter import Scatter
from kivy.uix.camera import Camera
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color

from game.core import Game
from screens.custom_widgets import SilverBackgroundWidget
from models.image_process import texture_to_numpy, ImageDetector



class GameScreen(Screen):
    message = StringProperty('Hello!')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        import sys
        layout = FloatLayout()
        #set the background color to silver
        self.background = SilverBackgroundWidget()
        layout.add_widget(self.background)
        scatter = Scatter(do_scale=False, do_translation=False, do_rotation=False)
        scatter.size_hint = (None, None)
        scatter.size = (600, 800)
        scatter.pos_hint = {'right': 1, 'y': 0}
        if sys.platform == 'darwin':
            scatter.rotation = 90
        camera = Camera(play=True, resolution=(640, 480))  # Reduced resolution for better performance
        camera.size_hint = (None, None)
        camera.size = (400, 300)  # Keep the view size the same
        # Mirror the camera feed by flipping  ,
        camera.canvas.before.clear()
        with camera.canvas.befor:
            from kivy.graphics import PushMatrix, Scale
            PushMatrix()
            Scale(x=-1, y=1, z=1, origin=camera.center)
        with camera.canvas.after:
            from kivy.graphics import PopMatrix
            PopMatrix()
        scatter.add_widget(camera)
        layout.add_widget(scatter)

        # Horizontal box for Start and Pause at bottom left
        button_box = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size_hint=(None, None),
            size=(640, 100),
            pos_hint={'center_x': 0.5, 'top': 1},
            padding=[10, 0, 10, 0]
        )
        start_btn = Button(text='Start', size_hint=(None, None), size=(200, 80),
                           on_press=self.on_start_click)
        pause_btn = Button(text='Pause', size_hint=(None, None), size=(200, 80),
                           on_press=self.on_pause_click)
        self.add_actor_btn = Button(text='Add Actor', size_hint=(None, None), size=(200, 80),
                                    disabled=True,
                                    on_press=self.on_add_actor_click)
        button_box.add_widget(start_btn)
        button_box.add_widget(pause_btn)
        button_box.add_widget(self.add_actor_btn)
        layout.add_widget(button_box)

        self.add_widget(layout)

        # # Detection variables
        self.last_detection = None
        self.detection_count = 0

        self.game = Game()

    def on_start_click(self, instance):
        ## schedule YOLO detection at 2 FPS (every 0.5 seconds)
        # Clock.schedule_interval(self.detect_objects, 0.5)
        logger.info('Game Started!')
        self.add_actor_btn.opacity = 1
        self.add_actor_btn.disabled = False

    def on_add_actor_click(self, instance):
        logger.info('Add Actor button clicked')
        Clock.schedule_interval(self.detect_objects, 0.5)

    def on_pause_click(self, instance):
        ## unschedule YOLO detection
        Clock.unschedule(self.detect_objects)
        self.add_actor_btn.opacity = 0
        self.add_actor_btn.disabled = True
        logger.info('Game Paused!')

    def detect_objects(self, dt):
        """ run object detection on the camera feed and update game state """
        img = self.get_camera_numpy()
        if img is not None:
            # Use the ImageDetector to detect objects in the image
            detector = ImageDetector()
            detection = detector.detect_objects(img)
            if detection:
                self.last_detection = detection
                self.detection_count += 1
                logger.info(f'Detected {len(detection)} objects: {self.last_detection}')
                if self.detection_count >= 5:
                    # Reset detection count after 5 detections
                    self.detection_count = 0
                    logger.info('Resetting detection count after 5 detections')

                # Update game state with detected objects

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
