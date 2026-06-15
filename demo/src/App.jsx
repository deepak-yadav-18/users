/*
======================================= useState Hook ========================================
React Hooks are built-in functions introduced in React 16.8 that allow you to use state and other 
React features inside functional components without writing class components.

To use useState hook we have to import it from react library.

import {useState} from "./react"

syntax:-
--------

^ const [state,setState] = useState(initialValue) ;

* state = The current value of the state variable
* setState = The updater function called to change the state value and schedule a re-render.
* initialValue: The value you want the state to start with (e.g., numbers, strings, arrays, or objects)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
================================ Even t Handling in React JS =================================
-------------------Normal JS ----------------------

<button onclick="showAlert()">click</button>

function showAlert(){
  alert("You have clicked");
}
---------------------------------------------------

-------------------React JS -----------------------
syntax:- <tagName onEventName={functionName}></tagName>

function showAlert(){
  alert("You have clicked")
}

<button onClick = {showAlert}>click</button>


ex:- 
----
onClick
onMouseEnter
onKeyDown
onSubmit
....
*/
import { useState } from "react";
import "./MyCSS.css";

function showAlert(n) {
  alert(`hello ${n}`);
}

function formsubmit(e) {
  e.preventDefault();
  console.log("submit button clicked");
}

function App() {
  let name = "Ram";

  let user_name = "";

  let [count, setCount] = useState(10);

  let [u_name , setName] = useState("");
  return (
    <>
      <h1
        style={{
          color: "Green",
          textAlign: "center",
          fontSize: "50px",
        }}
        className="h1"
      >
        Name is - {name}
      </h1>

      <button onClick={() => setCount((count += 1))} className="btn">  +  </button>
      <h1>{count}</h1>

      {/* <button onClick={showAlert} className="btn">Click</button> */}

      {/* <button onClick={()=>{alert("hello")}} className="btn">Click</button> */}

      {/*==== function with parameters =====  */}
      <button onClick={() => showAlert("Ram")} className="btn">
        Click
      </button>

      {/*<button onMouseEnter={showAlert} className="btn">Click</button> */}

      <form className="form" onSubmit={formsubmit}>
        <input
          type="text"
          name="user"
          onChange={(e) => setName(u_name = e.target.value)}
        />
        <input type="submit" />
      </form>

      <h1>Entered User name is: {u_name}</h1>
    </>
  );
}

export default App;
