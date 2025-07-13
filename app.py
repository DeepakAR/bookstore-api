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

#print("adding a book")
#print(create_book("the power of now","Eckhart Tolle",350))

#print("final books list")
#print(books)



def delete(book_id):
    for index,book in enumerate (books):
        if book["id"]==book_id:
            deleted_book=books.pop(index)
            return {"message": "deleted book" , "book": deleted_book}
        else:
            return {"error":f"book with id {book_id} not found"}
        
#print("checking delete function")
#print(delete(1))
#print(books)
    



def search_book(query):
    if not query:
        return {"error":"search query is empty"}
    query_lower=query.lower()
    results=[]

    for book in books:
        if query_lower in book["title"].lower() or query_lower in book["author"].lower():
            results.append(book)
        
    if not results:
        return {'error':f"no book found matching {query}"}
    return results

#print("checking search fucntion")
#print(search_book("Atomic habits"))
#print(books)

def update_book(book_id,updated_data):
    for book in books:
        if book["id"]==book_id:
            for key in updated_data:
                if key in book:
                    book[key]=updated_data[key]
            return {"message":"Book updated","book":book}
    return {"error":"book not found"}

print(update_book(1,{"title":"updated book","price":249}))
print(books)