import { createBrowserRouter } from "react-router-dom";
import App from "../App";
import Homepage from "../pages/homepage/homepage";
import Movies from "../pages/movies/movies";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            { path: "homepage", element: <Homepage /> },
            { path: "movies", element: <Movies /> }
        ]
    }
]);
