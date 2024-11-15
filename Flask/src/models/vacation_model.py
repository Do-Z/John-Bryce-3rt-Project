from datetime import date

class VacationModel():
    # initiating the vacation object
    def __init__(self, vacation_id, country, description, start_date, end_date, price, image):
        self.vacation_id = vacation_id
        self.country = country
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.image = image

    # function for checking chronological order of dates
    @staticmethod
    def is_end_date_after_start_date(start_date, end_date):
        start_date_data = str(start_date).split('-')
        end_date_data = str(end_date).split('-')

        if start_date_data[0] > end_date_data[0]:
            return True
        if start_date_data[0] < end_date_data[0]:
            return False
        if start_date_data[1] > end_date_data[1]:
            return True
        if start_date_data[1] < end_date_data[1]:
            return False
        if start_date_data[2] >= end_date_data[2]:
            return True
        return False

    # validating info for insert a vacation
    def validate_insert(self): 
        if not self.country: return "missing country"
        if not self.description: return "missing description"
        if not self.start_date: return "missing start date"
        if not self.end_date: return "missing end date"
        if not self.price: return "missing price"
        if not self.image: return "missing image"
        if len(self.description) < 3: return "description is too short"
        if not 0 < float(self.price) <= 10000: return "price must be between 0 to 10000"
        if self.is_end_date_after_start_date(self.start_date, self.end_date): return "end date must be after start date"
        today = date.today()
        if self.is_end_date_after_start_date(today, self.start_date): return "can't use past date as start date"
        if self.is_end_date_after_start_date(today, self.end_date): return "can't use past date as end date"
        return None

    # validating info for update a vacation
    def validate_update(self):
        if not self.country: return "missing country"
        if not self.description: return "missing description"
        if not self.start_date: return "missing start date"
        if not self.end_date: return "missing end date"
        if not self.price: return "missing price"
        if len(self.description) < 3: return "description is too short"
        if not 0 < float(self.price) <= 10000: return "price must be between 0 to 10000"
        if self.is_end_date_after_start_date(self.start_date, self.end_date): return "end date must be after start date"
        return None

