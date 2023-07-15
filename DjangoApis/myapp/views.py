from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MyModel
import json

def get_data(request):
    data = MyModel.objects.all().values()
    return JsonResponse(list(data), safe=False)

@csrf_exempt
def create_data(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        my_model = MyModel(field1=payload['field1'], field2=payload['field2'])
        my_model.save()
        return JsonResponse({'message': 'Data created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def update_data(request, id):
    if request.method == 'PUT':
        try:
            payload = json.loads(request.body)
            my_model = MyModel.objects.get(id=id)
            my_model.field1 = payload['field1']
            my_model.field2 = payload['field2']
            my_model.save()
            return JsonResponse({'message': 'Data updated successfully'})
        except MyModel.DoesNotExist:
            return JsonResponse({'error': 'Data not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def delete_data(request, id):
    if request.method == 'DELETE':
        try:
            my_model = MyModel.objects.get(id=id)
            my_model.delete()
            return JsonResponse({'message': 'Data deleted successfully'})
        except MyModel.DoesNotExist:
            return JsonResponse({'error': 'Data not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
