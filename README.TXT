"""
README.TXT file
"""
Submit by:
 Student id:    --------
 Name:          -------- -----

About project:
Project Book Store Database with MongoDB
like a https://gutenberg.org (Thanks for reference of book data),
Program -can CURD for manament data in database
        such Add_book(Create) insert book data and file,
             Update_book(Update) update book detail data 
                              in database,
             Delete_book(Delete) delete book data and file
                              in database.
        -can Search about tag 
        such as title, _id, author_name,
                genre and etc. (8 function Search)
and Download ebook and Upload ebook to Database.

Requirement:
    mongod --version is "db version v7.0.5" or better.
    (https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)
    Python 3.10.12 or better.
    python library pymongo==4.6.2 (detail in requirement.txt)
    (https://pymongo.readthedocs.io/en/stable/installation.html)

Before use Program:
    1. read README.TXT see about detail and Requirement. 
    2. you should check this mongod is start or use command:

    sudo systemctl start mongod   #start mongod service

    3. you should create python environment command:  

    python3 -m venv --clear --copies --upgrade-deps --prompt ’mongovenv’ mongovenv

       *but! if you don't have python environment please use command ot install:

    sudo apt install python3.10-venv

    4. when create environment success you can see ./mongovenv directory
       you should active python environment by command:

    source source mongovenv/bin/activate

       and install library by requirement.txt by command:

    python3 -m pip install -r requirement.txt

        *but if you don't have python pip please use command ot install:
    sudo apt install python3-pip 
        (https://pymongo.readthedocs.io/en/stable/installation.html)

    5. if not found problem, That's mean 
    you ready to use This Project Program!!!

About File in Project:
64160118/                 | head folder
64160118/books/*          | directory store book test file (.epub and .pdf)
64160118/README.TXT       | this file. tell about project
64160118/requirement.txt  | library requirement for python pip install
64160118/BulkLoader.py    | program load data before start client 
64160118/GridFS.py        | program gridfs for save_file and load_file from DB
64160118/metadata.py      | metadata books storage [DATA, SCHEMA]
64160118/client.py        | program for use manage database [CURD, Search] 
64160118/u1.py            | program for display ui text interface

How to use:
1. first run BulkLoader.py 
   to loaddata in mongo database.
   
   Successful for <Load_Bulk_Data> !!!

2. run client.py to use program
   manage CURD search 

MAINMENU Choice Pick.
    ======================================================================

                                Main Menu

    **********************************************************************
    1.  View Categories
    2.  View Authors
    3.  View Books
    4.  View Search by Menu
    5.  Add Books
    6.  Delete Books
    7.  Update Books
    8.  Add New Category
    9.  Download Book
    10.  Exit

    ======================================================================
    Enter choice: 3
"explain program will call ui menu to display interface menu
and get_choice input to call any function."


___________________________________________________________________________________
BOOKS Show list. (Search)

                                Books Menu

    [ Page 1/5 ]:
    _id = 1: The Odyssey by Homer
    _id = 2: The Count of Monte Cristo by Alexandre Dumas
    _id = 3: Dracula by Bram Stoker
    _id = 4: The War of the Worlds by H.G. Wells
    _id = 5: The Count of Monte Cristo by Alexandre Dumas
    navigate menu
    1. Next page
    2. Previous page
    3. Select book by ID
    4. Return to main menu
    ----------------------------------------------------------------------
    Enter choice: 3
    Enter the _id of the book to select: 1
"explain program will get all bug data and Manage data for display interface
user can enter choice 1.Next page show Next data+5
                      2. Previous page show Previous data-5
                      3. Select book by ID for get this input number by _id
                      4. Return to main menu go to main menu"


___________________________________________________________________________________
Show Book detail. (Search)
                            Selected book details

    _id: 1
    Title: The Odyssey
    Author: Homer
    Language: English
    Publish Date: 1818-01-01
    Genre: epic poetry
    Tag: classic, adventure
    ISBN: 9780140449112
    Abstract: The Odyssey is one of two major ancient Greek epic poems attributed to Homer.
    It follows the Greek hero Odysseus, king of Ithaca, and his journey home after the fall of Troy.


                                Author Details

    _id: 2
    Name: Homer
    Pseudonyms:
    Birthdate: Unknown
    Deathdate: Unknown
    Country: Greece
    Books: The Odyssey, The Iliad
    Book Count: 2
___________________________________________________________________________________
Add New Book. (Create)

                               Add Book

Enter Book Title: The Alice in Burapha
Enter Author Name: Big Potato
Enter Language: English
Enter Publish Date (1990-12-01): 2002-12-22
Enter Genre: Adventure
Enter File Path (./NOSQL.epub): ./books/NOSQL.epub
Enter File Name: The Alice in Burapha
Enter ISBN (9876543210102): 9876543210102

Book 'The Alice in Burapha' added successfully with _id 22
******************************
"explain program will get input data to format {data base Schema}
while input success sent input_data add to database [collection books]
and read file path and load to database with GridFS"


___________________________________________________________________________________
Delete Book data. (Delete)

                          Delete Books Menu

[ Page 5/5 ]:
_id = 21: Frankenstein; Or, The Modern Prometheus by Mary Wollstonecraft Shelley
_id = 22: The Alice in Burapha by Big Potato
navigate menu
1. Next page
2. Previous page
3. Select book by ID
4. Return to main menu
----------------------------------------------------------------------
Enter choice: 3
Enter the _id of the book to delete: 22


Delete Book 22 Success !
======================================================================
"explain program will get input _id to get data in database, find fs.chunk fs.files 
by ObjectId user _id to delete file in database collection  [fs.chunk, fs.files] 
and delte book by bookid(_id)"


___________________________________________________________________________________
Update Book data. (Update)

                          Update Books Menu

[ Page 1/5 ]:
_id = 1: Odyssey of Jingle's Bell by Homer
_id = 2: The Count of Monte Cristo by Alexandre Dumas
_id = 3: Dracula by Bram Stoker
_id = 4: The War of the Worlds by H.G. Wells
_id = 5: The Count of Monte Cristo by Alexandre Dumas
navigate menu
1. Next page
2. Previous page
3. Select book by ID
4. Return to main menu
----------------------------------------------------------------------
Enter choice: 3
Enter the _id of the book to update: 1


                         Current book details

_id: 1
Title: Odyssey of Jingle's Bell
Author: Homer
Language: English
Publish Date: 1818-01-01
Genre: epic poetry
Tag: classic, adventure

Enter the field to update (title, author, language, publish_date, genre, tag): Title
Enter the new value for 'title': Odyssey of Jingle's Bear
Book with _id '1' updated successfully

"explain program will get _id of book and show data for User,
User choose tag data to update and enter new_data update
program will update by [_id, tag: new_data]"


___________________________________________________________________________________


And any function in program.
Thanks.;=;;