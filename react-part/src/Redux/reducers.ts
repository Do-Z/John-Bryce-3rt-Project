import { PayloadAction } from "@reduxjs/toolkit";
import { UserModel } from "../Models/UserModel";
import { TotalUsersModel } from "../Models/TotalUsersModel";
import { TotalLikesModel } from "../Models/TotalLikesModel";
import { VacationsStatsModel } from "../Models/VacationsStatsModel";
import { LikesPerCountryModel } from "../Models/LikesPerCountryModel";

export function login(currentState: UserModel, action:PayloadAction<UserModel>): UserModel{
    console.log("Login reducer called:", action.payload);
    const newState = action.payload;
    return newState
}

export function logout(currentState: UserModel, action:PayloadAction<UserModel>): UserModel{
    return null
}

export function initTotalUsers(currentState: TotalUsersModel, action:PayloadAction<TotalUsersModel>): TotalUsersModel{
    const totalUsers = action.payload;
    return totalUsers
}

export function initTotalLikes(currentState: TotalLikesModel, action:PayloadAction<TotalLikesModel>): TotalLikesModel{
    const totalLikes = action.payload;
    return totalLikes
}

export function initVacationsStats(currentState: VacationsStatsModel, action:PayloadAction<VacationsStatsModel>): VacationsStatsModel{
    const vacationsStats = action.payload;
    return vacationsStats
}

export function initLikesPerCountry(currentState: LikesPerCountryModel[], action:PayloadAction<LikesPerCountryModel[]>): LikesPerCountryModel[]{
    const likesPerCountry = action.payload;
    return likesPerCountry
}