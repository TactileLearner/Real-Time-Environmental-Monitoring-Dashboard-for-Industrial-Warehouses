from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

from .models import SensorReading
from .serializers import SensorReadingSerializer

# ✅ API View
class SensorDataAPIView(APIView):
    def post(self, request):
        serializer = SensorReadingSerializer(data=request.data)
        if serializer.is_valid():
            reading = serializer.save()

            # Send data to WebSocket group
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'sensor_data_group',
                {
                    'type': 'send_data',
                    'data': serializer.data
                }
            )

            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# ✅ Login View
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'monitor/login.html', {'form': {'errors': True}})
    return render(request, 'monitor/login.html', {'form': {}})

# ✅ Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# def dashboard(request):
#     data = SensorReading.objects.all().order_by('-timestamp')[:20]
#     return render(request, 'dashboard.html', {'data': data})    

# ✅ Protected Dashboard View
@login_required(login_url='login')
# def dashboard_view(request):
#     return render(request, 'monitor/dashboard.html')  # or whatever your template is


def dashboard_view(request):
    try:
        get_template('monitor/dashboard.html')  # this will raise an error if not found
    except TemplateDoesNotExist:
        raise
    return render(request, 'monitor/dashboard.html')    