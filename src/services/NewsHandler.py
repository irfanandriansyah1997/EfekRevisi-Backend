from generated.efekRevisi.ThriftServices.news import NewsService
from generated.efekRevisi.ThriftServices.news.ttypes import News, NewsList


class NewsHandler:
    def __init__(self):
        self.log = {}
        self.news = [
            {
                'newsID': 1,
                'title': 'Machine Learning for Anyone who Took Math in 8th Grade',
                'thumbnail': 'https://cdn-images-1.medium.com/focal/198/203/47/44/1*4MPrAZ3izcEH7o8FGj3YaQ.jpeg',
                'date': 'Feb 6',
                'description': 'Set aside all the complexity, and what’s left is a simple algebraic formula'
            },
            {
                'newsID': 2,
                'title': 'How to Create a Sketch Style Guide, Library, and UI Kit',
                'thumbnail': 'https://cdn-images-1.medium.com/fit/c/198/203/1*XcAspFE17o2WUYIm4IRngg.png',
                'date': 'Feb 17',
                'description': """Sketch is a valuable, time-saving resource. Using it to create style guides can 
                    make it even more of a time-saver."""
            },
            {
                'newsID': 3,
                'title': 'Muscle Mentor — Injury Prevention App: UX Case Study',
                'thumbnail': 'https://cdn-images-1.medium.com/fit/c/198/203/1*jTJ3zefnyknfa1WbVEvQcA.jpeg',
                'date': 'Mar 14',
                'description': """I’ve noticed a lot of confusion in the industry about various software 
                    roles and titles, even among founders, hiring managers, and team…"""
            }
        ]

    def getNews(self):
        return NewsList(list(map(lambda x: News(**x), self.news)))


handler = NewsHandler()
processor = NewsService.Processor(handler)

