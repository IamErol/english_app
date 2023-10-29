from PIL import Image

class ImageResizer:
    """Resize image."""

    SIZE_CHOICES  = {
        "1600x1338": (1600, 1338),
        "1366x768": (1366, 768),
        "1024x768": (1024, 768),
        "800x480": (800, 480),
        "480x320": (480, 320),
    }

    def __init__(self, image):
        self.image = image

    def resize(self, width=None, height=None, size_choice=None):
        if size_choice:
            if size_choice in self.SIZE_CHOICES:
                width, height = self.SIZE_CHOICES[size_choice]
            else:
                raise ValueError("Invalid size choice")

        resized_image = Image.open(self.image)
        resized_image = resized_image.size(width, height)
        return resized_image
