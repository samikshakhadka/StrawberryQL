# myapp/schema.py
import strawberry

@strawberry.type
class Book:
    id: int
    title: str
    author: str

@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> list[Book]:
        return [
            Book(id=1, title="1984", author="George Orwell"),
            Book(id=2, title="Brave New World", author="Aldous Huxley"),
            Book(id=3, title="Fahrenheit 451", author="Ray Bradbury"),
        ]

schema = strawberry.Schema(query=Query)
