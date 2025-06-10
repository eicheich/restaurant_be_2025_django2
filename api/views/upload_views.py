from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from django.conf import settings
from uuid import uuid4


class ImageUploadView(APIView):
    """
    API endpoint for image uploads
    """
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        """
        Upload an image file
        """
        try:
            image_file = request.FILES.get('image')

            if not image_file:
                return Response(
                    {"error": "No image file provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Generate a unique filename with original extension
            file_extension = os.path.splitext(image_file.name)[1]
            unique_filename = f"{uuid4()}{file_extension}"

            # Determine the directory based on type parameter
            upload_type = request.data.get('type', 'general')
            if upload_type == 'menu':
                directory = 'images/menu/'
            elif upload_type == 'article':
                directory = 'images/articles/'
            else:
                directory = 'images/general/'

            # Create directory if it doesn't exist
            upload_dir = os.path.join(settings.MEDIA_ROOT, directory)
            os.makedirs(upload_dir, exist_ok=True)

            # Create the file path
            file_path = os.path.join(directory, unique_filename)
            full_path = os.path.join(settings.MEDIA_ROOT, file_path)

            # Save the file
            with open(full_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            # Create response with full URL to the image
            image_url = request.build_absolute_uri(
                f"{settings.MEDIA_URL}{file_path}"
            )

            return Response({
                "url": image_url,
                "path": file_path,
                "filename": unique_filename
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
