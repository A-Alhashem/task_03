from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list": [
    		{
    			"restaurant": "chilis",
    			"food": "mexican",
    		},
    		{
    			"restaurant": "lorenzo",
    			"food": "italian",
    		},
    		{
    			"restaurant": "osaka",
    			"food": "japanese",
    		},
    	],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object": {
    		"restaurant": "meat_co",
    		"food": "steak",
    	},
    }
    return render(request, 'detail.html', context)
