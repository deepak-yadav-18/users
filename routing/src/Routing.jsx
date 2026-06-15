/*

We use routing to create single page applications(SPA). when we click any link our entire page will not reload. 
=> change will reflect on that component.
Routing is used to link different react components.

To work with routing we have to install :- "npm install react-router-dom" (inside the terminal)

syntax:-
---------
import {BrowserRouter , Routes , Route} from "react-router-dom"


Here are the simple definitions for the four main tools you just imported:
*<BrowserRouter>: The engine that connects your app to the browser's URL bar.
*<Routes>: The switchboard that looks at the current URL and decides which page to display.
*<Route />: The map entry that pairs a specific web path (like /about) to a specific component.
*<Link>: The clickable button that changes the URL instantly without reloading the page.
*<NavLink> is a special version of <Link> that knows when it is active. 
           It automatically adds an active class to the clicked link so you can style it differently 
           (like changing its color) to show users which page they are currently viewing
*/
import {Routes , Route ,NavLink} from "react-router-dom"

import Home from "./pages/Home.jsx"
import Contact from "./pages/Contact.jsx"
import About from "./pages/About.jsx"
import Gallery from "./pages/Gallery.jsx"
function Routing() {

  return (
    <>
    <h1>This is Our App.jsx File </h1>
    <br />
    {/* (condition) ? true statement : false statement; */}
      <nav>
        <NavLink  to="/" className={(isActive)=>{isActive ?"active":"notActive"}}>Home</NavLink>
        <NavLink  to="/about">About</NavLink>
        <NavLink  to="/contact">Contact</NavLink>
        <NavLink  to="/Gallery">Gallery</NavLink>
      </nav>

    {/* ===================================================================================== */}
      
        <Routes>
            <Route path="/" element={<Home />}>Home</Route>
            <Route path="/about" element={<About />}>About</Route>
            <Route path="/contact" element={<Contact />}>Contact</Route>
            <Route path="/Gallery" element={<Gallery />}>Gallery</Route>
        </Routes>
    </>
  )
}

export default Routing
