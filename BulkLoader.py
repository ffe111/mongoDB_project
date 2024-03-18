#! /usr/bin/env python3
"""
bulkloader.py
Load databook to MongoDB first
"""
import sys
import pymongo 
from GridFS import *
from metadata import *

def delete_collections(*,client,session,db, coltsname):
    """ Delete the collection name"""
    try:
        retval = db.drop_collection(coltsname)
    except pymongo.errors.WriteError as xcpn:
        print(xcpn.details['errmsg'], file=sys.stderr)
        return
    if retval['ok'] != 1.0:
        print(retval)
        raise SystemExit(EXIT_FAILURE)
    if coltsname in db.list_collection_names():
        print(f"drop \"{coltsname}\" failed!", file=sys.stderr)
        raise SystemExit(EXIT_FAILURE)
    
def create_collections(*, client, session, db, coltsname, coltsdata, schema):
    """ Create the authors collection and insert some test data """
    try:
        # collection = db.create_collection(coltsname)
        collection = db.create_collection(
           coltsname,
           validator=schema,
           validationLevel="strict",
           validationAction="error")
    except pymongo.errors.CollectionInvalid as xcpn:
        print(f"Unable to create {coltsname} collection:", xcpn)
        raise SystemExit(EXIT_FAILURE)
    if not isinstance(collection, pymongo.collection.Collection):
        print(f"Unable to create {coltsname} collection:", collection)
        raise SystemExit(EXIT_FAILURE)
    try:
        collection.insert_many(coltsdata, session=session)
    except pymongo.errors.BulkWriteError as xcpn:
        print("Failure loading authors:", xcpn, file=sys.stderr)
        raise SystemExit(EXIT_FAILURE)
    
def create_books(*, client, session, db, coltsname, coltsdata, schema):
    """ Create the collection name and insert some test data """
    try:
        collection = db.create_collection(
           coltsname,
           validator=schema,
           validationLevel="strict",
           validationAction="error")
    except pymongo.errors.CollectionInvalid as xcpn:
        print(f"Unable to create '{coltsname}' collection: {xcpn}")
        raise SystemExit(EXIT_FAILURE)
    if not isinstance(collection, pymongo.collection.Collection):
        print(f"\n\n\nUnable to create '{coltsname}' collection: {collection}")
        raise SystemExit(EXIT_FAILURE)
    collection.create_index([("name", pymongo.ASCENDING)],unique=False,session=session)
    try:
        for document in coltsdata:
            # print(document)
            file_id, file_type = fileinput(db=db, session=session, fname=document['file_name'], fpath=document['file_path'])
            if file_id and file_type:
                document["file_id"] = file_id
                document["file_type"] = file_type
                collection.insert_one(document, session=session)
    except pymongo.errors.BulkWriteError as excp:
        print(f"Failure loading {coltsname}: {excp}", file=sys.stderr)
        raise SystemExit(EXIT_FAILURE)
    return True

def initialize_db(*, client,session,db):
    old_collection_names = db.list_collection_names()

    # initial CATEGORIES
    if "categories" in old_collection_names:
        delete_collections(client=client,session=session,db=db, coltsname='categories')
    create_collections(client=client, session=session, db=db, coltsname='categories', coltsdata=CATEGORIES_DATA, schema=CATEGORIES_SCHEMA)
    
    # initial AUTHORS
    if "authors" in old_collection_names:
        delete_collections(client=client,session=session,db=db, coltsname='authors')
    create_collections(client=client, session=session, db=db, coltsname='authors', coltsdata=AUTHORS_DATA, schema=AUTHORS_SCHEMA)
    
    # initial BOOKS
    if "books" in old_collection_names:
        delete_collections(client=client,session=session,db=db, coltsname='books')
    try:
        create_books(client=client, session=session, db=db, coltsname='books', coltsdata=BOOKS_DATA, schema=BOOKS_SCHEMA)
    except Exception as e:
        print(f"Can't Create Book\n{e}")
        raise SystemExit(EXIT_FAILURE)

def main():
    """ Main entry point """
    # connect to MongoDB server and start a session
    retcode=EXIT_SUCCESS
    try:
        client = pymongo.MongoClient(host=HOST,
                                 port=PORT,
                                 directConnection=True,
                                 connect=True,
                                 )
        session = client.start_session(causal_consistency=True)
        db = client.get_database(name=DBNAME)
        initialize_db(client=client,session=session,db=db)
        print("Successful for <Load_Bulk_Data> !!!")
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
