#!/usr/bin/env python3

class Book:
    def __init__(self, title="outliers", page_count=123,):
        self.title = title
        self.page_count = page_count
        # self.turn_page = turn_page
        
    @property
    def title(self):
        "The name of the property"
        return self._title
    
    @title.setter
    def title(self,title):
        "title is required"
        if title is not None:
            self._title =title
        else:
            raise ValueError("Title is required and cannot be empty")   
    
    # pagecount
    @property
    def page_count(self):
        "Page property"
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
           print ("page_count must be an integer")
           
           
    def turn_page(self):
         print("Flipping the page...wow, you read fast!")
    pass
    
        