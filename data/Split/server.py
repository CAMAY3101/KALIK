from pymongo import MongoClient
client = MongoClient(
    "mongodb+srv://kalikTeam:NietosDeGauss@cluster0.uhbfdme.mongodb.net/?retryWrites=true&w=majority")
db = client.test