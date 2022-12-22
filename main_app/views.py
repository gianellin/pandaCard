from django.shortcuts import render

# added the import
from django.http import HttpResponse



##############################################
# THIS IS SIMULATING A MODEL, JUST FOR TODAY, 
# SO WE HAVE DATA TO INJECT INTO OUR TEMPLATES
class Panda:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description, diet, origin, weight, age):
    self.name = name
    self.type = type
    self.description = description
    self.diet = diet
    self.origin = origin
    self.weight = weight
    self.age = age
    

    

# This the array, we are injecting into the template
pandas = [
  Panda('Lola', 'giant panda', 'gentlest bears','herbivore', 'China','91 kg', 2),
  Panda ('Sachi', 'red panda', ' red hybrid fox', 'herbivore', 'China', '56 kg', 30),
  Panda('Loui', 'qinling panda', 'brown panda','herbivore', 'Bhutan','113 kg', 17)
]


# After this lesson this code will not be used
# because we'll use a REAL MODEL that can talk to 
# the DB
##############################################

# Create your views here.

def home (request):
    return render(request,'home.html')

def about (request):
    return render(request,'about.html')

def pandas_index (request):
    return render(request, 'pandas/index.html', { 'pandas': pandas })
