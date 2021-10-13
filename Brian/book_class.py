class Booklist():
	def __init__(self):
		self.books = []

	def add(self, title, author):
		book = {}
		book['title'] = title
		book['author'] = author
		self.books.append(book)



	def count_books(self):
		return (len(self.books))

	def remove_title(self, title):
		book_list = []
		for book in self.books:
			if book['title'] == title:
				self.books.remove(book)

	def display_titles(self):
		alpha_list = []
		for book in self.books:
			alpha_list.append(book['title'])
			alpha_list.sort()
		return alpha_list
