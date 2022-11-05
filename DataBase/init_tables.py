import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipe_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")
    
def insert_to_table():
    with connection.cursor() as cursor:
         connection.commit()

def init_tables():
    pass

if __name__ == "__main__":
     init_tables()