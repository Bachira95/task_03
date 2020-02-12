from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list":[{"restaurant_name":"Taemeh","food_type":"Flafel"},
    {"restaurant_name":"Mosselly","food_type":"Shawrma"},
    {"restaurant_name":"Jafra","food_type":"Breakfast"}
    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":{"restaurant_name":"Jafra", "food_type":"Breakfast"}

    }
    return render(request, 'detail.html', context)
