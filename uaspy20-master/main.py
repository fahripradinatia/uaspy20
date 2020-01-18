from data_model import *
from core.baseapp import BaseApp
from view.view_book import *
from view.input_book import *

class MainApp(BaseApp):
    def __init__(self):
        self.books = []

    def list_book(self):
        ViewBook.list(self)

    def add_book(self):
        InputBook.input(self)
        # InputBook.search(self)
    def search_book(self):
        InputBook.search(self)




if __name__ == "__main__":
    app = MainApp()
    app.run()

