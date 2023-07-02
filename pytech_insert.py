from pymongo import MongoClient
url = "mongodb+srv://rloos:Cybr410@project42.q8nksg5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students

fred = {
    "first_name" : "Fred",
    "last_name" : "Jones",
    "student_id" : "1007"
}

anthony = {
    "first_name" : "Anthony",
    "last_name" : "Kiedis",
    "student_id" : "1008"
}

john = {
    "first_name" : "John",
    "last_name" : "Frusciante",
    "student_id" : "1009"
}

student1 = students.insert_one(fred).inserted_id
student2 = students.insert_one(anthony).inserted_id
student3 = students.insert_one(john).inserted_id

print("--INSERT STATEMENTS--")
print("Inserted student record " + fred["first_name"] + " " + fred["last_name"] + " into the students collection with document_id" + str(student1))
print("Inserted student record " + anthony["first_name"] + " " + anthony["last_name"] + " into the student collection with document_id" + str(student2))
print("Inserted student record " + john["first_name"] + " " + john["last_name"] + " into the student collection with document_id" + str(student3))
