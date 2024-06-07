from django.shortcuts import render
import requests
import json
import main.main_query as main_query
from django.conf import settings


def index(request):
    return render(request, "main/index.html")


def home(request):
    return render(request, "main/index.html")


def ingredient(request):
    result = main_query.selectAllIngredients()
    return render(
        request,
        "main/ingredient.html",
        {"title": "fridge foraging", "ingredients": result},
    )


def recipe(request):
    result = main_query.selectAllIngredients()
    ingredientString = ",+".join(str(data["name"]) for data in result)
    ingredients = ingredientString

    url = (
        settings.API_DOMAIN
        + "/recipes/findByIngredients?ingredients="
        + ingredients
        + "&number=5"
        + "&apiKey="
        + settings.API_KEY
    )

    response = requests.get(url)
    data = json.loads(response.content)
    recipeIdList = []
    for i in data:
        recipeIdList.append(str(i["id"]))

    url = (
        settings.API_DOMAIN
        + "/recipes/informationBulk"
        + "?ids="
        + ",".join(recipeIdList)
        + "&number=5"
        + "&apiKey="
        + settings.API_KEY
    )

    response = requests.get(url)
    data2 = json.loads(response.content)
    for i in range(len(data2)):
        for key, value in data2[i].items():
            if type(value) is bool:
                data2[i][key] = str(value).lower() 
            if value is None:
                data2[i][key] = []
            if key == 'winePairing':
                data2[i][key] = []
        
    jsonString = json.dumps(data2)
    
    return render(
        request,
        "main/recipe.html",
        {"title": "Recipes", "name": "sowon", "recipes": data, "recipesDetail" : jsonString},
    )


def recipeDetail(request, id: int):
    url = (
        settings.API_DOMAIN
        + "/recipes/"
        + str(id)
        + "/information"
        + "?apiKey="
        + settings.API_KEY
    )
    response = requests.get(url)
    data = json.loads(response.content)
    return render(
        request,
        "main/recipeDetail.html",
        {"title": "Recipe", "recipeData": data},
    )


def category(request):
    cuisines = [
        "All",
        "African",
        "Asian",
        "American",
        "British",
        "Cajun",
        "Caribbean",
        "Chinese",
        "Eastern European",
        "European",
        "French",
        "German",
        "Greek",
        "Indian",
        "Irish",
        "Italian",
        "Japanese",
        "Jewish",
        "Korean",
        "Latin American",
        "Mediterranean",
        "Mexican",
        "Middle Eastern",
        "Nordic",
        "Southern",
        "Spanish",
        "Thai",
        "Vietnamese",
    ]
    diets = [
        "All",
        "Gluten Free",
        "Ketogenic",
        "Vegetarian",
        "Lacto-Vegetarian",
        "Ovo-Vegetarian",
        "Vegan",
        "Pescetarian",
        "Paleo",
        "Primal",
        "Low FODMAP",
        "Whole30",
    ]
    return render(
        request,
        "main/recipeCategory.html",
        {"title": "Recipe Category", "cuisines": cuisines, "diets": diets},
    )
