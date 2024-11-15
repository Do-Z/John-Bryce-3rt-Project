import { useEffect, useState } from "react";
import css from "./TotalUsers.module.css";
import { TotalUsersModel } from "../../../Models/TotalUsersModel";
import { statsService } from "../../../Services/StatsService";
import { notify } from "../../../Utils/Notify";
import { useSelector } from "react-redux";
import { AppState } from "../../../Redux/state";
import { UserModel } from "../../../Models/UserModel";

export function TotalUsers(): JSX.Element {
    const [totalUsers, setTotalUsers] = useState<TotalUsersModel>();
    const user = useSelector<AppState,UserModel>(store=>store.user);
    useEffect(()=>{
        if (user){
        statsService.getTotalUsers()
        .then(totalUsersObj=>setTotalUsers(totalUsersObj))
        .catch(err=>notify.error(err));
    }
},[user])

    return (
        <div className={css.TotalUsers}>
			<p> Total Users on the Website: </p>
            <p className={css.dashboard}> {totalUsers?.total_users} </p>
        </div>
    );
}
