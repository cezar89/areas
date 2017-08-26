import pymongo
import pprint

from pymongo import MongoClient

client = MongoClient()

db = client.yelp

collection = db.businesses

full_list = []

venue = 'Restaurants'
city = 'Tempe'
stars = 3.0


for post in collection.find({"$and":[{"categories":{"$in":[venue]}},{"stars":{"$gte":stars}}, {"city":city}]},{"name":1,"latitude":1,"longitude":1,"_id":0,"city":1,"stars":1}).limit(1000):
	print("8888888 ")
	full_list.append("new google.maps.LatLng(" + str(post['latitude']) + ", " + str(post['longitude']) + "),")

full_list[-1] = full_list[-1][0:-1]
#print(full_list)

# close the connection to MongoDB
client.close()
