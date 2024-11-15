import { useForm } from "react-hook-form";
import css from "./login.module.css";
import { CredentialsModel } from "../../../Models/CredentialsModel";
import { useNavigate } from "react-router-dom";
import { userService } from "../../../Services/UserService";
import { notify } from "../../../Utils/Notify";
import { useTitle } from "../../../Utils/useTitle";

export function Login(): JSX.Element {
    useTitle("Statics | Log in")
    const {register, handleSubmit} = useForm<CredentialsModel>()
    const navigate = useNavigate()
    async function send(credentials: CredentialsModel){
        try{
            await userService.login(credentials);
            notify.success("Welcome Back!")
            navigate("/home")
            }
        catch(err:any){
            notify.error(err)
        }
    }
    return (
        <div className={css.login}>
            <form onSubmit={handleSubmit(send)}>
                <label> Email: </label>
                <input type="email"{...register("email")} required></input>
                <label> Password: </label>
                <input type="password"{...register("password")} required></input>
                <button>Login</button>
            </form>
        </div >
    );
}
