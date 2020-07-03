from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello,myAPP2 Django")

from datetime import datetime

from django.shortcuts import render   # Added for this step

def index(request):
    now = datetime.now()

    return render(
        request,
        "myAPP2/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'content': "<strong>Hello myAPP2 Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

# Create your views here.
