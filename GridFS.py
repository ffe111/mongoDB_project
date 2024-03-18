#! /usr/bin/env python3
"""
GridFS.py for save and get file by GrideFS
func filenput for insert data to DB
     fileoutput for load data from DB
"""
import os
import sys
import stat
import pymongo
import gridfs 

class LengthError(Exception):
    """ file length is invalid """

class BadFile(Exception):
    """ file is invalid """

def fileinput(*, db, session, fname, fpath):
    """ Read in fname and write it back out again """
    if fpath[-5:] == ".epub":
        content_type = "EPUB BOOK"
        ftype = "epub"
    elif fpath[-4:] == ".pdf":
        content_type = "PDF BOOK"
        ftype = "pdf"
    else:
        raise BadFile(f"File {fpath} not .epub or .pdf file")

    filter = {"file_name": fname, "contentType": content_type}
    # get access to mydb's gridfs area
    fs = gridfs.GridFS(db)
    # if the file is already in the gridfs
    if fs.exists(filter, session=session):
        # find the gridfs _id
        the_id = fs.find_one(filter, no_cursor_timeout=True, session=session)._id
        # and use it to delete the file from the gridfs
        fs.delete(the_id, session=session)
        # delete 'the_id' variable so we don't accidentally use a stale _id value
        del the_id
    if os.path.isdir(fpath):
        raise BadFile(f"specified file \"{fpath}\" is a directory, not a file.")
    # open the file on disk for binary read
    try:
        with open(fpath,'rb') as infile:
            # load the file's data into gridfs, saving the generated _id in 'the_id'
            the_id = fs.put(infile.read(),
                            filename=fname,
                            content_type=content_type,
                            session=session)
            if the_id is None:
                raise BadFile(f'failed to save file "{fpath}" to GridFS.')
            # print(the_id)
    except FileNotFoundError:
        raise BadFile(f'specified file "{fpath}" does not exist.')
    return the_id, ftype

def fileoutput(*, db, session, fname, fid, ftype):
    filter = {"file_name": fname}
    fs = gridfs.GridFS(db)
    try:
        # search for the file we just loaded by name in gridfs
        with fs.find(filter, no_cursor_timeout=True, session=session) as cur:
            # for each match we find, show some information 
            for tfile in cur:
                print(f"_id={tfile._id}")
                print(f"name=\"{tfile.name}\"")
                print(f"length in bytes={tfile.length}")
                print(f"metadata={tfile.metadata}")
    
        # output filename will be original name with '.copy1' appended to it
        outfname = fname+'.'+ftype
        outfname = outfname.replace(' ', '_')
        # if the output file already exists, remove it
        try:
            os.remove(outfname)
        except FileNotFoundError:
            pass # ignore not found errors
        # open a outfname file on disk for binary write
        with open(outfname, 'wb') as outfile:
            # and copy the data from gridfs to that new file
            outfile.write(fs.get(fid, session=session).read())
        # make that new file read-only
        os.chmod(outfname, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)

        # fetch latest version of a file by name
        tfile = fs.get_last_version(filename=fname, session=session)
        _id, filename, filelength, upload_date = tfile._id, tfile.name, tfile.length, tfile.upload_date
        content_type, metadata = tfile.content_type, tfile.metadata
        first_two_bytes = tfile.read(2).hex().upper()
        tfile.seek(-2,2)
        last_two_bytes = tfile.read(2).hex().upper()
        tfile.close()
        print(f"_id={_id}\nname=\"{filename}\"\nlength in bytes={filelength}")
        print(f"upload date={upload_date}\ncontent type={content_type}")
        print(f"metadata={metadata}\n")
        if filelength != os.path.getsize(outfname):
            raise LengthError("Bad length, got {filelength}, expected {os.path.getsize(fname)}")
        
    except gridfs.errors.NoFile as e:
        print(f"Can't find data in GridFS: \n{e}")

def main():
    """ Main entry point """
    retcode = EXIT_SUCCESS
    try:
        client = pymongo.MongoClient(host=HOST,
                                 port=PORT,
                                 directConnection=True,
                                 connect=True,
                                 )
        session = client.start_session(causal_consistency=True)
        db = client.get_database(name=DBNAME)
        try:
            fid, ftype = fileinput(db=db, session=session, fname=INPUT_FILENAME, fpath=INPUT_FILEPATH)
            fileoutput(db=db, session=session, fname=INPUT_FILENAME, fid=fid, ftype=ftype)
        except (BadFile, LengthError) as excpn:
            print(excpn)
            retcode = EXIT_FAILURE # trouble ....
    except pymongo.errors.ServerSelectionTimeoutError as xcpn:
        #print(f"xcpn._message={xcpn._message}")
        print(f"ERROR: Cannot connect to MongoDB server ({HOST}:{PORT})", file=sys.stderr)
        retcode = EXIT_FAILURE
    return retcode

HOST='127.0.0.1'
PORT=27017
DBNAME='test'
EXIT_SUCCESS=0
EXIT_FAILURE=1
INPUT_FILENAME = "NOSQL.epub"
INPUT_FILEPATH = "./books/NOSQL.epub"
TEST_FILENAME = "NOSQLaaa.epub"

if __name__ == "__main__":
     raise SystemExit(main())