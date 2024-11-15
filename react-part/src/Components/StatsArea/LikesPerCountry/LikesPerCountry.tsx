import { useEffect, useState } from "react";
import { LikesPerCountryModel } from "../../../Models/LikesPerCountryModel";
import css from "./LikesPerCountry.module.css";
import { statsService } from "../../../Services/StatsService";
import { notify } from "../../../Utils/Notify";
import { useSelector } from "react-redux";
import { AppState } from "../../../Redux/state";
import { UserModel } from "../../../Models/UserModel";
import { pieArcLabelClasses, PieChart } from "@mui/x-charts/PieChart";


export function LikesPerCountry(): JSX.Element {
    const [likesPerCountry, setLikesPerCountry] = useState<LikesPerCountryModel[]>([]);
    const user = useSelector<AppState, UserModel>(store => store.user)
    useEffect(() => {
        if (user) {
            statsService.getLikesPerCountry()
                .then(likesPerCountryArray => setLikesPerCountry(likesPerCountryArray))
                .catch(err => notify.error(err));
        }
    }, [user])

    const pieChartData = likesPerCountry.map((d, index) => ({
        id: index,
        value: d.likes,
        label: d.destination
    }));

    return (
        <div className={css.LikesPerCountry}>
            <p> Vacations by Countries: </p>
            <PieChart
                colors={['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'pink', 'brown', 'white', 'violet', 'grey']}
                series={[
                    {
                        arcLabel: (item) => `${item.value}`,
                        arcLabelMinAngle: 20,
                        arcLabelRadius: '60%',
                        data: pieChartData,
                        cx: 230
                    },
                ]}
                sx={{
                    [`& .${pieArcLabelClasses.root}`]: {
                        fontWeight: 'bold',
                    },
                }}
                width={700}
                height={250}

            />

        </div>
    );
}
