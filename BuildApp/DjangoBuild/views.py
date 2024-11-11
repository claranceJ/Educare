from django.shortcuts import render

# # Create your views here.
# from DjangoBuild import views
    
    
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about-us.html')
def contact(request):
    return render(request, 'contact.html')
def courseDetails(request):
    return render(request, 'course-details.html')
def courses(request):
    return render(request, 'courses.html')
def elements(request):
    return render(request, 'elements.html')
def singleBlog(request):
    return render(request, 'single-blog.html')

def courses(request):
    return render(request, 'courses.html')
