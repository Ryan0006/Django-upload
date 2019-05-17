from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ImageSerializer
from .models import Image

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser,)

    # def post(self, request, *args, **kwargs):
    #     image_serializer = ImageSerializer(data=request.data)
    #     if image_serializer.is_valid():
    #         image_serializer.save()
    #         return Response(image_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        for image in request.data.getlist('image'):
            try:
                Image.objects.create(image=image)
            except:
                return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("ok", status=status.HTTP_201_CREATED)


