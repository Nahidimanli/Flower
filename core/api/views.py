from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from core.models import Blog
#from core.api.serializers import BlogSerialaizer

class BlogAPIView(APIView):
    def get(self,request,*args,**kwargs):
        blog = Blog.objects.all()
        data = []
        for blogs in blogs:
            data.append({
                'title': blog.title,
                'description' : blog.description,
                'image' : blog.image,
                'author' : blog.author,
                'slug' : blog.slug,
                })
        return Response(data=data)    