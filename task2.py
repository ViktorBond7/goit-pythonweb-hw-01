from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int

    def __str__(self):
        return f"{self.title} by {self.author} {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title, author, year): ...
    @abstractmethod
    def remove_book(self, title): ...
    @abstractmethod
    def show_books(self): ...


class Library(LibraryInterface):
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, title, author, year):

        self.books.append(Book(title, author, int(year)))

    def remove_book(self, title):
        for book in self.books:

            if book.title == title:
                self.books.remove(book)
                break

    def show_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title, author, year):
        self.library.add_book(title, author, year)

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":

    main()
