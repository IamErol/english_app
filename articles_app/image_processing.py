import os
from PIL import Image
from PIL.Image import NEAREST
from io import BytesIO
from django.core.files.base import ContentFile

image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
                }

def image_resize(image, instance):
    original_image = Image.open(image)
    sizes = [(1600, 1200), (1366, 768), (1024, 768), (800, 480), (480, 320)]
    image_name, extention = os.path.splitext(image.name)
    for size in sizes:
        if original_image.mode == 'RGBA':
            original_image.convert('RGB')
        img = original_image.copy()
        img = img.resize(size, NEAREST)

        image_field_name = f"image_{size[0]}_{size[1]}"
        image_field = getattr(instance, image_field_name)
        ext = original_image.format
        if original_image.format == 'JPEG':
            output = BytesIO()
            img.save(output, format='JPEG', quality=95)
            image_field.save(f'{image_name}/image_{size[0]}_{size[1]}.jpg', ContentFile(output.getvalue()), save=False)
        elif original_image.format == 'PNG':
            output = BytesIO()
            img.save(output, format='PNG')
            image_field.save(f'{image_name}/image_{size[0]}_{size[1]}.png', ContentFile(output.getvalue()), save=False)






