#! /usr/bin/env python3
"""
metadata.py data for bulk load
store data, shema set database 
"""

# BOOKS: DATA SCHEMA
#
BOOKS_REGEX = "^([A-Za-z0-9&-;:,.()/' ]+)$"

BOOKS_SCHEMA = {"$jsonSchema": {
   "title": "Book record",
   "bsonType": "object",
   "required": ["_id", "title", "author", "language", "publish_date", "genre", "file_path", "ISBN"],
   "properties": {
      "_id": {
         "bsonType": ["int", "objectId"],
         "minimum": 0,
         "description": "primary key, book number, must be a non-negative integer, unique and is required"
      },
      "title": {
         "bsonType": "string",
         "minLength": 1,
         "maxLength": 255,
         "pattern": BOOKS_REGEX,
         "description": "Title of the book"
      },
      "author": {
         "bsonType": "array",
         "minItems": 1,
         "items": {
            "bsonType": "object",
            "required": ["name"],
            "properties": {
               "name": {
                  "bsonType": "string",
                  "minLength": 1,
                  "maxLength": 255,
                  "pattern": "^([\p{L}'-. ]+)$",
                  "description": "Author's name"
               }
            }
         },
         "description": "Array of author objects, each containing the author's name"
      },
      "language": {
         "bsonType": "string",
         "minLength": 1,
         "maxLength": 255,
         "pattern": "^([\p{L}'-. ]+)$",
         "description": "Language of the book"
      },
      "publish_date": {
         "bsonType": "string",
         "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
         "description": "Publish date of the book in the format YYYY-MM-DD"
      },
      "genre": {
         "bsonType": "array",
         "minItems": 1,
         "items": {
            "bsonType": "string",
            "minLength": 1,
            "maxLength": 255,
            "pattern": "^([\p{L}'-. ]+)$",
            "description": "Genre of the book"
         },
         "description": "Array of genres associated with the book"
      },
      "subgenre": {
         "bsonType": "array",
         "items": {
            "bsonType": "string",
            "minLength": 1,
            "maxLength": 255,
            "pattern": "^([\p{L}'-. ]+)$",
            "description": "Subgenre of the book"
         },
         "description": "Array of subgenres associated with the book"
      },
      "main_character": {
         "bsonType": "array",
         "items": {
            "bsonType": "string",
            "minLength": 1,
            "maxLength": 255,
            "pattern": "^([\p{L}'-. ]+)$",
            "description": "Main character of the book"
         },
         "description": "Array of main characters associated with the book"
      },
      "tag": {
         "bsonType": "array",
         "items": {
            "bsonType": "string",
            "minLength": 1,
            "maxLength": 255,
            "pattern": "^([A-Za-z- ]+)$",
            "description": "Tag associated with the book"
         },
         "description": "Array of tags associated with the book"
      },
      "copyright": {
         "bsonType": "string",
         "minLength": 1,
         "maxLength": 255,
         "description": "Copyright information of the book"
      },
      "abstract": {
         "bsonType": "string",
         "minLength": 1,
         "description": "Abstract or summary of the book"
      },
      "ISBN": {
         "bsonType": "string",
         "minLength": 1,
         "maxLength": 255,
         "description": "ISBN of the book"
      },
      "file_path": {
         "bsonType": "string",
         "minLength": 1,
         "pattern": '^\./.*\.(epub|pdf)$',
         "description": "File path of the book"
      },
      "file_name": {
         "bsonType": "string",
         "minLength": 1,
         "description": "File path of the book"
      },
      "file_type": {
         "bsonType": "string",
         "minLength": 1,
         "description": "File type of the book (pdf or epub)"
      },
      "file_id": {
         "bsonType": "objectId",
         "minLength": 1,
         "description": "File id of the book"
      },
   },
   "additionalProperties": False
}}

