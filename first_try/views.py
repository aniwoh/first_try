from django.shortcuts import render

def fix_web(request):
    return render(request, 'errors/maintenance.html')

def bad_request400(request, exception):
    return render(request, 'errors/400.html', {'exception': exception}, status=400)


def permission_denied403(request, exception):
    return render(request, 'errors/403.html', {'exception': exception}, status=403)


def page_not_found404(request, exception):
    return render(request, 'errors/404.html', {'exception': exception}, status=404)

def page_not_found429(request, exception):
    return render(request, 'errors/429.html', {'exception': exception}, status=429)


def server_error500(request):
    return render(request, 'errors/500.html', status=500)


def server_error502(request, exception):
    return render(request, 'errors/502.html', {'exception': exception}, status=502)


def server_error503(request, exception):
    return render(request, 'errors/503.html', {'exception': exception}, status=503)


def server_error504(request, exception):
    return render(request, 'errors/504.html', {'exception': exception}, status=504)

def layer_view(request, page_name):
    return render(request, 'layer/'+page_name+'.html')