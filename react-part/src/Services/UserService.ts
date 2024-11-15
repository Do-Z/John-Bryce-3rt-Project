import { jwtDecode } from "jwt-decode";
import { CredentialsModel } from "../Models/CredentialsModel";
import axios from "axios";
import { appConfig } from "../Utils/AppConfig";
import { UserModel } from "../Models/UserModel";
import { store, userActions } from "../Redux/state";

class UserService {
    public constructor(){
        //Extract token from localstorage if exist  
        const token = localStorage.getItem("token");
        //if not token do nothing 
        if (!token) return;
        const dbUser = jwtDecode<{user:UserModel}>(token).user; 
        const action = userActions.login(dbUser);
        store.dispatch(action);
    }

    public async login(credentials: CredentialsModel): Promise<void>{
        const response = await axios.post<UserModel>(appConfig.loginUrl, credentials, {withCredentials: true})
        const dbUser = response.data;
        const action = userActions.login(dbUser);
        store.dispatch(action);
    }

    public logout():void {
        //create action object for logout 
        const action = userActions.logout()
        //logout user from global state 
        store.dispatch(action); 
        //remove token from local storage 
        localStorage.removeItem("token"); 
    }
}

export const userService = new UserService();
