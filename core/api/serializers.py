from rest_framework import serializers

from core.models import Blog


class BlogSerialazer(serializers.ModelSerializer):


    class Meta:
        model = Blog
        fields = (
            'title',
            'description',
            'image',
            'author',
            'slug',

        )



