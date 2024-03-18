#! /usr/bin/env python3
"""
client.py
program for CURD MongoDB
Management database search update delete
brr..
"""

import sys
# This is needed to prevent creation of the accursed
# '__cache__' directory that we do not want
sys.dont_write_bytecode=True
import pymongo
import u1 as ui
from metadata import *
from GridFS import *

def display_download_paged(*, client, session, db, books_per_page=5):
    """
    Display Delete in a paged format.
    """
    books_collection = db.get_collection(name="books")
    total_books = books_collection.count_documents({})

    page = 1
    while True:
        print("\n")
        start_index = (page - 1) * books_per_page
        end_index = start_index + books_per_page
        books = list(books_collection.find({}, {"_id": 1, "title": 1, "author": 1}).skip(start_index).limit(books_per_page))
        print(f"\n{'Download Books Menu':^70s}\n")
        print(f"[ Page {page}/{(total_books + books_per_page - 1) // books_per_page} ]:")
        for book in books:
            authors = ", ".join([author["name"] for author in book.get("author", [{"name": ""}])])
            print(f"_id = {book['_id']}: {book.get('title', '')} by {authors}")

        print(f"navigate menu")
        print("1. Next page")
        print("2. Previous page")
        print("3. Select book by ID")
        print("4. Return to main menu")
        print("-"*70)
        choice = input("Enter choice: ")

        if choice == '1':
            page += 1
        elif choice == '2':
            if page > 1:
                page -= 1
            else:
                print("You are on the first page.")
        elif choice == '3' :
            book_id = input("Enter the _id of the book to select: ")
            books_collection = db.get_collection(name="books")
            book = books_collection.find_one({"_id": int(book_id)})
            if book == None:
                print("\nMessage:")
                print("Book with _id '{book_id}' not found")
                print("\n")
            else:
                # print(book["file_name"])
                # print(book["file_id"])
                # print(book["file_type"])
                while True:
                    dchoice = input("download?(y/n) : ")
                    if dchoice.lower() == 'y' :
                        fileoutput(db=db, session=session, fname=book['file_name'], fid=book['file_id'], ftype=book['file_type'])
                        print("Load Book Success !")
                        break
                    elif dchoice.lower() == 'n':
                        print("OK;3")
                        break
                    else:
                        print("invalid input,  Please enter 'Y' or 'N'.")
           
        elif choice == '4':
            break
        else:
            print("Invalid choice") 


def download_book(*, client, session, db):
    try:
        display_download_paged(client=client, session=session, db=db, books_per_page=5)
    except KeyboardInterrupt as e:
        print("User Exit Feature with Ctrl-C!!")
        
def string_id(tid):
    """ return the value of _id as a string """
    if isinstance(tid,int):
        return f"{tid:d}"
    return f"{str(tid):s}"
    
"""catagory part"""     
def add_category(*,client,session,db):
    print("\n")
    print(f"\n{'Add Category':^70s}\n")
    """ add a new category """
    try:
        categoryname = ui.get_string(minlength=4,maxlength=50, pattern=r"^([A-Za-z&' ]+)$",
                                prompt="Enter Category Name:")
        categories_collection = db.get_collection(name="categories")
        last_book = categories_collection.find_one(sort=[('_id', -1)])  # Get the last document to get the last _id
        last_id = last_book['_id'] if last_book else 0  # If no last document, start from 0
        new_id = last_id + 1  # Increment the last _id to continue the sequence
        try:
            rezult = categories_collection.insert_one({"_id": new_id, "name": categoryname})
        except pymongo.errors.DuplicateKeyError as xcpn:
            print(f"Error: Category '{categoryname:s}' already exists.", file=sys.stderr)
            return
        except pymongo.errors.WriteError as xcpn:
            if xcpn.details['errmsg'] == 'Document failed validation':
                print(f"Invalid category name '{categoryname:s}'!", file=sys.stderr)
            else:
                print(xcpn.details['errmsg'], file=sys.stderr)
            return
        print(f"Category '{categoryname:s}' added successfully")
    except KeyboardInterrupt as e:
        print("User Exit Feature with Ctrl-C!!")

