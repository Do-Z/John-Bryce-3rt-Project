import css from "./UserMenu.module.css";
import { UserModel } from "../../../Models/UserModel"
import { AppState } from "../../../Redux/state"
import { NavLink, useNavigate } from "react-router-dom";
import { userService } from "../../../Services/UserService";
import { notify } from "../../../Utils/Notify";
import { useSelector } from "react-redux";

export function UserMenu(): JSX.Element {
    const user = useSelector<AppState, UserModel>(store => store.user);
    console.log(user)
    const navigate = useNavigate();
    function logout(){
        userService.logout();
        notify.success("Bye bye")
        navigate("/home")
    }
    return (
        <div className={css.UserMenu}>
            {
                !user && <div>
                    Hello, Guest! |&nbsp;
                    <NavLink to="/login">Login</NavLink>
                </div>
            }
            {
                user && <div>
                        Hello, {user.first_name} {user.last_name} ! |&nbsp;
                        <NavLink to="" onClick={logout}>Logout</NavLink>
                    </div>
            }
        </div>
    );
}
