books=[
    {"id":1,"title":"the Alchemist","author":"paulo Coelho","price":299},
    {"id":2,"title":"Atomic habits","author":"James clear","price":499}

    
]



def create_book(title,author,price):
    if not title or not author or not price:
        return {"error":"title, author and price are required "} 
    new_id=max([book["id"] for book in books] ,default=0)+1
    
    new_book={
        "id":new_id,
        "title":title,
        "author":author,
        "price":price
    }

    books.append(new_book)
    return new_book

print("adding a book")
print(create_book("the power of now","Eckhart Tolle",350))

print("final books list")
print(books)



def delete(book_id):
    for index,book in enumerate (books):
        if book["id"]==book_id:
            deleted_book=books.pop(index)
            return {"message": "deleted book" , "book": deleted_book}
        else:
            return {"error":f"book with id {book_id} not found"}
        
print("checking delete function")
print(delete(1))
print(books)
    