# def rename_category(*,client,session,db):
#     """ rename an existing category """
#     cat_id = choose_category(client=client,session=session,db=db)
#     if cat_id[0] is None:
#         print("No category selected to rename")
#         return
#     newcatname = ui.get_string(minlength=4,maxlength=50,
#                                prompt="Enter Category Name:")
#     if cat_id[0] == newcatname:
#         print(f"Could not rename category: old name '{cat_id[0]:s}' matches new name '{newcatname:s}'")
#         return
#     categories_collection = db.get_collection(name="categories")
#     try:
#         rezult = categories_collection.update_one({"_id":cat_id[1]},{"$set": {"name": newcatname}})
#     except pymongo.errors.DuplicateKeyError as xcpn:
#         print(f"Error: Category '{newcatname:s}' already exists.", file=sys.stderr)
#         return
#     except pymongo.errors.WriteError as xcpn:
#         if xcpn.details['errmsg'] == 'Document failed validation':
#             print(f"Invalid new category name '{newcatname:s}'!", file=sys.stderr)
#         else:
#             print(xcpn.details['errmsg'], file=sys.stderr)
#         return
#     if ((rezult.raw_result['n'] != 1) or
#         (rezult.raw_result['ok'] != 1.0) or
#         (not rezult.raw_result['updatedExisting'])):
#         print(f"Could not rename category '{cat_id[0]:s}' (_id={string_id(cat_id[1]):s}")
#         return
#     print(f"Category '{cat_id[0]:s}' renamed to '{newcatname:s}' successfully")

def dump_categories(*,client,session,db):
    try:
        """ Display all the documents in the categories collection 
            {'_id': 0, 'name': 'Horror/Ghosts'}
        """
        categories_collection = db.get_collection(name="categories")
        # for document in categories_collection.find({},{"_id":1, "name":1}):
            # print(f" _id =  {string_id(document['_id']):s}")
            # print(f"name = '{document['name']:s}'")
        display_categories_paged(client=client, session=session, db=db)
    except KeyboardInterrupt as e:
        print("User Exit Feature with Ctrl-C!!")

"""authors part"""  

def dump_authors(*,client,session,db):
    """ Display all the documents in the authors collection 
    """
    authors_collection = db.get_collection(name="authors")
    # for document in authors_collection.find({}, {"_id": 1, "name": 1, "birthdate": 1, "books": 1}):
        # book_titles = ", ".join([book["title"] for book in document.get("books", [])])
        # print(f"_id = {document['_id']:d}, name = '{document['name']:s}', birthdate = '{document['birthdate']:s}', books = '{book_titles}'")
    display_authors_paged(client=client, session=session, db=db)
def pretty_dump_authors(*,client,session,db):
    try:
        print(f"\n{'Authors Menu':^70s}\n")
        dump_authors(client=client,session=session,db=db)
    except KeyboardInterrupt as e:
        print("User Exit Feature with Ctrl-C!!")

"""books part""" 

