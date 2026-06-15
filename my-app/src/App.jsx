import {num} from "./Home.jsx"
import Home from "./Home.jsx"

import "./MyCss.css"

const name="Ram";


function App() {
  return (
    <>
      <h1>Hello My name is : {name}</h1>
    </>
  )
}
{/*

NOTE :- React is a  Combination of  html+js
---------------------------------------------------------------------
react component Structure :-
----------------------------
function ComponentName(){
  return(
    <>
    
    </> 
  );
}  
  
export default ComponentName;

=====================================================================
Component.jsx 
1. Component always imported  in App.jsx
*/}
export default App