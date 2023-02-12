from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class BlockerUser(MiddlewareMixin):
    def process_request(self,request):
        print("user id and name", request.user.id, request.user.username)
        # if request.user.id == 1:
        #     return HttpResponse('You are blocked')