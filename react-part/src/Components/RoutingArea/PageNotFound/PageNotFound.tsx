import css from "./PageNotFound.module.css";
import Plane from "../../../Assets/Images/plane-crash.png"
import { useTitle } from "../../../Utils/useTitle";

export function PageNotFound(): JSX.Element {
    useTitle("Statics | 404")
    return (
        <div className={css.PageNotFound}>
            <a rel="noopener noreferrer" href={"/home"}><img src={Plane}></img></a>
            <h2> Seems like you've reached an unknown territory 🙁 </h2>
            <h4> click on the image above to go back to the home page </h4>
        </div>
    );
}
