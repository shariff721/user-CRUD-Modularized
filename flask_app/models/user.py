from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    DB = "users_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = """ INSERT INTO users (first_name, last_name, email, updated_at)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW())"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result 
    
    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM users;"""
        results = connectToMySQL(cls.DB).query_db(query)
        
        all_users = []

        for user in results:
            all_users.append(cls(user))
        return all_users
    
    @classmethod
    def get_one(cls,user_id):
        query = """ SELECT * FROM users WHERE id = %(id)s """
        results = connectToMySQL(cls.DB).query_db(query,{"id":user_id})
        return cls(results[0])
    
    @classmethod
    def editUser(cls,data):
        query = """ UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
                WHERE id = %(id)s"""
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def deleteUser(cls,user_id):
        query = """ DELETE FROM users WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query, {"id":user_id})
    
    @staticmethod
    def validate_user(user):
        is_valid = True

        if len(user['first_name']) < 3:
            flash("Name must be atleat 3 characters.")
            is_valid = False

        if len(user['last_name']) < 3:
            flash("Name must be atleast 3 characters.")
            is_valid = False

        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    


    