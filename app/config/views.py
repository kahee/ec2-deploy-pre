import mimetypes
import os
from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect


def serve_media(request, path):
    # path에는 미디어 파일 (User-uploaded files)의 경로가 주어짐
    # 주어진 미디어파일의 경로를 settings.MEDIA_ROOT를 기준으로해서
    # 해당 파일을 리턴해주는  view함수 작성
    media_math = os.path.join(settings.MEDIA_ROOT, path)
    content_type, encoding = mimetypes.guess_type(path)

    return FileResponse(open(media_math, 'rb'), content_type, )
