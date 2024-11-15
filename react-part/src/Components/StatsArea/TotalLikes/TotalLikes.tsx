import { useEffect, useState } from "react";
import css from "./TotalLikes.module.css";
import { TotalLikesModel } from "../../../Models/TotalLikesModel";
import { statsService } from "../../../Services/StatsService";
import { notify } from "../../../Utils/Notify";
import { useSelector } from "react-redux";
import { AppState } from "../../../Redux/state";
import { UserModel } from "../../../Models/UserModel";

export function TotalLikes(): JSX.Element {
    const [totalLikes, setTotalLikes] = useState<TotalLikesModel>();
    const user = useSelector<AppState,UserModel>(store=>store.user);
    useEffect(()=>{
        if (user){
        statsService.getTotalLikes()
        .then(totalLikesObj=>setTotalLikes(totalLikesObj))
        .catch(err=>notify.error(err));
    }
},[user])

    return (
        <div className={css.TotalLikes}>
			<p> Total Likes on the Website: </p>
            <p className={css.dashboard}> {totalLikes?.total_likes} </p>
        </div>
    );
}
