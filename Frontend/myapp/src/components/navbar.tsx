import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <div className="Navbar">
            <h1>Welcome to React</h1>
            
            <Link to={"/homepage"}>
                <button>Homepage</button>
            </Link>
            <Link to={"/movies"}>
                <button>Movies</button>
            </Link>
        </div>
    );
}

export default Navbar;
