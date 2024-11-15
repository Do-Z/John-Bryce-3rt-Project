import { TotalUsersModel } from "../Models/TotalUsersModel";
import axios from "axios";
import { appConfig } from "../Utils/AppConfig";
import { likesPerCountryActions, store, totalLikesActions, totalUsersActions, vacationsStatsActions } from "../Redux/state";
import { TotalLikesModel } from "../Models/TotalLikesModel";
import { VacationsStatsModel } from "../Models/VacationsStatsModel";
import { LikesPerCountryModel } from "../Models/LikesPerCountryModel";

class StatsService {
	public async getTotalUsers(): Promise<TotalUsersModel>{
        const response = await axios.get<TotalUsersModel>(appConfig.totalUsersUrl, {withCredentials: true});
        const totalUsers = response.data
        store.dispatch(totalUsersActions.initTotalUsers(totalUsers))
        return totalUsers
    }

    public async getTotalLikes(): Promise<TotalLikesModel>{
        const response = await axios.get<TotalLikesModel>(appConfig.totalLikesUrl, {withCredentials: true});
        const totalLikes = response.data
        store.dispatch(totalLikesActions.initTotalLikes(totalLikes))
        return totalLikes
    }

    public async getVacationsStats(): Promise<VacationsStatsModel>{
        const response = await axios.get<VacationsStatsModel>(appConfig.statsUrl, {withCredentials: true});
        const vacationsStats = response.data
        store.dispatch(vacationsStatsActions.initVacationsStats(vacationsStats))
        return vacationsStats
    }

    public async getLikesPerCountry(): Promise<LikesPerCountryModel[]>{
        const response = await axios.get<LikesPerCountryModel[]>(appConfig.likesPerCountryUrl, {withCredentials: true});
        const likesPerCountry = response.data
        store.dispatch(likesPerCountryActions.initLikesPerCountry(likesPerCountry))
        return likesPerCountry
    }
}

export const statsService = new StatsService();
