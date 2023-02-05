from mysqlconnection import connectToMySQL

class Users:
    db = 'books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)

        all_users=[]
        for item in results:
            all_users.append(cls(item))

        return all_users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (f_name, l_name, email, password, created_at, updated_at) VALUES (%(f_name)s, %(l_name)s, %(email)s, %(password)s, NOW(), NOW())"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def getOneByEmail(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET f_name = %(f_name)s, l_name = %(l_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result