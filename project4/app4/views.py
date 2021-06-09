from django.shortcuts import render
from django.http import HttpResponse

def showIndex(request):
    message = '''<html>
                   <body bgcolor="yellow">
                      <h1><font size='8' font color='red' face='chiller'> "Hello World, This is Django Class" 
                      </font>  
                      </h1>                    
      </body>
    </html>
    
    '''
    return HttpResponse(message)