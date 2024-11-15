import css from "./Home.module.css";
import imageSource from "../../../Assets/Images/Bar Chart.gif"
import { useTitle } from "../../../Utils/useTitle";

export function Home(): JSX.Element {
    useTitle("Statics | Home")
    return (
        <div className={css.Home}>
            <h4>Here you can see all the data our company has to offer about our users and vacations worldwide.</h4>
            <h4>Such as likes per country, total users etc.</h4>
            <h4>It's important to mention that all the data is protected by copyrights laws.</h4>
            <img src={imageSource}></img>
        </div>
    );
}
