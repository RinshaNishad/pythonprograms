import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="animal"
)

cursor=db.cursor()
query="""
insert into pets(age,gender,breed,location,price) values(7,'male','breed5','tvm',27000)


"""
cursor.execute(query)

db.commit() #save changes