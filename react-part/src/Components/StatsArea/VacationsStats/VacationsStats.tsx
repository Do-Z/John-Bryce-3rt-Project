import { useEffect, useState } from "react";
import css from "./VacationsStats.module.css";
import { statsService } from "../../../Services/StatsService";
import { VacationsStatsModel } from "../../../Models/VacationsStatsModel";
import { notify } from "../../../Utils/Notify";
import { useSelector } from "react-redux";
import { AppState } from "../../../Redux/state";
import { UserModel } from "../../../Models/UserModel";
import { BarChart } from "@mui/x-charts";

export function VacationsStats(): JSX.Element {
    const [vacationsStats, setVacationsStats] = useState<VacationsStatsModel>();
    const user = useSelector<AppState, UserModel>(store => store.user);
    useEffect(() => {
        if (user) {
            statsService.getVacationsStats()
                .then(vacationsStatsObj => setVacationsStats(vacationsStatsObj))
                .catch(err => notify.error(err));
        }
    }, [user])

    return (
        <div className={css.TotalUsers}>
            <p> Vacations by Time Periods: </p>
        
        <BarChart
            xAxis={[{ 
                scaleType: 'band', 
                data: ['Past Vacations', 'Current Vacations', 'Future Vacations'],
                
            }]}
            series={[{ data: [vacationsStats?.past_vacations, vacationsStats?.on_going_vacations, vacationsStats?.future_vacations] }]}
            width={500}
            height={280}
            borderRadius={10}
            barLabel="value"
            />
        </div>
    );
    
}