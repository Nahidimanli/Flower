from rest_framework import serializers

from core.models import Blog, ContactUs
from baseuser.models import MyUser






class BlogSerialazer(serializers.ModelSerializer):
    #url = serializers.SerializerMethodField()


    class Meta:
        model = Blog
        fields = (
            "id",
            'title',
            'description',
            'image',
            'author',
            'slug',

        )


class Authorserialazer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'id'
            'bio',
            'image',
        )


class GETBlogSerialazer:
    author = Authorserialazer()


    class Meta:
        model = Blog
        fields = (
            "id",
            'title',
            'description',
            'image',
            'author',
        )



class POSTBlogSerialazer:
    author = Authorserialazer()


    class Meta:
        model = Blog
        fields = (
            "id",
            'title',
            'description',
            'image',
        )


class ContactUsSerializer(serializers.ModelSerializer):


    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'phone',
            'message',
        )



