from selftools import deal_select
from django.shortcuts import render
from django.shortcuts import HttpResponse
from requests import put, get
from django.http import HttpResponseRedirect
def index(request):
    #return HttpResponse("hello world!");
    nlpwords = ""
    nlp_content = "这里就是数据啦"
    if request.method == "POST":
        nlpwords = request.POST.get("nlpwords");
        try:
            words=put('http://localhost:5050/todo1', data={'data': nlpwords}).json()
            #nlpwords = request.POST.get("nlpwords");
            nlp_content = nlpwords+':'+'\n'
            for i in range(0,9):
                nlp_content +=words[str(i)];
        except:
            print("process exception")
            nlp_content='输入异常'
    return render(request ,"main.html",{"nlpwords" : nlpwords,"nlp_content":nlp_content})
# Create your views here.
def index2(request):
    #return HttpResponse("hello world!");
    nlpwords = ""
    nlp_content = "这里就是数据啦"
    if request.method == "POST":
        nlpwords = request.POST.get("search_words");
        print(nlpwords)
        try:
            words=put('http://localhost:5050/todo1', data={'data': nlpwords}).json()
            #nlpwords = request.POST.get("nlpwords");
            nlp_content = nlpwords+':'+'\n'
            for i in range(0,9):
                nlp_content +=words[str(i)];
            print("页面跳转")
            return render(request ,"Select.html",{"select" : words[str(0)],"nlp_content":nlp_content})
        except:
            print("process exception")
            nlp_content='输入异常'
            return render(request ,"Select.html",{"select" : nlpwords,"nlp_content":nlp_content})
    return render(request ,"mstp_35_knowledge/index.html",{"search_words" : nlpwords})
# Create your views here.
def select(request):
    #return HttpResponse("hello world!");
    nlpwords = ""
    nlp_content = request.POST.get("nlp_content");
    if request.method == "POST":
        select = request.POST.get("select");
        try:
            return HttpResponseRedirect('http://www.bjguahao.gov.cn/dpt/hps/1,0,0,0,'+deal_select.deal(select)+'.htm')
        except:
            print("process exception")
            nlp_content='输入异常'
            #return render(request ,"select.html",{"select" : select,"nlp_content":nlp_content})
    return render(request ,"select.html",{"select" : nlpwords,"nlp_content":nlp_content})
# Create your views here.
