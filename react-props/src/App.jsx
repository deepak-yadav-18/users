{
  /* 
================================= props ======================================
=> props mean properties 

Properties => Behavior OR Characterstics

* these the properties which passed into the components
* It is used to make a react application reusable and dynamic

NOTE :- These are Passed By Parent Component(App.jsx) to Child Component.

Phone
  => RAM
  => color
  => Camera
  => Size

syntax:-
--------
in clild component :-
---------------------

funtion ComponentName(props){
  return(
    <>
      <h1>Message {props.propertyName1}</h1>
      <h1>Message {props.propertyName2}</h1>
    </>
  )
}
  
export default ComponentName 

*/
}

// import User from "./User.jsx";
// import Conditional from "./Conditional.jsx"

const users = [
  {
    name: "Rahul",
    source: "https://randomuser.me/api/portraits/men/1.jpg",
    info: "Web Developer",
  },
  {
    name: "Priya",
    source: "https://randomuser.me/api/portraits/women/52.jpg",
    info: "UI/UX Designer",
  },
  {
    name: "Amit",
    source: "https://randomuser.me/api/portraits/men/3.jpg",
    info: "Frontend Developer",
  },
  {
    name: "Sneha",
    source: "https://randomuser.me/api/portraits/women/4.jpg",
    info: "Backend Developer",
  },
  {
    name: "Vikram",
    source: "https://randomuser.me/api/portraits/men/5.jpg",
    info: "Full Stack Developer",
  },
  {
    name: "Anjali",
    source: "https://randomuser.me/api/portraits/women/12.jpg",
    info: "Mobile App Developer",
  },
  {
    name: "Karan",
    source: "https://randomuser.me/api/portraits/men/7.jpg",
    info: "DevOps Engineer",
  },
  {
    name: "Neha",
    source: "https://randomuser.me/api/portraits/women/8.jpg",
    info: "Software Tester",
  },
  {
    name: "Arjun",
    source: "https://randomuser.me/api/portraits/men/9.jpg",
    info: "Data Scientist",
  },
  {
    name: "Pooja",
    source: "https://randomuser.me/api/portraits/women/10.jpg",
    info: "Cloud Engineer",
  },
];

import Dashboard from "./Dashboard.jsx";
import Login from "./Login.jsx";

{/* 
function Conditional(){
    let islogin=true;
    
    if(islogin){
      // return <h1 style={{"color":"green"}}  >User is Loged In</h1>
      return <Dashboard />
    }
    else{
      // return <h1 style= {{"color":"red"}} >User is Not LogIn</h1>
      return <Login />
    }
}
*/}

// Using ternary operator

// function Conditional(){
//     let islogin=false;

//    return (islogin)?  <Dashboard /> :  <Login /> ; 
// }

// function Conditional(){
//     let islogin=false;

//    return (islogin)?  <Dashboard /> :  <Login /> ; 
// }

function WeekDay({day}){
    
    switch(day){
      case 1:
        return <h1 style={{"color":"green"}}>Monday</h1>
        break;
      case 2:
        return <h1 style={{"color":"orange"}}>Tuesday</h1>
        break;

      case 3:
        return <h1 style={{"color":"yellow"}}>Wednesday</h1>
        break;

      case 4:
        return <h1 style={{"color":"pink"}}>Thursday</h1>
        break;

      case 5:
        return <h1 style={{"color":"blue"}}>Friday</h1>
        break;

      case 6:
        return <h1 style={{"color":"aqua"}}>Saturday</h1>
        break;

      case 7:
        return <h1 style={{"color":"aquamarine"}}>Sunday</h1>
        break;

      default:
        return <h1 style={{"color":"red"}}>Invalid Day</h1>
    }
}

function App() {
  return (
    <>

      {/* ========================================== props ====================================================  */}
      
      {/* <div className="container">
        {users.map((user, index) => (
          <User name={user.name} source={user.source} info={user.info} />
        ))} 
         
      */}


        {/* <User name="jatin" source="./src/assets/code1.jpg" info="react developer" />
      <User name="Suresh" source="./src/assets/code1.jpg" info="Python developer" />
      <User name="Kanha" source="./src/assets/code1.jpg" info="AI developer" /> */}



    {/* </div> */}


    {/* =============================== conditional rendering =============================== */}
    {/* <Conditional /> */}
    
    <WeekDay day={1}/>
    <WeekDay day={2}/>
    <WeekDay day={3}/>
    <WeekDay day={4}/>
    <WeekDay day={5}/>
    <WeekDay day={6}/>
    <WeekDay day={7}/>
    <WeekDay day={9}/>
    
    </>
  );
}

export default App;
