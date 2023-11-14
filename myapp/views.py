from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def main(request):
    some = Post.objects.all()
    print(some)
    content = [
        {'title':'Falastin', 'id':'1001', 'sana':'14.11.23'},
        {'title':'Al-Aqso', 'id':'1002', 'sana':'10.11.23'},
        {'title':'Quddus', 'id':'1003', 'sana':'14.10.23'},
        {'title':'Gazo', 'id':'1004', 'sana':'14.11.23'},
        {'title':'Xamas', 'id':'1005', 'sana':'12.11.23'},
        {'title':'BAA', 'id':'1006', 'sana':'14.11.23'},
        {'title':'Embargo', 'id':'1007', 'sana':'14.11.23'},
        {'title':'Iroq', 'id':'1008', 'sana':'12.11.23'},
    ]
    return render(request, 'main.html', {'context':content})