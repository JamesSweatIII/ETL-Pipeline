import pymongo
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb+srv://ds2002:UVA!1819@cluster1.enga0sb.mongodb.net/test')

# Switch to the sample_mflix database
db = client.sample_mflix

# Show dbs
print(client.list_database_names())

# Use sample_mflix
db = client['sample_mflix']

# Show collections
print(db.list_collection_names())

# Movies Collection General Queries

# Write a MongoDB query to display the total number of documents in the collection movies.
print(db.movies.count_documents({}))

# Write a MongoDB query to display any 5 documents using pretty format in the collection movies.
for movie in db.movies.find().limit(5):
    print(movie)

# Write a MongoDB query to display 5 documents sorted by “title” using pretty format in the collection movies.
for movie in db.movies.find().sort('title', pymongo.ASCENDING).limit(5):
    print(movie)

# Write a MongoDB query to display 5 documents (display only title and awards) sorted by “title” using pretty format in the collection movies.
for movie in db.movies.find({}, {'title': 1, 'awards': 1}).sort('title', pymongo.ASCENDING).limit(5):
    print(movie)

# Write a MongoDB query to display 5 documents (display only title and awards) sorted by “title” in descending order using pretty format in the collection movies.
for movie in db.movies.find({}, {'title': 1, 'awards': 1}).sort('title', pymongo.DESCENDING).limit(5):
    print(movie)

# Write a MongoDB query to display movies (display only title and awards) with most awards (number of awards in descending order).
for movie in db.movies.find({}, {'title': 1, 'awards': 1}).sort('awards.wins', pymongo.DESCENDING).limit(10):
    print(movie)

# Write a MongoDB query to display the details of the movie that won most awards.
most_awards_movie = db.movies.find_one(sort=[('awards.wins', pymongo.DESCENDING)])
print(most_awards_movie)

# $AND/$ALL Operation

# Write a MongoDB query to display any 5 movies with both the genres: “Adventure” and “Movie” in collection movies (use $all)
for movie in db.movies.find({'genres': {'$all': ['Adventure', 'Movie']}}).limit(5):
    print(movie)

# Write a MongoDB query to display any 5 movies with both the condition: genres “Adventure” and cast “Tom Hanks”.
for movie in db.movies.find({'genres': 'Adventure', 'cast': 'Tom Hanks'}).limit(5):
    print(movie)

# Aggregation

# Write a MongoDB query to display average number of awards won by a movie (use aggregate function with $avg operator).
pipeline = [
    {'$group': {'_id': None, 'avgAwards': {'$avg': '$awards.wins'}}}
]
result = list(db.movies.aggregate(pipeline))
print(result[0]['avgAwards'])

# Write a MongoDB query to display most awards won by a movie (use aggregate function with $max operator).
pipeline = [
    {'$group': {'_id': None, 'maxAwards': {'$max': '$awards.wins'}}}
]
result = list(db.movies.aggregate(pipeline))
print(result[0]['maxAwards'])


# Query to display most awards won by a movie
most_awards_movie = db.movies.aggregate([{"$group": {"_id": "$title", "maxAwards": {"$max": "$awards.wins"}}},
                                          {"$sort": {"maxAwards": -1}},
                                          {"$limit": 1}])
print("Most awards won by a movie:")
for doc in most_awards_movie:
    print(doc)

# Query to display the total number of documents in the collection movies
total_movies = db.movies.count_documents({})
print("Total number of movies:", total_movies)

# Query to display the total number of users by name in the collection movies
users = db.movies.distinct("comments.name")
num_users = len(users)
print("Total number of users:", num_users)

# Query to display any 5 documents using pretty format in the collection comments
comments = db.comments.find().limit(5)
print("Any 5 documents in the comments collection:")
for comment in comments:
    print(comment)

# Query to display 5 documents sorted by name in the collection comments
comments_by_name = db.comments.find().sort("name").limit(5)
print("5 documents sorted by name in the comments collection:")
for comment in comments_by_name:
    print(comment)

# Query to display 5 latest comments from "Megan Richards" in the collection comments
megan_comments = db.comments.find({"name": "Megan Richards"}).sort("date", -1).limit(5)
print("5 latest comments from Megan Richards in the comments collection:")
for comment in megan_comments:
    print(comment)
