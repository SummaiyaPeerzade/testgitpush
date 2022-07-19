import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:affan786@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"summaiya",
    "email":"summaiyatouqeer@gmail.com",
    "surname":"Peerzade"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
