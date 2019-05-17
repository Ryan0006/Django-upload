from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('__all__')

# class ImageListSerializer(serializers.Serializer) :
#     image = serializers.ListField(child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False ))
    
#     def create(self, validated_data):
#         image = validated_data.pop('image')
#         for img in image:
#             image_obj=Image.objects.create(image=img)
#         return photo