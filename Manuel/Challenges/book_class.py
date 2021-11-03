class Booklist():
	    def __init__(self):
              self.books = []
		
	
def add(self, title, author):
	book = {}
book['title'] = title
book['author'] = authorself.books.append(book)
    		
		
def count_books(self,):
    		    return (len(self.books))
		

def remove_title(self, title):
		      for book in self.books:
    			      if book['title'] == title:
    					      self.book.remove(book)
def display_titles(self):
		      titles = []
		      for book in self.books:
    			      titles.append(book['title'])
	            titles.sort()
print(titles)


