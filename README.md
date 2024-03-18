# mongoDB_project

## About project:
```Project Book Store Database with MongoDB
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
and Download ebook and Upload ebook to Database.```

## Requirement:
    ```mongod --version is "db version v7.0.5" or better.
    (https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)
    Python 3.10.12 or better.
    python library pymongo==4.6.2 (detail in requirement.txt)
    (https://pymongo.readthedocs.io/en/stable/installation.html)```

## Before use Program:
    ```1. read README.TXT see about detail and Requirement. 
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
    you ready to use This Project Program!!!```

## About File in Project:
```64160118/                 | head folder
64160118/books/*          | directory store book test file (.epub and .pdf)
64160118/README.TXT       | this file. tell about project
64160118/requirement.txt  | library requirement for python pip install
64160118/BulkLoader.py    | program load data before start client 
64160118/GridFS.py        | program gridfs for save_file and load_file from DB
64160118/metadata.py      | metadata books storage [DATA, SCHEMA]
64160118/client.py        | program for use manage database [CURD, Search] 
64160118/u1.py            | program for display ui text interface```

## How to use:
```1. first run BulkLoader.py 
   to loaddata in mongo database.
   
   Successful for <Load_Bulk_Data> !!!

2. run client.py to use program
   manage CURD search```
