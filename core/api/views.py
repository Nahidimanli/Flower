from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from core.models import Blog
from core.api.serializers import BlogSerialazer

class BlogAPIView(APIView):
    def get(self,request,*args,**kwargs):
        blog = Blog.objects.all()
        data = []
        # for blogs in blogs:
        #     data.append({
        #         'title': blog.title,
        #         'description' : blog.description,
        #         'image' : blog.image,
        #         'author' : blog.author,
        #         'slug' : blog.slug,
        #         })
        #return Response(data=data)    

        serializer = BlogSerialazer(blog, many=True)
        serializer = BlogSerialazer(blog, many = True,context={'request': request})
        return Response(data=serializer.data)


    def post (self, request, *args, **kwargs):
        serializer = BlogSerialazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    