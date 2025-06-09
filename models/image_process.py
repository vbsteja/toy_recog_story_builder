import numpy as np

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

