import { Link } from "react-router-dom"
import "./Navbar.css"


const Navbar = () => {
    return (
        <nav className="navbar">
            <Link to="books" className="books">
                Books
            </Link>
            <Link to="authors" className="authors">
                Authors
            </Link>
            <Link to="genres" className="genres">
                Genres
            </Link>
            <Link to="publishers" className="publishers">
                Publishers
            </Link>
        </nav>
    )
}

export default Navbar