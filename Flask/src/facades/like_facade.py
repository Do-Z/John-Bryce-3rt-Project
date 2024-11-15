from flask import session
from logic.like_logic import LikesLogic
from logic.vacation_logic import VacationLogic
from models.client_error import ResourceNotFoundError

class LikesFacade():
# initiating the logic field in this class 
    def __init__(self):
        self.logic = LikesLogic()
        self.vacation_logic = VacationLogic()

# function which determines whether the user liked or disliked the vacation
    def handle_like(self, vacation_id):
        if not self.vacation_logic.get_one_vacation(vacation_id): raise ResourceNotFoundError(vacation_id)
        user = session.get("current_user")
        user_id = user["user_id"]
        is_liked = self.logic.get_like(user_id, vacation_id)
        if not is_liked:
            self.logic.add_like(user_id, vacation_id)
        else: self.logic.delete_like(user_id, vacation_id)

# closing
    def close(self):
        self.logic.close()
