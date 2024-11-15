from utils.dal import DAL

class AuthLogic:
    # initiating the dal field in this class
    def __init__(self):
        self.dal = DAL()

    def add_user(self, user):
        sql = "INSERT INTO users(first_name, last_name, email, password, role_id) VALUES (%s, %s, %s, %s, %s)"
        params = (user.first_name, user.last_name, user.email, user.password, user.role_id)
        result = self.dal.insert(sql, params)
        return result
    
    def is_email_taken(self, email):
        sql = "SELECT EXISTS(SELECT * FROM users WHERE email = %s) as is_taken"
        # the SQL query returning 1 if the email is taken and 0 if the email isn't taken
        result = self.dal.get_scalar(sql, (email,))
        return result["is_taken"] == 1


    # getting the logged in/registered user in order to save him in the session
    def get_user(self, email, password):
        sql = "SELECT * FROM users WHERE email= %s and password = %s"
        user = self.dal.get_scalar(sql, (email, password))
        return user

    # closing
    def close(self):
        self.dal.close()