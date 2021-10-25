class Booklist():
	def __init__(self):
		 self.books = []

	def add(self, title, author):
		book = {}
		book['title'] = title # adds the key in the key-value of dictionary 'book'
		book['author'] = author # adds the value in the key-value of the dict. 'books'
		self.books.append(book)

	def count_books(self):
		len(self.books)# counts the elements in the list 'self.books'

	def remove_title(self, title):
		for book in self.books:
			if book['title'] == title:
				self.books.remove(book) # deletes an element from the array self.books

	def display_titles(self):
		titles = []
		for book in self.books:
			titles.append(book['title']) # adds an element to the array 'titles'
		titles.sort() # sorts the list 'titles' alphabetically
		print(titles)