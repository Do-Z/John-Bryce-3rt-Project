from utils.dal import DAL
from utils.image_handler import ImageHandler

class VacationLogic:
    # initiating the dal field in this class
    def __init__(self):
        self.dal = DAL()

    def get_one_vacation(self, id):
        sql = "SELECT * FROM vacations WHERE vacation_id = %s"
        params = (id,)
        result = self.dal.get_scalar(sql, params)
        return result

    def get_all_vacations(self):
        sql = """
        SELECT V.*,
        C.country_name FROM vacations AS V LEFT JOIN countries as C
        ON V.country_id = C.country_id
        ORDER BY start_date
        """
        result = self.dal.get_table(sql)
        return result

    # getting table of vacations with country names and likes count for each vacation    
    def get_vacations_info(self):
        sql = """
        SELECT DISTINCT
            V.*,
                COUNT(L.vacation_id) AS likes_count,
                C.country_name
            FROM vacations as V LEFT JOIN countries AS C
            ON V.country_id = C.country_id
            LEFT JOIN likes as L
            ON V.vacation_id = L.vacation_id
            GROUP BY V.vacation_id
            ORDER BY V.start_date
        """
        all_vacations = self.dal.get_table(sql)
        return all_vacations
    
    def get_all_countries(self):
        sql = "SELECT country_name FROM countries"
        all_countries = self.dal.get_table(sql)
        return all_countries
    
    def get_country_id(self, country):
        sql = "SELECT country_id FROM countries WHERE country_name = %s"
        params = (country, )
        country_id = self.dal.get_scalar(sql, params)
        return country_id["country_id"]

    # insert vacation + handling its image
    def insert_vacation(self, country_id, description, start_date, end_date, price, image):
        image = ImageHandler.save_image(image)
        sql = "INSERT INTO vacations (country_id, description, start_date, end_date, price, image) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (country_id, description, start_date, end_date, price, image)
        new_vacation_id = self.dal.insert(sql, params)
        return new_vacation_id

    # update vacation + handling its image if exists   
    def update_vacation(self, country_id, description, start_date, end_date, price, image, vacation_id):
        old_image_name = self.get_old_image_name(vacation_id)
        image_name = ImageHandler.update_image(old_image_name, image)
        sql = "UPDATE vacations SET country_id = %s, description = %s, start_date = %s, end_date = %s, price = %s, image = %s WHERE vacation_id = %s"
        params = (country_id, description, start_date, end_date, price, image_name, vacation_id)
        self.dal.update(sql, params)
        
    def get_vacation(self, vacation_id):
        sql = "SELECT * FROM vacations WHERE vacation_id = %s"
        params = (vacation_id,)
        vacation = self.dal.get_scalar(sql, params)
        return vacation

    # delete the vacation and the image from DB    
    def delete_vacation(self, vacation_id):
        image_name = self.get_old_image_name(vacation_id)
        ImageHandler.delete_image(image_name)
        sql = "DELETE FROM vacations WHERE vacation_id = %s"
        params = (vacation_id,)
        row_count = self.dal.delete(sql, params)
        return row_count

    # get the old image name in order to delete it
    def get_old_image_name(self, vacation_id):
        sql = "SELECT image FROM vacations WHERE vacation_id = %s"
        params = (vacation_id,)
        result = self.dal.get_scalar(sql, params)
        return result["image"]
  
    def get_liked_vacations_ids(self, user_id):
        sql = "SELECT vacation_id FROM likes WHERE user_id = %s"
        params = (user_id, )
        result = self.dal.get_table(sql, params)
        return result

    #closing
    def close(self):
        self.dal.close()