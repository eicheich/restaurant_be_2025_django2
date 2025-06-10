import os
import uuid
from PIL import Image
from django.conf import settings


def save_image(image_file, directory='images/'):
    """
    Save an image file with a unique name

    Args:
        image_file: The uploaded image file
        directory: Directory to save the image (relative to MEDIA_ROOT)

    Returns:
        str: Path to the saved image (relative to MEDIA_ROOT)
    """
    # Generate unique filename
    ext = os.path.splitext(image_file.name)[1]
    filename = f"{uuid.uuid4()}{ext}"

    # Create the full directory path
    full_directory = os.path.join(settings.MEDIA_ROOT, directory)
    os.makedirs(full_directory, exist_ok=True)

    # Full path to save the image
    filepath = os.path.join(full_directory, filename)

    # Save the image
    with Image.open(image_file) as img:
        img.save(filepath)

    # Return the relative path
    return os.path.join(directory, filename)


def delete_image(image_path):
    """
    Delete an image file

    Args:
        image_path: Path to the image file (relative to MEDIA_ROOT)

    Returns:
        bool: True if deletion was successful, False otherwise
    """
    if not image_path:
        return False

    full_path = os.path.join(settings.MEDIA_ROOT, image_path)

    try:
        if os.path.exists(full_path):
            os.remove(full_path)
            return True
        return False
    except Exception:
        return False
