import { useSelector } from "react-redux";
import css from "./StatsPage.module.css";
import { AppState } from "../../../Redux/state";
import { UserModel } from "../../../Models/UserModel";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
import { notify } from "../../../Utils/Notify";
import { LikesPerCountry } from "../LikesPerCountry/LikesPerCountry";
import { TotalLikes } from "../TotalLikes/TotalLikes";
import { TotalUsers } from "../TotalUsers/TotalUsers";
import { VacationsStats } from "../VacationsStats/VacationsStats";
import { useTitle } from "../../../Utils/useTitle";

export function StatsPage(): JSX.Element {
    useTitle("Statics | Stats Page")
    const user = useSelector<AppState, UserModel>(store=>store.user);
    const navigate = useNavigate();
    console.log(user)
    useEffect(()=>{
        if (!user) {
            notify.error("You are not logged in")
            navigate("/login")
        }
    },[user, navigate])

    return (
        <div className={css.StatsPage}>
			<div><TotalLikes/></div>
            <div><TotalUsers/></div>
            <div><LikesPerCountry/></div>
            <div><VacationsStats/></div>
        </div>
    );
}
