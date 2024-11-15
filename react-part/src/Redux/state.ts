import { configureStore, createSlice } from "@reduxjs/toolkit";
import { UserModel } from "../Models/UserModel"
import { initLikesPerCountry, initTotalLikes, initTotalUsers, initVacationsStats, login, logout } from "./reducers";
import { TotalUsersModel } from "../Models/TotalUsersModel";
import { TotalLikesModel } from "../Models/TotalLikesModel";
import { VacationsStatsModel } from "../Models/VacationsStatsModel";
import { LikesPerCountryModel } from "../Models/LikesPerCountryModel";

export type AppState = {
    user: UserModel;
    totalUsers: TotalUsersModel;
    totalLikes: TotalLikesModel;
    vacationsStats: VacationsStatsModel;
    likesPerCountry: LikesPerCountryModel[];
};

const userSlice = createSlice({
    name: "user",
    initialState: null,
    reducers: { login, logout }
})

const totalUsersSlice = createSlice({
    name: "totalUsers",
    initialState: null,
    reducers: { initTotalUsers }
})

const totalLikesSlice = createSlice({
    name: "totalLikes",
    initialState: null,
    reducers: { initTotalLikes }
})

const vacationsStatsSlice = createSlice({
    name: "vacationsStats",
    initialState: null,
    reducers: { initVacationsStats }
})

const likesPerCountrySlice = createSlice({
    name: "likesPerCountry",
    initialState: null,
    reducers: { initLikesPerCountry }
})

export const userActions = userSlice.actions;
export const totalUsersActions = totalUsersSlice.actions;
export const totalLikesActions = totalLikesSlice.actions;
export const vacationsStatsActions = vacationsStatsSlice.actions;
export const likesPerCountryActions = likesPerCountrySlice.actions;

export const store = configureStore<AppState>({
    reducer: {
        user: userSlice.reducer,
        totalUsers: totalUsersSlice.reducer,
        totalLikes: totalLikesSlice.reducer,
        vacationsStats: vacationsStatsSlice.reducer,
        likesPerCountry: likesPerCountrySlice.reducer
    }
})