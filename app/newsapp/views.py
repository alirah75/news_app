from django.shortcuts import render
from django.views import View
from newsapi import NewsApiClient

# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        newsapi = NewsApiClient(api_key='4244c042b00d4dddb2261691a3bd2ebc')
        top = newsapi.get_top_headlines(sources='techcrunch')

        l = top['articles']
        desc = []
        news = []
        img = []

        for i in range(len(l)):
            f = l[i]
            news.append(f['title'])
            desc.append(f['description'])
            img.append(f['urlToImage'])
        mylist = zip(news, desc, img)
        return render(request, 'newsapp/index.html', context={"mylist": mylist})



