from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from core.models import Blog
from core.api.serializers import BlogSerialazer

class BlogAPIView(APIView):
    def get(self,request,*args,**kwargs):
        blog = Blog.objects.all()
        #data = []
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



class BlogDetailAPIView(APIView):
    def get(self, request, id, *args, **kwargs):

        try:
            blog = Blog.objects.get(id=id)
            #blog = Blog.objects.filter(id=id).first()
            serialazer = BlogSerialazer(blog)
            return Response(data=serialazer.data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response({'error': 'id is not invalid'}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, *args, **kwargs):
        blog = Blog.objects.filter(id=kwargs['id']).first()
        if not blog:
            return Response({'error': 'id is not requried'}, status=status.HTTP_400_BAD_REQUEST)
        serialazer = BlogSerialazer(data=request.data, instance=blog, partial=True)
        serialazer.is_valid(raise_exception=True)
        serialazer.save()
        return Response(serialazer.data, status=status.HTTP_200_OK)


    def delete(self, request, *args, **kwargs):
        blog = Blog.objects.filter(id=kwargs['id']).first()
        if not blog:
            return Response({'error': 'id is not requried'}, status=status.HTTP_400_BAD_REQUEST)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
