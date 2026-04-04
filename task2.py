from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging
from typing import List

logging.basicConfig(
    format="%(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)


@dataclass
class Book:
    title: str
    author: str
    year: int

    def __str__(self) -> str:
        return f"{self.title} by {self.author} {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None: ...

    @abstractmethod
    def remove_book(self, title: str) -> None: ...

    @abstractmethod
    def get_books(self) -> List[Book]: ...


class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:

        self.books.append(book)

    def remove_book(self, title: str) -> None:
        for book in self.books:

            if book.title == title:
                self.books.remove(book)
                break

    def get_books(self) -> List[Book]:
        return self.books


class LibraryManager:

    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        for book in self.library.get_books():
            logging.info(
                f"Title: {book.title}, Author: {book.author}, Year: {book.year}"
            )


class LoggerLibrary(LibraryInterface):
    def __init__(self, wrapped: LibraryInterface):
        self.wrapped = wrapped

    def add_book(self, book: Book) -> None:
        logging.info(f"Adding book: {book}")
        self.wrapped.add_book(book)

    def remove_book(self, title: str) -> None:
        logging.info(f"Removing book with title: {title}")
        self.wrapped.remove_book(title)

    def get_books(self) -> List[Book]:
        logging.info("Getting list of books")
        return self.wrapped.get_books()


def main():
    library = Library()
    logger_library = LoggerLibrary(library)
    manager = LibraryManager(logger_library)

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
                logging.info("Invalid command. Please try again.")


if __name__ == "__main__":

    main()
