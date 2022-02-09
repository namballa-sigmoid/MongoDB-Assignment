# QUESTION 01 and QUESTION 02
import json
import pymongo
from bson import ObjectId
client = pymongo.MongoClient("mongodb://localhost:27017/")

print(client.list_database_names())

mflix_db = client['sample_mflix']

comments = mflix_db['comments']
movies = mflix_db['movies']
theaters = mflix_db['theaters']
users = mflix_db['users']

print(mflix_db.list_collection_names())


with open('comments.json') as comments_file:
    comments_data = comments_file.readlines()
    for comment in comments_data:
        data_doc = json.loads(comment)
        data_doc['_id'] = ObjectId(data_doc['_id']['$oid'])
        data_doc['movie_id'] = ObjectId(data_doc['movie_id']['$oid'])
        data_doc['date'] = data_doc['date']['$date']['$numberLong']
        comments.insert_one(data_doc)


with open('movies.json') as movies_file:
    movies_data = movies_file.readlines()
    for movie in movies_data:
        data_doc = json.loads(movie)
        data_doc['_id'] = ObjectId(data_doc['_id']['$oid'])
        movies.insert_one(data_doc)

with open('theaters.json') as theaters_file:
    theaters_data = theaters_file.readlines()
    for theater in theaters_data:
        data_doc = json.loads(theater)
        data_doc['_id'] = ObjectId(data_doc['_id']['$oid'])
        theaters.insert_one(data_doc)

with open('users.json') as users_file:
    users_data = users_file.readlines()
    for user in users_data:
        data_doc = json.loads(user)
        data_doc['_id'] = ObjectId(data_doc['_id']['$oid'])
        users.insert_one(data_doc)


print(mflix_db.list_collection_names())
