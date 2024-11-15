import { NavLink } from "react-router-dom";
import css from "./Menu.module.css";
import { useSelector } from "react-redux";
import { AppState } from "../../../Redux/state";
import { UserModel } from "../../../Models/UserModel";

export function Menu(): JSX.Element {
    const user = useSelector<AppState, UserModel>(store=>store.user)
    return (
        <div className={css.Menu}>
			<NavLink to="/home">Home</NavLink>
            <NavLink to="/about">About</NavLink>
            {
                !user && <NavLink to="/login">Login</NavLink>
            }
            {
                user && <NavLink to="/stats">Stats</NavLink>
            }
        </div>
    );
}
