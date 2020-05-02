from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import jsonpickle
from json import JSONEncoder

from restappone.models import Car


def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')


def get_car(request, car_name):
    if request.method == 'GET':
        try:
            car = Car.objects.get(name=car_name)
            sampleSet = {'Car': car.name, 'Top Speed': car.top_speed}
            sampleJson = jsonpickle.encode(sampleSet)
            response = json.dumps([sampleJson])
        except:
            sampleSet1 = {'Error': 'No car with that name'}
            sampleJson1 = jsonpickle.encode(sampleSet1)
            response = json.dumps([sampleJson1])
    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def add_car(request):
    print(request)
    if request.method == 'POST':
        payload = json.loads(request.body)
        car_name = payload['car_name']
        top_speed = payload['top_speed']
        car = Car(name=car_name, top_speed = top_speed)
        try:
            car.save()
            sampleSet11 = {'Success', 'Car added successfully'}
            sampleJson11 = jsonpickle.encode(sampleSet11)
            response = json.dumps([sampleJson11])
        except:
            sampleSet12 = {'Error', 'Car could not be added'}
            sampleJson12 = jsonpickle.encode(sampleSet12)
            response = json.dumps([sampleJson12])
    return HttpResponse(response, content_type='text/json')