BOOKS_DATA=[
    {
        "_id": 1,
        "title": "The Odyssey",
        "author": [{"name": "Homer"}],
        "language": "English",
        "publish_date": "1818-01-01",
        "genre": ["epic poetry"],
        "subgenre": [],
        "main_character": ["Odysseus"],
        "tag": ["classic", "adventure"],
        "copyright": "Public domain in the USA",
        "abstract": "The Odyssey is one of two major ancient Greek epic poems attributed to Homer. It follows the Greek hero Odysseus, king of Ithaca, and his journey home after the fall of Troy.",
        "ISBN": "9780140449112",
        "file_name": "The Odyssey",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 2,
        "title": "The Count of Monte Cristo",
        "author": [{"name": "Alexandre Dumas"}],
        "language": "English",
        "publish_date": "1844-08-28",
        "genre": ["adventure"],
        "subgenre": [],
        "main_character": ["Edmond Dantès"],
        "tag": ["classic", "revenge"],
        "copyright": "Public domain in the USA",
        "abstract": "The Count of Monte Cristo is an adventure novel by Alexandre Dumas. It is one of the author's most popular works, along with The Three Musketeers.",
        "ISBN": "9780141392462",
        "file_name": "The Count of Monte Cristo",
        "file_path": "./books/NOSQL.pdf"
    },
    {
        "_id": 3,
        "title": "Dracula",
        "author": [{"name": "Bram Stoker"}],
        "language": "English",
        "publish_date": "1897-05-26",
        "genre": ["Gothic", "horror"],
        "subgenre": [],
        "main_character": ["Count Dracula"],
        "tag": ["classic", "vampire"],
        "copyright": "Public domain in the USA",
        "abstract": "Dracula is an 1897 Gothic horror novel by Irish author Bram Stoker. It introduced the character of Count Dracula and established many conventions of subsequent vampire fantasy.",
        "ISBN": "9780141439845",
        "file_name": "Dracula",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 4,
        "title": "The War of the Worlds",
        "author": [{"name": "H.G. Wells"}],
        "language": "English",
        "publish_date": "1898-05-01",
        "genre": ["science fiction"],
        "subgenre": [],
        "main_character": ["Narrator"],
        "tag": ["classic", "alien invasion"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141441039",
        "abstract": "The War of the Worlds is a science fiction novel by English author H. G. Wells, first serialized in 1897 by Pearson's Magazine in the UK and by Cosmopolitan magazine in the US.",
        "file_name": "The War of the Worlds",
        "file_path": "./books/NOSQL.pdf"
    },
    {
        "_id": 5,
        "title": "The Count of Monte Cristo",
        "author": [{"name": "Alexandre Dumas"}],
        "language": "English",
        "publish_date": "1844-08-28",
        "genre": ["adventure"],
        "subgenre": [],
        "main_character": ["Edmond Dantès"],
        "tag": ["classic", "revenge"],
        "copyright": "Public domain in the USA",
        "abstract": "The Count of Monte Cristo is an adventure novel by Alexandre Dumas. It is one of the author's most popular works, along with The Three Musketeers.",
        "ISBN": "9780141392462",
        "file_name": "The Count of Monte Cristo",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 6,
        "title": "The War of the Worlds",
        "author": [{"name": "H.G. Wells"}],
        "language": "English",
        "publish_date": "1898-05-01",
        "genre": ["science fiction"],
        "subgenre": [],
        "main_character": ["Narrator"],
        "tag": ["classic", "alien invasion"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141441039",
        "abstract": "The War of the Worlds is a science fiction novel by English author H. G. Wells, first serialized in 1897 by Pearson's Magazine in the UK and by Cosmopolitan magazine in the US.",
        "file_name": "The_War_of_the_Worlds",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 7,
        "title": "Robinson Crusoe",
        "author": [{"name": "Daniel Defoe"}],
        "language": "English",
        "publish_date": "1719-04-25",
        "genre": ["adventure"],
        "subgenre": [],
        "main_character": ["Robinson Crusoe"],
        "tag": ["classic", "castaway"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141439821",
        "abstract": "Robinson Crusoe is a novel by Daniel Defoe, first published on 25 April 1719. The first edition credited the work's protagonist Robinson Crusoe as its author, leading many readers to believe he was a real person and the book a travelogue of true incidents.",
        "file_name": "Robinson Crusoe",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 8,
        "title": "The Adventures of Sherlock Holmes",
        "author": [{"name": "Arthur Conan Doyle"}],
        "language": "English",
        "publish_date": "1892-10-14",
        "genre": ["detective fiction"],
        "subgenre": [],
        "main_character": ["Sherlock Holmes", "Dr. John Watson"],
        "tag": ["classic", "mystery"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780142437052",
        "abstract": "The Adventures of Sherlock Holmes is a collection of twelve short stories by Arthur Conan Doyle, featuring his fictional detective Sherlock Holmes.",
        "file_name": "The Adventures of Sherlock Holmes",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 9,
        "title": "Gulliver's Travels",
        "author": [{"name": "Jonathan Swift"}],
        "language": "English",
        "publish_date": "1726-10-28",
        "genre": ["adventure"],
        "subgenre": [],
        "main_character": ["Lemuel Gulliver"],
        "tag": ["classic", "satire"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141439975",
        "abstract": "Gulliver's Travels, or Travels into Several Remote Nations of the World. In Four Parts. By Lemuel Gulliver, First a Surgeon, and then a Captain of Several Ships, is a prose satire by the Irish writer and clergyman Jonathan Swift, satirizing both human nature and the 'travellers' 'tales' literary subgenre.",
        "file_name": "Gulliver's Travels",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 10,
        "title": "The Jungle Book",
        "author": [{"name": "Rudyard Kipling"}],
        "language": "English",
        "publish_date": "1894-04-01",
        "genre": ["children's literature"],
        "subgenre": [],
        "main_character": ["Mowgli"],
        "tag": ["classic", "animals"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141325293",
        "abstract": "The Jungle Book is a collection of stories by the English author Rudyard Kipling. Most of the characters are animals such as Shere Khan the tiger and Baloo the bear, though a principal character is the boy or 'man-cub' Mowgli, who is raised in the jungle by wolves.",
        "file_name": "The Jungle Book",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 11,
        "title": "Treasure Island",
        "author": [{"name": "Robert Louis Stevenson"}],
        "language": "English",
        "publish_date": "1883-11-14",
        "genre": ["adventure"],
        "subgenre": [],
        "main_character": ["Jim Hawkins"],
        "tag": ["classic", "pirates"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141321004",
        "abstract": "Treasure Island is an adventure novel by Scottish author Robert Louis Stevenson, narrating a tale of 'buccaneers and buried gold'.",
        "file_name": "Treasure Island",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 12,
        "title": "Alice's Adventures in Wonderland",
        "author": [{"name": "Lewis Carroll"}],
        "language": "English",
        "publish_date": "1865-11-26",
        "genre": ["fantasy"],
        "subgenre": [],
        "main_character": ["Alice"],
        "tag": ["classic", "nonsense"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141192490",
        "abstract": "Alice's Adventures in Wonderland is an 1865 novel by Lewis Carroll. It tells of a young girl named Alice, who falls through a rabbit hole into a subterranean fantasy world populated by peculiar, anthropomorphic creatures.",
        "file_name": "Alice's Adventures in Wonderland",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 13,
        "title": "Moby-Dick; or, The Whale",
        "author": [{"name": "Herman Melville"}],
        "language": "English",
        "publish_date": "1851-10-18",
        "genre": ["adventure"],
        "subgenre": [],
        "main_character": ["Ishmael", "Captain Ahab"],
        "tag": ["classic", "whaling"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780142437243",
        "abstract": "Moby-Dick; or, The Whale is an 1851 novel by American writer Herman Melville. The book is the sailor Ishmael's narrative of the obsessive quest of Ahab, captain of the whaling ship Pequod, for revenge on Moby Dick, the giant white sperm whale that on the ship's previous voyage bit off Ahab's leg at the knee.",
        "file_name": "Moby-Dick; or, The Whale",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 14,
        "title": "Wuthering Heights",
        "author": [{"name": "Emily Brontë"}],
        "language": "English",
        "publish_date": "1847-12-01",
        "genre": ["Gothic", "romance"],
        "subgenre": [],
        "main_character": ["Heathcliff", "Catherine Earnshaw"],
        "tag": ["classic", "tragedy"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141439555",
        "abstract": "Wuthering Heights is Emily Brontë's only novel. It was first published in 1847 under the pseudonym Ellis Bell, and a posthumous second edition was edited by her sister Charlotte. The name of the novel comes from the Yorkshire manor on the moors on which the story centres (as an adjective, wuthering is a Yorkshire word referring to turbulent weather).",
        "file_name": "Wuthering Heights",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 15,
        "title": "Pride and Prejudice",
        "author": [{"name": "Jane Austen"}],
        "language": "English",
        "publish_date": "1813-01-28",
        "genre": ["novel"],
        "subgenre": [],
        "main_character": ["Elizabeth Bennet", "Fitzwilliam Darcy"],
        "tag": ["classic", "romance"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141439517",
        "abstract": "Pride and Prejudice is an 1813 novel of manners by Jane Austen. The novel follows the character development of Elizabeth Bennet, the dynamic protagonist of the book who learns about the repercussions of hasty judgments and comes to appreciate the difference between superficial goodness and actual goodness.",
        "file_name": "Pride and Prejudice",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 16,
        "title": "Jane Eyre",
        "author": [{"name": "Charlotte Brontë"}],
        "language": "English",
        "publish_date": "1847-10-16",
        "genre": ["Gothic", "romance"],
        "subgenre": [],
        "main_character": ["Jane Eyre", "Edward Rochester"],
        "tag": ["classic", "feminism"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141441145",
        "abstract": "Jane Eyre is a novel by English writer Charlotte Brontë, published under the pen name 'Currer Bell', on 16 October 1847, by Smith, Elder & Co. of London. The first American edition was published the following year by Harper & Brothers of New York.",
        "file_name": "Jane Eyre",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 17,
        "title": "Anna Karenina",
        "author": [{"name": "Leo Tolstoy"}],
        "language": "Russian",
        "publish_date": "1877-01-01",
        "genre": ["novel"],
        "subgenre": [],
        "main_character": ["Anna Karenina"],
        "tag": ["classic", "tragedy"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141441169",
        "abstract": "Anna Karenina is a novel by the Russian author Leo Tolstoy, first published in book form in 1878. Many writers consider Anna Karenina the greatest work of literature ever, and Tolstoy himself called it his first true novel.",
        "file_name": "Anna Karenina",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 18,
        "title": "Little Women",
        "author": [{"name": "Louisa May Alcott"}],
        "language": "English",
        "publish_date": "1868-09-30",
        "genre": ["novel"],
        "subgenre": [],
        "main_character": ["Jo March", "Meg March", "Beth March", "Amy March"],
        "tag": ["classic", "family"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141441142",
        "abstract": "Little Women is a novel by American author Louisa May Alcott (1832–1888), originally published in two volumes in 1868 and 1869. Alcott wrote the book over several months at the request of her publisher.",
        "file_name": "Little Women",
        "file_path": "./books/NOSQL.epub"
        
    },
    {
        "_id": 19,
        "title": "The Picture of Dorian Gray",
        "author": [{"name": "Oscar Wilde"}],
        "language": "English",
        "publish_date": "1890-07-01",
        "genre": ["Gothic", "philosophical fiction"],
        "subgenre": [],
        "main_character": ["Dorian Gray"],
        "tag": ["classic", "vanity"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141442477",
        "abstract": "The Picture of Dorian Gray is a Gothic and philosophical novel by Oscar Wilde, first published complete in the July 1890 issue of Lippincott's Monthly Magazine. Fearing the story was indecent, the magazine's editor deleted roughly five hundred words before publication.",
        "file_name": "The Picture of Dorian Gray",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id": 20,
        "title": "Great Expectations",
        "author": [{"name": "Charles Dickens"}],
        "language": "English",
        "publish_date": "1861-08-01",
        "genre": ["novel"],
        "subgenre": [],
        "main_character": ["Pip", "Miss Havisham", "Abel Magwitch"],
        "tag": ["classic", "coming-of-age"],
        "copyright": "Public domain in the USA",
        "ISBN": "9780141442446",
        "abstract": "Great Expectations is the thirteenth novel by Charles Dickens and his penultimate completed novel, which depicts the education of an orphan nicknamed Pip (the book is a bildungsroman, a coming-of-age story).",
        "file_name": "Great Expectations",
        "file_path": "./books/NOSQL.epub"
    },
    {
        "_id" : 21,
        "title": "Frankenstein; Or, The Modern Prometheus",
        "author": [{"name": "Mary Wollstonecraft Shelley"}],
        "language": "English",
        "publish_date": "1818-01-01",
        "genre": ["horror"],
        "subgenre": ["science fiction"],
        "main_character": ["Frankenstein"],
        "tag": ["classic", "monster"],
        "copyright": "Public domain in the USA",
        "abstract": "Frankenstein tells the story of scientist Victor Frankenstein, who creates a sapient creature in an unorthodox scientific experiment.",
        "ISBN": "9780520201798",
        "file_name": "Frankenstein; Or, The Modern Prometheus",
        "file_path": "./books/NOSQL.epub"
    },
]

# AUTHORS: DATA SCHEMA
#
AUTHORS_DATA =[
    {
        "_id": 1,
        "name": "Mary Wollstonecraft Shelley",
        "psuedonyms": "None",
        "birthdate": "August 30, 1797",
        "deathdate": "February 1, 1851",
        "country": "United Kingdom",
        "books": [
            {
                "title": "Frankenstein; Or, The Modern Prometheus"
            }
        ],
        "book_count": 1 
    },
    {
        "_id": 2,
        "name": "Homer",
        "psuedonyms": "None",
        "birthdate": "Unknown",
        "deathdate": "Unknown",
        "country": "Greece",
        "books": [{"title": "The Odyssey"},{"title": "The Iliad"}],
        "book_count": 2
    },
    {
        "_id": 3,
        "name": "Alexandre Dumas",
        "psuedonyms": "None",
        "birthdate": "July 24, 1802",
        "deathdate": "December 5, 1870",
        "country": "France",
        "books": [{"title": "The Count of Monte Cristo"}],
        "book_count": 1
    },
    {
        "_id": 4,
        "name": "Bram Stoker",
        "psuedonyms": "None",
        "birthdate": "November 8, 1847",
        "deathdate": "April 20, 1912",
        "country": "Ireland",
        "books": [{"title": "Dracula"}],
        "book_count": 1    
    },
    {
        "_id": 5,
        "name": "H.G. Wells",
        "psuedonyms": "None",
        "birthdate": "September 21, 1866",
        "deathdate": "August 13, 1946",
        "country": "United Kingdom",
        "books": [{"title": "The Time Machine"},{"title": "The War of the Worlds"}],
        "book_count": 2       
    },
    {
        "_id": 6,
        "name": "Jack London",
        "psuedonyms": "None",
        "birthdate": "January 12, 1876",
        "deathdate": "November 22, 1916",
        "country": "United States",
        "books": [{"title": "The Call of the Wild"}],
        "book_count": 1
        
    },
    {
        "_id": 7,
        "name": "Daniel Defoe",
        "psuedonyms": "None",
        "birthdate": "Unknown",
        "deathdate": "April 24, 1731",
        "country": "United Kingdom",
        "books": [{"title": "Robinson Crusoe"}],
        "book_count": 1        
    },
    {
        "_id": 8,
        "name": "Arthur Conan Doyle",
        "psuedonyms": "None",
        "birthdate": "May 22, 1859",
        "deathdate": "July 7, 1930",
        "country": "United Kingdom",
        "books": [{"title": "The Adventures of Sherlock Holmes"},{"title": "The Hound of the Baskervilles"}],
        "book_count": 2     
    },
    {
        "_id": 9,
        "name": "Jonathan Swift",
        "psuedonyms": "None",
        "birthdate": "November 30, 1667",
        "deathdate": "October 19, 1745",
        "country": "Ireland",
        "books": [{"title": "Gulliver's Travels"}],
        "book_count": 1,
        
    },
    {
        "_id": 10,
        "name": "Rudyard Kipling",
        "psuedonyms": "None",
        "birthdate": "December 30, 1865",
        "deathdate": "January 18, 1936",
        "country": "India (British)",
        "books": [{"title": "The Jungle Book"}],
        "book_count": 1       
    },
    {
        "_id": 11,
        "name": "Robert Louis Stevenson",
        "psuedonyms": "None",
        "birthdate": "November 13, 1850",
        "deathdate": "December 3, 1894",
        "country": "United Kingdom",
        "books": [{"title": "Treasure Island"},{"title": "The Strange Case of Dr Jekyll and Mr Hyde"}],
        "book_count": 2       
    },
    {
        "_id": 12,
        "name": "Lewis Carroll",
        "psuedonyms": "Lewis Carroll (real name: Charles Lutwidge Dodgson)",
        "birthdate": "January 27, 1832",
        "deathdate": "January 14, 1898",
        "country": "United Kingdom",
        "books": [{"title": "Alice's Adventures in Wonderland"}],
        "book_count": 1     
    },
    {
        "_id": 13,
        "name": "Herman Melville",
        "psuedonyms": "None",
        "birthdate": "August 1, 1819",
        "deathdate": "September 28, 1891",
        "country": "United States",
        "books": [{"title": "Moby-Dick; or, The Whale"}],
        "book_count": 1       
    },
    {
        "_id": 14,
        "name": "Emily BrontÃ",
        "psuedonyms": "None",
        "birthdate": "July 30, 1818",
        "deathdate": "December 19, 1848",
        "country": "United Kingdom",
        "books": [{"title": "Wuthering Heights"}],
        "book_count": 1       
    },
    {
        "_id": 15,
        "name": "Jane Austen",
        "psuedonyms": "None",
        "birthdate": "December 16, 1775",
        "deathdate": "July 18, 1817",
        "country": "United Kingdom",
        "books": [{"title": "Emma"},{"title": "Sense and Sensibility"},{"title": "Pride and Prejudice"}],
        "book_count": 3      
    },
    {
        "_id": 16,
        "name": "Charlotte BrontÃ",
        "psuedonyms": "Currer Bell (real name: Charlotte BrontÃ)",
        "birthdate": "April 21, 1816",
        "deathdate": "March 31, 1855",
        "country": "United Kingdom",
        "books": [{"title": "Jane Eyre"}],
        "book_count": 1 
    },
    {
        "_id": 17,
        "name": "Leo Tolstoy",
        "psuedonyms": "None",
        "birthdate": "September 9, 1828",
        "deathdate": "November 20, 1910",
        "country": "Russia",
        "books": [{"title": "Anna Karenina"}],
        "book_count": 1        
    },
    {
        "_id": 18,
        "name": "Louisa May Alcott",
        "psuedonyms": "None",
        "birthdate": "November 29, 1832",
        "deathdate": "March 6, 1888",
        "country": "United States",
        "books": [{"title": "Little Women"}],
        "book_count": 1      
    },
    {
        "_id": 19,
        "name": "Oscar Wilde",
        "psuedonyms": "None",
        "birthdate": "October 16, 1854",
        "deathdate": "November 30, 1900",
        "country": "Ireland",
        "books": [{"title": "The Picture of Dorian Gray"}],
        "book_count": 1       
    },
    {
        "_id": 20,
        "name": "Charles Dickens",
        "psuedonyms": "None",
        "birthdate": "February 7, 1812",
        "deathdate": "June 9, 1870",
        "country": "United Kingdom",
        "books": [{"title": "Great Expectations"},{"title": "Oliver Twist"},{"title": "David Copperfield"},{"title": "A Tale of Two Cities"}],
        "book_count": 4      
    },
    {
        "_id": 21,
        "name": "Victor Hugo",
        "psuedonyms": "None",
        "birthdate": "February 26, 1802",
        "deathdate": "May 22, 1885",
        "country": "France",
        "books": [{"title": "Les MisÃ©rables"}],
        "book_count": 1      
    },
    {
        "_id": 22,
        "name": "Fyodor Dostoevsky",
        "psuedonyms": "None",
        "birthdate": "November 11, 1821",
        "deathdate": "February 9, 1881",
        "country": "Russia",
        "books": [{"title": "Crime and Punishment"},{"title": "The Brothers Karamazov"}],
        "book_count": 2       
    },
    {
        "_id": 23,
        "name": "George Eliot",
        "psuedonyms": "Mary Ann Evans (real name: Mary Ann Evans)",
        "birthdate": "November 22, 1819",
        "deathdate": "December 22, 1880",
        "country": "United Kingdom",
        "books": [{"title": "Middlemarch"}],
        "book_count": 1       
    },
    {
        "_id": 24,
        "name": "Nathaniel Hawthorne",
        "psuedonyms": "None",
        "birthdate": "July 4, 1804",
        "deathdate": "May 19, 1864",
        "country": "United States",
        "books": [{"title": "The Scarlet Letter"}],
        "book_count": 1      
    },
    {
        "_id": 25,
        "name": "L.M. Montgomery",
        "psuedonyms": "None",
        "birthdate": "November 30, 1874",
        "deathdate": "April 24, 1942",
        "country": "Canada",
        "books": [{"title": "Anne of Green Gables"}],
        "book_count": 1      
    },
    {
        "_id": 26,
        "name": "Mark Twain",
        "psuedonyms": "Mark Twain (real name: Samuel Langhorne Clemens)",
        "birthdate": "November 30, 1835",
        "deathdate": "April 21, 1910",
        "country": "United States",
        "books": [{"title": "The Adventures of Tom Sawyer"},{"title": "The Adventures of Huckleberry Finn"}],
        "book_count": 2
    },
    {
        "_id": 27,
        "name": "L. Frank Baum",
        "psuedonyms": "None",
        "birthdate": "May 15, 1856",
        "deathdate": "May 6, 1919",
        "country": "United States",
        "books": [{"title": "The Wonderful Wizard of Oz"}],
        "book_count": 1 
    },
    {
        "_id": 28,
        "name": "Jules Verne",
        "psuedonyms": "None",
        "birthdate": "February 8, 1828",
        "deathdate": "March 24, 1905",
        "country": "France",
        "books": [{"title": "Around the World in Eighty Days"}],
        "book_count": 1
    },
    {
        "_id": 29,
        "name": "Dante Alighieri",
        "psuedonyms": "None",
        "birthdate": "June 1, 1265",
        "deathdate": "September 13/14, 1321",
        "country": "Italy",
        "books": [{"title": "The Divine Comedy"}],
        "book_count": 1  
    },
    {
        "_id": 30,
        "name": "Miguel de Cervantes",
        "psuedonyms": "None",
        "birthdate": "September 29, 1547",
        "deathdate": "April 22, 1616",
        "country": "Spain",
        "books": [{"title": "Don Quixote"}],
        "book_count": 1        
    },
    {
        "_id": 31,
        "name": "Geoffrey Chaucer",
        "psuedonyms": "None",
        "birthdate": "Unknown",
        "deathdate": "October 25, 1400",
        "country": "England",
        "books": [{"title": "The Canterbury Tales"}],
        "book_count": 1      
    }
]

AUTHORS_REGEX = "^([A-Za-z.'\p{L}-]+ ?)+$"

AUTHORS_SCHEMA = {"$jsonSchema": {
   "title": "Author record",
   "bsonType": "object",
   "required": ["_id", "name", "books", "book_count"],
   "properties": {
      "_id": {
         "bsonType": ["int", "objectId"],
         "minimum": 0,
         "description": "primary key, author number, must be a non-negative integer, unique and is required"
      },
      "name": {
         "bsonType": "string",
         "minLength": 1,
         "maxLength": 255,
         "pattern": AUTHORS_REGEX,
         "description": "Author Name, like 'Mary Wollstonecraft Shelley'"
      },
      "psuedonyms": {
         "bsonType": "string",
         "description": "Any psuedonyms used by the author"
      },
      "birthdate": {
         "bsonType": "string",
        #  "pattern": "^(?:[0-9]{4}-[0-9]{2}-[0-9]{2}|[A-Za-z]+ [0-9]{1,2}, [0-9]{4})$",
         "description": "Author's birthdate"
      },
      "deathdate": {
         "bsonType": "string",
        #  "pattern": "^(?:[0-9]{4}-[0-9]{2}-[0-9]{2}|[A-Za-z]+ [0-9]{1,2}, [0-9]{4})$",
         "description": "Author's deathdate"
      },
      "country": {
         "bsonType": "string",
         "minLength": 1,
         "maxLength": 100,
         "description": "Author's country of origin"
      },
      "books": {
         "bsonType": "array",
         "description": "Array of books authored by the author",
         "items": {
            "bsonType": "object",
            "properties": {
               "title": {
                  "bsonType": "string",
                  "minLength": 1,
                  "maxLength": 200,
                  "description": "Title of the book"
               }
            },
            "required": ["title"]
         }
      },
      "book_count": {
         "bsonType": "int",
         "minimum": 0,
         "description": "Number of books authored by the author"
      }
   },
   "additionalProperties": False
} }

# CATEGORY: DATA SCHEMA
#
CATEGORY_REGEX = "^([A-Za-z&' ]+)$"

CATEGORIES_SCHEMA = {"$jsonSchema": {
   "title": "Category record",
   "bsonType": "object",
   "required": ["_id", "name"],
   "properties": {
      "_id": {
         "bsonType": ["int", "objectId"],
         "minimum": 0,
         "description": "primary key, category number, must be a non-negative integer, unique and is required"
      },
      "name": { # made unique with an index
         "bsonType": "string",
         "minLength": 4,
         "maxLength": 50,
         "pattern": CATEGORY_REGEX,
         "description": "Category Name, like 'Horror:Ghosts'"
      },
   },
   "additionalProperties": False
} }

CATEGORIES_DATA = [
  {"_id":  0, "name": "horror"},
  {"_id":  1, "name": "epic poetry"},
  {"_id":  2, "name": "adventure"},
  {"_id":  3, "name": "gothic"},
  {"_id":  4, "name": "science fiction"},
  {"_id":  5, "name": "detective fiction"},
  {"_id":  6, "name": "children's literature"},
  {"_id":  7, "name": "fantasy"},
  {"_id":  8, "name": "romance"},
  {"_id":  9, "name": "novel"},
  {"_id": 10, "name": "mystery"},
  {"_id": 11, "name": "poetry"},
]