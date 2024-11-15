import css from "./About.module.css";
import LinkedIn from "../../../Assets/Images/LinkedIn.png"
import Instagram from "../../../Assets/Images/Instagram.png"
import Threads from "../../../Assets/Images/Threads.png"
import Facebook from "../../../Assets/Images/Facebook.png"
import Tiktok from "../../../Assets/Images/Tiktok.png"
import Dor from "../../../Assets/Images/Dor.jpeg"
import { useTitle } from "../../../Utils/useTitle";

export function About(): JSX.Element {
    useTitle("Statics | About")
    return (
        <div className={css.About}>
			<h3>This Website was built by Dor Ziv.</h3>
            <p></p>
            <p>Content him:</p>
            <p></p>
            <a rel="noopener noreferrer" target="_blank" href={"https://www.linkedin.com/in/dor-ziv/"}><img src={LinkedIn}></img></a>
            <span> </span>
            <a rel="noopener noreferrer" target="_blank" href={"https://instagram.com/_dorziv_/"}><img src={Instagram}></img></a>
            <span> </span>
            <a rel="noopener noreferrer" target="_blank" href={"https://www.threads.net/"}><img src={Threads}></img></a>
            <span> </span>
            <a rel="noopener noreferrer" target="_blank" href={"https://www.facebook.com/"}><img src={Facebook}></img></a>
            <span> </span>
            <a rel="noopener noreferrer" target="_blank" href={"https://www.tiktok.com/"}><img src={Tiktok}></img></a>
            <p></p>
            <div
                className={css.image2}
                style={{ backgroundImage: `url(${Dor})` }}
            ></div>
            <h2>Dor Ziv</h2>
        </div>
    );
}

