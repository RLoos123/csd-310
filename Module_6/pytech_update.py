from pymongo import MongoClient

url = "mongodb+srv://rloos:Cybr410@project42.q8nksg5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

pytech = client.pytech
students = pytech.students

docs = students.find()

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print()

# update student_id 1007
students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

# find student_id 1007
doc = students.find_one({"student_id": "1007"})

print("-- DISPLAYING STUDENT DOCUMENT 1007 --")

print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")
print()

print("End of program, press any key to continue...")
