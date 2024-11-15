from logic.vacation_logic import VacationLogic
from models.vacation_model import VacationModel
from flask import request, session
from models.client_error import ValidationError, ResourceNotFoundError
from utils.date_handler import DateHandler

class VacationFacade:
# initiating the logic field in this class 
    def __init__(self):
        self.logic = VacationLogic()

    def get_all_vacations(self):
        all_vacations =  self.logic.get_vacations_info()
        # changing date format: yyyy-mm-dd -> dd.mm.yyyy
        formatted_vacations = list(map(DateHandler.handle_vacation_dates, all_vacations))
        return formatted_vacations
    
    def get_one_vacation(self, id):
        vacation = self.logic.get_one_vacation(id)
        if not vacation:
            raise ResourceNotFoundError(id)
        return vacation

    def get_all_countries(self):
        return self.logic.get_all_countries()

# handling insert vacation    
    def add_vacation(self):
        country = request.form.get("country") 
        description = request.form.get("description")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        price = request.form.get("price") 
        image = request.files["image"]  
        vacation = VacationModel(None, country, description, start_date, end_date, price, image)
        error = vacation.validate_insert()
        if error: raise ValidationError(error)
        country_id = self.logic.get_country_id(country)
        self.logic.insert_vacation(country_id, description, start_date, end_date, price, image)

# handling updating vacation    
    def update_vacation(self):
        vacation_id = request.form.get("id")
        country = request.form.get("country") 
        description = request.form.get("description")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        price = request.form.get("price") 
        image = request.files["image"]  
        vacation = VacationModel(vacation_id, country, description, start_date, end_date, price, image)
        error = vacation.validate_update()
        if error: raise ValidationError(error, vacation)
        country_id = self.logic.get_country_id(country)
        self.logic.update_vacation(country_id, description, start_date, end_date, price, image, vacation_id)

# getting vacation ids which the current logged in user liked
    def get_liked_vacations_ids(self):
        user = session.get("current_user")
        user_id = user["user_id"]
        liked_vacations_ids = self.logic.get_liked_vacations_ids(user_id)
        ids = [id["vacation_id"] for id in liked_vacations_ids]
        return ids     

    def delete_vacation(self, id):
        self.logic.delete_vacation(id)

# closing    
    def close(self):
        self.logic.close()