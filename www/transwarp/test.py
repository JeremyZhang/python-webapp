import db

db.create_engine(user='root', password='19900416', database='mysql', host='127.0.0.1', port=3306)
print db.select("select * from user")
