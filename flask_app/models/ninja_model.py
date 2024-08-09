from flask_app import database
from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]


    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM ninjas;
        """

        results = connectToMySQL(database).query_db(query)
        ninjas_list = []
        for row in results:
            new_ninjas = cls(row)
            ninjas_list.append(new_ninjas)
        return ninjas_list
    
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name,last_name,age) VALUES (%(first_name)s,%(last_name)s,%(age)s);"
        result = connectToMySQL(database).query_db(query,data)
        return result
    
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(database).query_db(query,data)
        return cls(result[0])


    #@classmethod
    #def update(cls,data):
    #   query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,age=%(age)s,updated_at=NOW() WHERE id = %(id)s;"
    #    return connectToMySQL(database).query_db(query,data)
