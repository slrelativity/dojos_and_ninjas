from flask_app import database
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM dojos;
        """

        results = connectToMySQL(database).query_db(query)
        dojo_list = []
        for row in results:
            new_dojo = cls(row)
            dojo_list.append(new_dojo)
        return dojo_list
    
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL(database).query_db(query,data)
        return result
    
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(database).query_db(query,data)
        return cls(result[0])


    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(database).query_db(query,data)