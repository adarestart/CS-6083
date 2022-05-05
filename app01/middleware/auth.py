from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path_info in ["/admin/login/", "/image/code/", "/admin/add/", "/user/individual/"]:
            return

        info_dict = request.session.get("info")
        # print(info_dict)
        if info_dict:
            return

        return redirect('/admin/login/')
