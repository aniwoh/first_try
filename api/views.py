from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse

def proxy_get_index_photo(request):
    # 构建API请求的URL，要求该api返回的结果是一个图片
    api_url = "https://t.mwm.moe/pc"
    response = requests.get(api_url)
    # 检查请求是否成功
    if response.status_code == 200:
        image_data = response.content
        response = HttpResponse(image_data, content_type="image/jpeg")
        response['Content-Disposition'] = 'attachment; filename="random_image.jpg"'
        return response
    else:
        return JsonResponse({'error': 'API request failed'}, status=500)