def add_books(*, client, session, db):
    """ Add a new book """
    print("\n")
    print(f"\n{'Add Book':^70s}\n")
    try:
        new_book_title = ui.get_string(minlength=4, maxlength=100, pattern=r"^([A-Za-z0-9&-;:,.()/' ]+)$", prompt="Enter Book Title: ")
        new_book_author_name = ui.get_string(minlength=4, maxlength=100, pattern=r'^[A-Za-z\s\.\',-]+$', prompt="Enter Author Name: ")
        new_book_language = ui.get_string(minlength=2, maxlength=50, pattern=r'^[A-Za-z\s\.\',-]+$', prompt="Enter Language: ")
        new_book_publish_date = ui.get_string(minlength=10, maxlength=50, pattern=r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", prompt="Enter Publish Date (1990-12-01): ")
        new_book_genre = ui.get_string(minlength=4, maxlength=50, pattern=r'^[A-Za-z\s\.\',-]+$', prompt="Enter Genre: ")
        new_book_file_path = ui.get_string(minlength=4, maxlength=200, pattern=r'^\./.*\.(epub|pdf)$', prompt="Enter File Path (./NOSQL.epub): ")
        new_book_file_name = ui.get_string(minlength=4, maxlength=200, pattern=None, prompt="Enter File Name: ")
        new_book_ISBN = ui.get_string(minlength=10, maxlength=13, pattern=None, prompt="Enter ISBN (9876543210102): ")

        books_collection = db.get_collection(name="books")
        last_book = books_collection.find_one(sort=[('_id', -1)])  # Get the last document to get the last _id
        last_id = last_book['_id'] if last_book else 0  # If no last document, start from 0

        new_id = last_id + 1  # Increment the last _id to continue the sequence
        new_book = {
            "_id": new_id,
            "title": new_book_title,
            "author": [{"name": new_book_author_name}],
            "language": new_book_language,
            "publish_date": new_book_publish_date,
            "genre": [new_book_genre],
            "file_path": new_book_file_path,
            "file_name": new_book_file_name,
            "ISBN": new_book_ISBN
        }

        try:
            # result = books_collection.insert_one(new_book)
            file_id, file_type = fileinput(db=db, session=session, fname=new_book['file_name'], fpath=new_book['file_path'])
            if file_id and file_type:
                new_book["file_id"] = file_id
                new_book["file_type"] = file_type
                books_collection.insert_one(new_book, session=session)
            
            print(f"\nBook '{new_book_title:s}' added successfully with _id {new_id}")
            print("*"*30)
        except Exception as e:
            print(f"Error adding book: {e}", file=sys.stderr)
    except KeyboardInterrupt as e:
        print("User Exit Feature with Ctrl-C!!")

def delete_books(*, client, session, db):
    """ Delete an existing book """
    try:
        display_delete_paged(client=client, session=session, db=db, books_per_page=5)
    except KeyboardInterrupt as e:
        print("User Exit Feature with Ctrl-C!!")

def dump_books(*,client,session,db):
    """ Display all the documents in the authors collection 
    """
    books_collection = db.get_collection(name="books")
    # for document in books_collection.find({}, {"_id": 1, "title": 1, "author": 1, "genre": 1}):
        # author_data = document.get("author", [{"name": ""}])
        # author = author_data[0].get("name", "") if author_data else ""
        # genre = "".join(document.get("genre", []))
        # tag = "".join(document.get("tag", []))
        # language = document.get("language", "")
        # print(f"_id = {document['_id']:d}, title = '{document.get('title', '')}', author = '{author}', genre = '{genre}'")
    display_books_paged(client=client, session=session, db=db)
    #select_book_by_id(client=client, session=session, db=db)
    
def pretty_dump_books(*,client,session,db):
    try:
        dump_books(client=client,session=session,db=db)
        print()
    except KeyboardInterrupt as e:
        print("User Exit Feature with Ctrl-C!!")

def display_delete_paged(*, client, session, db, books_per_page=5):
    """
    Display Delete in a paged format.
    """
    books_collection = db.get_collection(name="books")
    total_books = books_collection.count_documents({})

    page = 1
    while True:
        print("\n")
        start_index = (page - 1) * books_per_page
        end_index = start_index + books_per_page
        books = list(books_collection.find({}, {"_id": 1, "title": 1, "author": 1}).skip(start_index).limit(books_per_page))
        print(f"\n{'Delete Books Menu':^70s}\n")
        print(f"[ Page {page}/{(total_books + books_per_page - 1) // books_per_page} ]:")
        for book in books:
            authors = ", ".join([author["name"] for author in book.get("author", [{"name": ""}])])
            print(f"_id = {book['_id']}: {book.get('title', '')} by {authors}")

        print(f"navigate menu")
        print("1. Next page")
        print("2. Previous page")
        print("3. Select book by ID")
        print("4. Return to main menu")
        print("-"*70)
        choice = input("Enter choice: ")

        if choice == '1':
            page += 1
        elif choice == '2':
            if page > 1:
                page -= 1
            else:
                print("You are on the first page.")
        elif choice == '3' :
            book_id = input("Enter the _id of the book to delete: ")
            books_collection = db.get_collection(name="books")
            book = books_collection.find_one({"_id": int(book_id)})
            if not book:
                print("\nMessage:")
                print(f"Book with _id '{book_id}' not found")
                print("\n")
            # print(book)
            # print(type(book['file_id']),"\n\n")
            chunks = db.get_collection(name="fs.chunks")
            files = db.get_collection(name="fs.files")
            # documents = chunks.find({'files_id': book['file_id']})
            # print(list(documents))
            # docucment = files.find_one({"_id": book['file_id']})
            # print(docucment)
            res = chunks.delete_many({'files_id': book['file_id']})
            res2 = files.delete_one({"_id": book['file_id']})
            res3 = books_collection.delete_one({"_id": int(book_id)})
            # documents = chunks.find({'files_id': book['file_id']})
            # docucment = files.find_one({"_id": book['file_id']})
            # print(list(documents))
            # print(docucment)
            # print(res.acknowledged)
            # print(res2.acknowledged)
            # print(res3.acknowledged)
            if res.acknowledged and res2.acknowledged and res3.acknowledged:
                print(f"\n")
                print(f"Delete Book {int(book_id)} Success !")
                print(f"="*70)
            else:
                print(f"\n")
                print(f"Delete Book {int(book_id)} Failure !")
                print(f"="*70)
        elif choice == '4':
            break
        else:
            print("Invalid choice") 


def select_book_by_id(*, client, session, db):
    """ Select a book by _id and display other details """
    book_id = input("Enter the _id of the book to select: ")
    books_collection = db.get_collection(name="books")
    book = books_collection.find_one({"_id": int(book_id)})
    if not book:
        print("\nMessage:")
        print(f"Book with _id '{book_id}' not found")
        print("\n")
        return book_id
    print()
    print(f"\n{'Selected book details':^70s}\n")
    print(f"_id: {book['_id']}")
    print(f"Title: {book.get('title', '')}")
    print(f"Author: {', '.join([author.get('name', '') for author in book.get('author', [])])}")
    print(f"Language: {book.get('language', '')}")
    print(f"Publish Date: {book.get('publish_date', '')}")
    print(f"Genre: {', '.join(book.get('genre', []))}")
    print(f"Tag: {', '.join(book.get('tag', []))}")
    print(f"ISBN: {''.join(book.get('ISBN', []))}")
    print(f"Abstract: {''.join(book.get('abstract', []))}")
    
    display_author(client=client, session=session, db=db, book=book)
    return book

def display_author(*, client, session, db, book):
    authors_collection = db.get_collection(name="authors")
    author = authors_collection.find_one({"name": book.get('author')[0]['name']})
    if author:
        book_titles = ", ".join([book["title"] for book in author.get("books", [])])
        print()
        print(f"\n{'Author Details':^70s}\n")
        print(f"_id: {author['_id']}")
        print(f"Name: {author.get('name', '')}")
        print(f"Pseudonyms: {author.get('pseudonyms', '')}")
        print(f"Birthdate: {author.get('birthdate', '')}")
        print(f"Deathdate: {author.get('deathdate', '')}")
        print(f"Country: {author.get('country', '')}")
        print(f"Books: {book_titles}")
        print(f"Book Count: {len(author.get('books', []))}")
    
def update_book(*, client, session, db):
    try: 
        """ Update an existing book """
        display_update_paged(client=client, session=session, db=db, books_per_page=5)
    except KeyboardInterrupt as e:
        print("User Exit Feature with Ctrl-C!!")
        
def display_update_paged(*, client, session, db, books_per_page=5):
    """
    Display Update in a paged format.
    """
    books_collection = db.get_collection(name="books")
    total_books = books_collection.count_documents({})

    page = 1
    while True:
        print("\n")
        start_index = (page - 1) * books_per_page
        end_index = start_index + books_per_page
        books = list(books_collection.find({}, {"_id": 1, "title": 1, "author": 1}).skip(start_index).limit(books_per_page))
        print(f"\n{'Update Books Menu':^70s}\n")
        print(f"[ Page {page}/{(total_books + books_per_page - 1) // books_per_page} ]:")
        for book in books:
            authors = ", ".join([author["name"] for author in book.get("author", [{"name": ""}])])
            print(f"_id = {book['_id']}: {book.get('title', '')} by {authors}")

        print(f"navigate menu")
        print("1. Next page")
        print("2. Previous page")
        print("3. Select book by ID")
        print("4. Return to main menu")
        print("-"*70)
        choice = input("Enter choice: ")

        if choice == '1':
            page += 1
        elif choice == '2':
            if page > 1:
                page -= 1
            else:
                print("You are on the first page.")
        elif choice == '3' :
            book_id = input("Enter the _id of the book to update: ")
            books_collection = db.get_collection(name="books")
            book = books_collection.find_one({"_id": int(book_id)})
            if not book:
                print("\nMessage:")
                print(f"Book with _id '{book_id}' not found")
                print("\n")
                return
            print()
            print(f"\n{'Current book details':^70s}\n")
            print(f"_id: {book['_id']}")
            print(f"Title: {book.get('title', '')}")
            print(f"Author: {', '.join([author.get('name', '') for author in book.get('author', [])])}")
            print(f"Language: {book.get('language', '')}")
            print(f"Publish Date: {book.get('publish_date', '')}")
            print(f"Genre: {', '.join(book.get('genre', []))}")
            print(f"Tag: {', '.join(book.get('tag', []))}")
            print()
            while True:
                field_to_update = input("Enter the field to update (title, author, language, publish_date, genre, tag): ")
                field_to_update = field_to_update.lower()
                if field_to_update in ["title", "author", "language", "publish_date", "genre", "tag"]:
                    new_value = input(f"Enter the new value for '{field_to_update}': ")

                    update_query = {"$set": {field_to_update: new_value}}
                    try:
                        result = books_collection.update_one({"_id": int(book_id)}, update_query)
                        if result.modified_count == 1:
                            print(f"Book with _id '{book_id}' updated successfully")
                            break
                        else:
                            print(f"Could not update book with _id '{book_id}'")
                    except Exception as e:
                        print(f"Can't Update please:\n {e}")
                else:
                    print("Invalid input {field_to_update} !")
        elif choice == '4':
            break
        else:
            print("Invalid choice") 

"""search part"""    
def search_by_menu(*, client, session, db):
    try:
        print()
        print(f"\n{'Search by Menu':^70s}\n")
        print(" 1. Search by title")
        print(" 2. Search by _id")
        print(" 3. Search by author name")
        print(" 4. Search by genre")
        print(" 5. Search by main character")
        print(" 6. Search by language")
        print(" 7. Search by published year")
        print(" 8. Back to Main Menu")
        mchoice = input("Enter choice: ")
        if mchoice == '1':
                search_books_by_name(client=client, session=session, db=db)
        elif mchoice == '2':
                select_book_by_id(client=client, session=session, db=db)
        elif mchoice == '3':
                search_books_by_author(client=client, session=session, db=db)
        elif mchoice == '4':
                choose_category(client=client, session=session, db=db)
        elif mchoice == '5':
                search_books_by_main_character(client=client, session=session, db=db)
        elif mchoice == '6':
                search_books_by_language(client=client, session=session, db=db)
        elif mchoice == '7':
                search_books_by_publish_year(client=client, session=session, db=db)
        elif mchoice == '8':
                main()
        else:
            print("invalid choice")
    except KeyboardInterrupt as e:
        print("User Exit Feature with Ctrl-C!!")

def search_books_by_name(*, client, session, db):
    """
    Search for books by name.
    """
    search_query = input("Enter the book name to search for: ")
    books_collection = db.get_collection(name="books")
    books = list(books_collection.find({"title": {"$regex": search_query, "$options": "i"}}, {"_id": 1, "title": 1, "author": 1}))

    if books:
        print()
        print("Matching Books:")
        for book in books:
            authors = ", ".join([author["name"] for author in book.get("author", [{"name": ""}])])
            print(f"_id = {book['_id']}: {book.get('title', '')} by {authors}")
    else:
        print("No books found matching the search query.")
    display_books_paged(client=client, session=session, db=db)  
def search_books_by_author(*, client, session, db):
    """
    Search for books by author name.
    """
    author_name = input("Enter the author name to search for: ")
    books_collection = db.get_collection(name="books")
    books = list(books_collection.find({"author.name": {"$regex": author_name, "$options": "i"}}, {"_id": 1, "title": 1, "author": 1}))

    if books:
        print("Books by", author_name + ":")
        for book in books:
            authors = ", ".join([author["name"] for author in book.get("author", [{"name": ""}])])
            print(f"_id = {book['_id']}: {book.get('title', '')} by {authors}")
    else:
        print("No books found by", author_name)

    display_books_paged(client=client, session=session, db=db)       
def choose_category(*, client, session, db):
    """
    Show a list of all categories and let the user select one.
    """
    # Display categories for selection
    print("Available Categories:")
    for category in CATEGORIES_DATA:
        print(f"{category['_id']}: {category['name']}")

    # Get user input for category selection
    category_id = int(input("Enter the category ID to select: "))
    selected_category = next((category for category in CATEGORIES_DATA if category['_id'] == category_id), None)
    if not selected_category:
        print("Invalid category ID")
        return

    print(f"Selected Category: {selected_category['name']}")

    # Find all books in the selected category
    books_collection = db.get_collection(name="books")
    books = list(books_collection.find({"genre": selected_category['name']}, {"_id": 1, "title": 1}))
    if books:
        print()
        print("---- Books in this category ----")
        for book in books:
            print(f"_id = {book['_id']}: {book.get('title', '')}")
    else:
        print("No books found in this category.")
        
     # Display books menu
    print()
    print(f"\n{'Books menu':^70s}\n")
    print("1. See next page")
    print("2. Select book by ID")
    print("3. Return to main menu")
    print("-"*70)
    choice = input("Enter choice: ")
    if choice == '1':
        print("See next page")
    elif choice == '2':
        select_book_by_id(client=client, session=session, db=db)
    elif choice == '3':
        return  # Return to the main menu
    else:
        print("Invalid choice")    
def search_books_by_main_character(*, client, session, db):
    """
    Search for books by main character's name.
    """
    character_name = input("Enter the main character's name to search for: ")
    books_collection = db.get_collection(name="books")
    books = list(books_collection.find({"main_character": {"$regex": character_name, "$options": "i"}}, {"_id": 1, "title": 1, "author": 1}))

    if books:
        print(f"Books featuring {character_name}:")
        for book in books:
            authors = ", ".join([author["name"] for author in book.get("author", [{"name": ""}])])
            print(f"_id = {book['_id']}: {book.get('title', '')} by {authors}")
    else:
        print(f"No books found featuring {character_name}")

    display_books_paged(client=client, session=session, db=db)
def search_books_by_language(*, client, session, db):
    """
    Search for books by language.
    """
    language = input("Enter the language to search for: ")
    books_collection = db.get_collection(name="books")
    books = list(books_collection.find({"language": {"$regex": language, "$options": "i"}}, {"_id": 1, "title": 1, "author": 1}))

    if books:
        print(f"Books in {language}:")
        for book in books:
            authors = ", ".join([author["name"] for author in book.get("author", [{"name": ""}])])
            print(f"_id = {book['_id']}: {book.get('title', '')} by {authors}")
    else:
        print(f"No books found in {language}")

    display_books_paged(client=client, session=session, db=db)
def search_books_by_publish_year(*, client, session, db):
    """
    Search for books by publish year.
    """
    publish_year = input("Enter the publish year to search for: ")
    books_collection = db.get_collection(name="books")
    books = list(books_collection.find({"publish_date": {"$regex": f"^{publish_year}", "$options": "i"}}, {"_id": 1, "title": 1, "author": 1}))

    if books:
        print(f"Books published in {publish_year}:")
        for book in books:
            authors = ", ".join([author["name"] for author in book.get("author", [{"name": ""}])])
            print(f"_id = {book['_id']}: {book.get('title', '')} by {authors}")
    else:
        print(f"No books found published in {publish_year}")

    display_books_paged(client=client, session=session, db=db)
    
"""main part"""   
def display_books_paged(*, client, session, db, books_per_page=5):
    """
    Display books in a paged format.
    """
    books_collection = db.get_collection(name="books")
    total_books = books_collection.count_documents({})

    page = 1
    while True:
        print("\n")
        start_index = (page - 1) * books_per_page
        end_index = start_index + books_per_page
        books = list(books_collection.find({}, {"_id": 1, "title": 1, "author": 1}).skip(start_index).limit(books_per_page))
        print(f"\n{'Books Menu':^70s}\n")
        print(f"[ Page {page}/{(total_books + books_per_page - 1) // books_per_page} ]:")
        for book in books:
            authors = ", ".join([author["name"] for author in book.get("author", [{"name": ""}])])
            print(f"_id = {book['_id']}: {book.get('title', '')} by {authors}")

        print(f"navigate menu")
        print("1. Next page")
        print("2. Previous page")
        print("3. Select book by ID")
        print("4. Return to main menu")
        print("-"*70)
        choice = input("Enter choice: ")

        if choice == '1':
            page += 1
        elif choice == '2':
            if page > 1:
                page -= 1
            else:
                print("You are on the first page.")
        elif choice == '3' :
            select_book_by_id(client=client, session=session, db=db)
        elif choice == '4':
            break
        else:
            print("Invalid choice") 
def display_books_paged2(*, client, session, db, books_per_page=5):
    """
    Display books in a paged format.
    """
    books_collection = db.get_collection(name="books")
    total_books = books_collection.count_documents({})

    page = 1
    while True:
        start_index = (page - 1) * books_per_page
        end_index = start_index + books_per_page
        books = list(books_collection.find({}, {"_id": 1, "title": 1, "author": 1}).skip(start_index).limit(books_per_page))
        print(f"\n{'Books Menu':^70s}\n")
        print(f"[ Page {page}/{(total_books + books_per_page - 1) // books_per_page} ]:")
        for book in books:
            authors = ", ".join([author["name"] for author in book.get("author", [{"name": ""}])])
        print(f"\n")
        print("*"*70)
        # print(f"\n{'navigate menu':^70s}\n")
        print(f"navigate menu")
        print("1. Next page")
        print("2. Previous page")
        print("3. Select book by ID")
        print("4. Return to main menu")
        print("-"*70)
        choice = input("Enter choice: ")

        if choice == '1':
            page += 1
        elif choice == '2':
            if page > 1:
                page -= 1
            else:
                print("You are on the first page.")
        elif choice == '3' :
            select_book_by_id(client=client, session=session, db=db)
        elif choice == '4':
            break
        else:
            print("Invalid choice")            
def display_categories_paged(*, client, session, db, categories_per_page=5):
    """
    Display categories in a paged format.
    """
    categories_collection = db.get_collection(name="categories")
    total_categories = categories_collection.count_documents({})
    total_pages = (total_categories + categories_per_page - 1) // categories_per_page

    page = 1
    while True:
        start_index = (page - 1) * categories_per_page
        end_index = start_index + categories_per_page
        categories = list(categories_collection.find({}, {"_id": 1, "name": 1}).skip(start_index).limit(categories_per_page))
        print(f"\n{'Categories menu':^70s}\n")
        print(f"[ Page {page}/{total_pages} ] :")
        for category in categories:
            print(f"_id = {category['_id']}: {category.get('name', '')}")

        print(f"\n")
        print("*"*70)
        # print(f"\n{'Categories menu':^70s}\n")
        print(f"navigate menu")
        print("1. Next page")
        print("2. Previous page")
        print("3. Return to main menu")
        print("-"*70)
        choice = input("Enter choice: ")

        if choice == '1':
            page = min(page + 1, total_pages)
        elif choice == '2':
            page = max(page - 1, 1)
        elif choice == '3':
            break
        else:
            print("Invalid choice")
def display_authors_paged(*, client, session, db, authors_per_page=5):
    """
    Display authors in a paged format.
    """
    authors_collection = db.get_collection(name="authors")
    total_authors = authors_collection.count_documents({})
    total_pages = (total_authors + authors_per_page - 1) // authors_per_page

    page = 1
    while True:
        print("\n")
        start_index = (page - 1) * authors_per_page
        end_index = start_index + authors_per_page
        authors = list(authors_collection.find({}, {"_id": 1, "name": 1}).skip(start_index).limit(authors_per_page))
        print(f"\n{'Authors Menu':^70s}\n")
        print(f"[ Page {page}/{total_pages} ]:")
        for author in authors:
            print(f"_id = {author['_id']}: {author.get('name', '')}")

        print(f"\n")
        print("*"*70)
        # print(f"\n{'Authors menu':^70s}\n")
        print(f"navigate menu")
        print("1. Next page")
        print("2. Previous page")
        print("3. Return to main menu")
        print("-"*70)
        choice = input("Enter choice: ")

        if choice == '1':
            page = min(page + 1, total_pages)
        elif choice == '2':
            page = max(page - 1, 1)
        elif choice == '3':
            break
        else:
            print("Invalid choice")
        
            
def main():
    """ Main entry point """
    retcode = EXIT_SUCCESS # hope for the best
    # connect to MongoDB server and start a session
    try:
        with pymongo.MongoClient(host=HOST,
                                 port=PORT,
                                 directConnection=True,
                                 connect=True,
                                 timeoutMS=1000,
                                 socketTimeoutMS=1000,
                                 connectTimeoutMS=1000,
                                 serverSelectionTimeoutMS=1000,
                                 compressors=['zlib'],
                                 zlibCompressionLevel=9,
                                 appname="superparts2",
                                 fsync=True,
                                 uuidRepresentation="standard") as client, \
             client.start_session(causal_consistency=True) as session:
            db = client.get_database(name=DBNAME)
            try:
                retcode = ui.main_menu(mdata=[("View Categories",dump_categories),
                                              ("View Authors",pretty_dump_authors),
                                              ("View Books",pretty_dump_books),
                                              ("View Search by Menu",search_by_menu),
                                              ("Add Books",add_books),
                                              ("Delete Books",delete_books),
                                              ("Update Books",update_book),
                                              ("Add New Category",add_category),
                                              ("Download Book",download_book),
                                              ],
                                       client=client,session=session,db=db)
            except KeyboardInterrupt:
                # they hit Ctl-C
                print("\nProgram aborted by user request!")
                retcode = EXIT_FAILURE
    except pymongo.errors.ServerSelectionTimeoutError as xcpn:
        #print(f"xcpn._message={xcpn._message}")
        print(f"ERROR: Cannot connect to MongoDB server ({HOST}:{PORT})", file=sys.stderr)
        retcode = EXIT_FAILURE
    return retcode
    

HOST='127.0.0.1'
PORT=27017
DBNAME='bookdb'
EXIT_SUCCESS=0
EXIT_FAILURE=1
if __name__ == '__main__':
    raise SystemExit(main())
