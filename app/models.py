class Articles:
    '''
    define news objects
    '''

    def __init__(self,d,name,author,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.name =name
        self.author =author
        self.title =title
        self.description =description
        self.url =url
        self.urlToImage =urlToImage
        self.publishedAt =publishedAt
class Source:
    '''
    define source
            '''
    def __init__(self, id, name, description, url, category, country,title):
        self.id = id
        self.name = name
        self.description = description  
        self.url = url
        self.category = category
        self.title =title
        self.country= country
