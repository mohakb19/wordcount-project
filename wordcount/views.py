from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'firstapp/b.html')

def next(request):
    t=request.GET['text']
    l=[]
    l=t.split()
    d={}
    for word in l:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    
    sw=sorted(d.items(), key=operator.itemgetter(1), reverse=True)
            
    return render(request,'firstapp/c.html',{'count':len(d),'sw':sw})
def ab(request):
    return HttpResponse("here we go to about")

