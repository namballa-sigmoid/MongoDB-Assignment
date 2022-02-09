
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

mflix_db = client['sample_mflix']
print(mflix_db.list_collection_names())

comments = mflix_db['comments']
movies = mflix_db['movies']
theaters = mflix_db['theaters']
users = mflix_db['users']

comments.aggregate([
    {"$group": {"_id": {"User's_name": "$name", "email_id": "$email"}, "TotalComments": {"$sum": 1}}},
    {"$sort": {"TotalComments": -1}},
    {"$limit": 10}
])

comments.aggregate([
    {"$group": {"_id": {"Movie's_name": "$movie_id"}, "TotalComments": {"$sum": 1}}},
    {"$sort": {"TotalComments": -1}},
    {"$limit": 10}
])

movies.aggregate([
    {"$project": {"title": 1, "imdb.rating": 1}},
    {"$sort": {"imdb.rating": -1}},
    {"$limit": 10}
])


movies.aggregate([
    {"$match": {"year": 1914}},
    {"$project": {"_id": 0, "title": 1, "imdb.rating": 1}},
    {"$sort": {"imdb.rating": -1}},
    {"$limit": 10}
])

movies.aggregate([
    {"$match": {"imdb.votes": {"$gt": 1000}}},
    {"$project": {"_id": 0, "imdb.votes": 1, "title": 1, "imdb.rating": 1}},
    {"$sort": {"imdb.rating": -1}},
    {"$limit": 10}
])

movies.aggregate([
    {"$match": {"title": {"$regex": "Scene"}}},
    {"$project": {"_id": 0, "title": 1, "tomatoes.viewer.rating": 1}},
    {"$sort": {"tomatoes.viewer.rating": -1}},
    {"$limit": 10}
])

movies.aggregate([
    {"$unwind": "$directors"},
    {"$group": {"_id": {"Directors": "$directors"}, "TotalMovies": {"$sum": 1}}},
    {"$sort": {"TotalMovies": -1}},
    {"$limit": 10}
])

movies.aggregate([
    {"$unwind": "$directors"},
    {"$group": {"_id": {"directors": "$directors", "year": "$year"}, "TotalMovies": {"$sum": 1}}},
    {"$sort": {"TotalMovies": -1}},
    {"$match": {"_id.year": 1911}},
    {"$project": {"_id.directors": 1, "TotalMovies": 1}},
    {"$limit": 10}
])

movies.aggregate([
    {"$unwind": "$directors"},
    {"$unwind": "$genres"},
    {"$group": {"_id": {"directors": "$directors", "genres": "$genres"}, "totalMovies": {"$sum": 1}}},
    {"$sort": {"totalMovies": -1}},
    {"$match": {"_id.genres": "Short"}},
    {"$project": {"totalMovies": 1}},
    {"$limit": 10}
])

movies.aggregate([
    {"$unwind": "$cast"},
    {"$group": {"_id": {"cast": "$cast"}, "totalMovies": {"$sum": 1}}},
    {"$sort": {"totalMovies": -1}},
    {"$limit": 10}
])

movies.aggregate([
    {"$unwind": "$cast"},
    {"$group": {"_id": {"cast": "$cast", "year": "$year"}, "totalMovies": {"$sum": 1}}},
    {"$sort": {"totalMovies": -1}},
    {"$match": {"_id.year": 1912}},
    {"$project": {"_id.year": 0}},
    {"$limit": 10}
])

movies.aggregate([
    {"$unwind": "$cast"},
    {"$unwind": "$genres"},
    {"$group": {"_id": {"cast": "$cast", "genres": "$genres"}, "totalMovies": {"$sum": 1}}},
    {"$sort": {"totalMovies": -1}},
    {"$match": {"_id.genres": 'Short'}},
    {"$limit": 10}
])

theaters.aggregate([
        {"$group": {"_id": {"city": "$location.address.city"}, "totalTheaters": {"$sum": 1}}},
        {"$sort": {"totalTheaters": -1}},
        {"$project": {"city": "$_id.city", "totalTheaters": 1}},
        {"$limit": 10}
])

