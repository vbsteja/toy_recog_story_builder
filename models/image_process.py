import numpy as np
from kivy.graphics.texture import Texture

from ultralytics import YOLO

def texture_to_numpy(texture):
    """
    Convert a Kivy Texture to a numpy array (RGB).
    """
    if texture is None:
        return None
    size = texture.size
    pixels = texture.pixels  # RGBA
    img = np.frombuffer(pixels, dtype=np.uint8)
    img = img.reshape(size[1], size[0], 4)  # (height, width, 4)
    img = img[:, :, :3]  # Drop alpha channel
    return img

def numpy_to_texture(img):
    """
    Convert a numpy array (RGB) to a Kivy Texture.
    """
    if img is None:
        return None
    height, width, _ = img.shape
    texture = Texture.create(size=(width, height), colorfmt='rgb')
    texture.blit_buffer(img.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
    return texture


class ImageProcessor:
    """
    A class to handle image processing tasks.
    """

    @staticmethod
    def process_image(img):
        """
        Process the image (e.g., convert to grayscale).
        """
        if img is None:
            return None
        # Example processing: Convert to grayscale
        gray_img = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])  # Weighted sum for grayscale
        gray_img = gray_img.astype(np.uint8)
        return gray_img


class ImageDetector:
    """
    A class to handle image detection tasks.
    """

    @staticmethod
    def detect_objects(img):
        """
        Detect objects in the image (placeholder for actual detection logic).
        """
        if img is None:
            return []
        # Placeholder for object detection logic
        yolo = YOLO('yolov8n.pt')
        results = yolo(img)
        # Process results to extract detected objects
        detected_objects = []
        for result in results:
            for box in result.boxes:
                detected_objects.append({
                    'label': result.names[int(box.cls[0])],
                    'confidence': box.conf
                })
        # Return detected objects
        return detected_objects
        # Note: The actual detection logic will depend on the model and its output format
        # For now, just return a dummy list of detected objects
        # return [{'label': 'object1', 'confidence': 0.9}, {'label': 'object2', 'confidence': 0.8}]

    @staticmethod
    def get_top_class_name(results):
        """
        Get the top class name from detection results.
        results in the format of [{'label': 'object1', 'confidence': 0.9}, {'label': 'object2', 'confidence': 0.8}]
        """
        if not results:
            return None, 0.0
        # Sort results by confidence and get the top one
        top_result = max(results, key=lambda x: x['confidence'])
        return top_result['label'], top_result['confidence']