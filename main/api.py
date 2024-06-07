from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import main.main_query as main_query
import json
import requests


@api_view(['PUT', 'POST', 'DELETE'])
def updateIngredient(request):
    if(request.method == "PUT"):
        data = json.loads(request.body)
        main_query.updateIngredient(data)
        return Response(status=status.HTTP_200_OK)
    
    if(request.method == "POST"):
        data = json.loads(request.body)
        url = "https://api.spoonacular.com/food/ingredients/search?query="+data['name']+"&number=1&apiKey=a4ea6fcc69ce4c48b9b8c97ef546607a"
        response = requests.get(url)
        data['imgUrl'] = "https://img.spoonacular.com/ingredients_100x100/"+json.loads(response.content)['results'][0]['image']
        main_query.createIngredient(data)
        return Response(status=status.HTTP_200_OK)
    
    if(request.method == "DELETE"):
        data = json.loads(request.body)['ingredientId']
        main_query.deleteIngredient(data)
        return Response(status=status.HTTP_200_OK)