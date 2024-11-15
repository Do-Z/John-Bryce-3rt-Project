class DateHandler:
    # formatting date as dd.mm.yyyy
    @staticmethod
    def handle_date(date):
        formatted_date = date.strftime("%d.%m.%Y")
        return formatted_date
    
    @staticmethod
    def handle_vacation_dates(vacation):
        vacation["start_date"] = DateHandler.handle_date(vacation["start_date"])
        vacation["end_date"] = DateHandler.handle_date(vacation["end_date"])
        return vacation