from rest_framework import serializers
from category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ('id', 'name','image_url','descriptions','cover_photo_url','resized_image_url','cover_video','tagline')
