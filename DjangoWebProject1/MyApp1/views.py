from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello,MyApp1 Django")

from datetime import datetime

#def index(request):
#    now = datetime.now()

#    html_content = "<html><head><title>Hello, Django</title></head><body>"
#    html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#    html_content += "</body></html>"

#    return HttpResponse(html_content)

from django.shortcuts import render   # Added for this step

#def index(request):
#    now = datetime.now()

#    return render(
#        request,
#        "MyApp1/index.html",  # Relative path from the 'templates' folder to the template file
#        # "index.html", # Use this code for VS 2017 15.7 and earlier
#        {
#            'wfcontentwf': "<strong>Hello MyApp1 Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#        }
#    )

def index(request):
    now = datetime.now()

    return render(
        request,
        "MyApp1/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'wftitle' : "Hello Django",
            'wfmessage' : "hHello Django!",
            'wfcontentwf' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def howabout(request):
    return render(
        request,
        "MyApp1/about.html",
        {
            'wftitle' : "About HelloDjangoApp",
            'content' : "Example wf app page for Django."
        }
    )


# Create your views here.
