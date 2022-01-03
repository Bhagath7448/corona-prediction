from django.shortcuts import render
from django.http import JsonResponse
from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import ImageSerializer

import keras
from keras.models import * 
from keras.preprocessing import image

import numpy as np

# Create your views here.
@api_view(['GET'])
def list_api(request):
    return JsonResponse("Corona prediction API",safe=False)

@api_view(['POST'])
def corona_prediction(request):

    image_data = request.data
    
    print(image_data)
    
    serializer = ImageSerializer(data=image_data)

    if serializer.is_valid():  
        serializer.save()

    prediction_image = Image_to_Text.objects.all().last().image
    image_path = prediction_image.path

    print(image_path)

    model = load_model('model_covid.h5')

    img = image.load_img(image_path , target_size=(224,224))
    img = image.img_to_array(img)
    img = np.expand_dims(img,axis=0) 
    p = (model.predict(img) > 0.5).astype("int32")
    print('Positive' if p[0][0]==0 else 'negative')
    if p[0][0] == 0:
        prediction = "Positive"
    else:
        prediction = "Negative"

    return JsonResponse(prediction , safe=False)