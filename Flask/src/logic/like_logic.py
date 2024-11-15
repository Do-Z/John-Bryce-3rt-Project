from utils.dal import DAL

class LikesLogic():
    # initiating the dal field in this class
    def __init__(self):
        self.dal = DAL()

    def add_like(self, user_id, vacation_id):
        sql = "INSERT INTO likes (user_id, vacation_id) VALUES (%s, %s)"
        params = (user_id, vacation_id)
        last_like_details = self.dal.insert(sql, params)
        return last_like_details

    # function for determining whether we need to add like or delete like    
    def get_like(self, user_id, vacation_id):
        sql = "SELECT * FROM likes WHERE user_id = %s AND vacation_id = %s"
        params = (user_id, vacation_id)
        like = self.dal.get_scalar(sql, params)
        return like
    
    def delete_like(self, user_id, vacation_id):
        sql = "DELETE FROM likes WHERE user_id = %s AND vacation_id = %s"
        params = (user_id, vacation_id)
        deleted_like = self.dal.delete(sql, params)
        return deleted_like

    # closing    
    def close(self):
        self.dal.close()