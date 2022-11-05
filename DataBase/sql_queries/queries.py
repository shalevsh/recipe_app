INSERT_INTO_DAIRY = """INSERT INTO dairy(ingredient_name) VALUES(%s)"""

INSERT_INTO_GLUTEN = """INSERT INTO gluten(ingredient_name) VALUES(%s)"""

SELECT_FROM_DAIRY = """SELECT * FROM dairy WHERE ingredient_name LIKE %s"""

SELECT_FROM_GLUTEN = """SELECT * FROM gluten WHERE ingredient_name LIKE %s"""