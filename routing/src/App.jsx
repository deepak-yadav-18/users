/*
import {useState} from "react"
----------------------------------------------------------------
npm install react-router-dom
----------------------------------------------------------------
import {BrouserRouter , Routes , Route} from "react-router-dom"
import {Link} from "react-router-dom"
----------------------------------------------------------------
<BrowserRouter>
  <Link to="/">Home</Link>
  <Link to="/about">About</Link>
  <Link to="/contact">Contact</Link>

  <Routes>
    <Route url="/" element={<Home />} />
    <Route url="/about" element={<About />} />
  </Routes>
</BrowserRouter>
*/

import Routing from "./Routing.jsx"

function App() {

  return (
    <>
      <Routing />    
    </>
  )
}

export default App
