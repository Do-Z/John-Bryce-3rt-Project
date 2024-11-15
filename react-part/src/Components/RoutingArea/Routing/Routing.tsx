import { Navigate, Route, Routes } from "react-router-dom";
import { Home } from "../../HomeArea/Home/Home";
import { About } from "../../AboutArea/About/About";
import { PageNotFound } from "../PageNotFound/PageNotFound";
import { Login } from "../../UserArea/login/login";
import { StatsPage } from "../../StatsArea/StatsPage/StatsPage";

export function Routing(): JSX.Element {
    return (
        <div className={css.Routing}>
			<Routes>
                <Route path="/" element={<Navigate to="/home"/>} />
                <Route path="/home" element={<Home/>} />
                <Route path="/about" element={<About/>} />
                <Route path="/login" element={<Login/>} />
                <Route path="/stats" element={<StatsPage/>}/>
                <Route path="*" element={<PageNotFound />} />
            </Routes>
        </div>
    );
}
