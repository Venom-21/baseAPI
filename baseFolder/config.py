from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://aravindraj273:MEvmWJLh4hbCSbuE@djangoproject.c0y4lpx.mongodb.net/')
db = client['Django']
# collection = db['tblUser']
