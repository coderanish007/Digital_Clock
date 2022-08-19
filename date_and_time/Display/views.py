from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):

    date = str(datetime.now().date())
    time = str(datetime.now().time())

    html = f'''
    
    <html>
        <head>
            <meta http-equiv="refresh" content="10">
            <title>Clock</title>
            <style>
            </style>
        </head>
        <body style="background-color: smokewhite">
            <h1 style="text-align:center;
            text-color: white">
            Current Date and Time
            </h1>
            
            <div style="background-color: aqua;
            border: 2px solid black;
            height: 120px;
            width: 400px;
            margin: 50px 470px;
            align-items: center;
            box-shadow: 10px 10px 20px blue;">
            
                <h2 style="text-align:center" id="h1">Date: {date}</h2>
                <h2 style="text-align:center">Time: {time}</h2>
            </div>
        </body>
    </html>
    '''
    return HttpResponse(html)