from django.http.response import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
import markdown
from django.conf import settings
from .serializers import DeviceSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Device

def apiHome(request):

    home_directory = settings.BASE_DIR
    
    with open(str(home_directory) +  '/README.md', 'r') as markdown_file:
        content = markdown_file.read()

        html_content = markdown.markdown(content)
        print(type(html_content))
    
        return HttpResponse(html_content)

# This response is stil returning JSON, it just has a nice Django framework wrapper that includes some other information and functionality
# return Response needs to be used in conjunction with the decorator @api_view

# Need to use this in conjuction with a serializer, this allows any Model object to be converted to JSON, which can then be returned via the API

@api_view(['GET'])
def apiOverview(request):
    json_data = {'Test1': 'Test1 Data'}
    return Response(json_data)

# List all devices or create a device

@api_view(['GET', 'POST'])
def deviceList(request):

    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)

    if request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data)

# List a specifc device or delete specific device

@api_view(['GET', 'DELETE'])
def deviceDetail(request, identifier):
    
    try:
        device = Device.objects.get(device_identifier=identifier)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    

