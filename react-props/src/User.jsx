import "./MyCSS.css"

// function User(props){
//     return (
//         <>
//             <div className="box">
//                 <h1>Name of user is : {props.name}</h1>
//                 <img src={props.source} alt="Image is loading..." className="image" /> {/* This is self closing tag */}
//                 <br />
//                 <h3>{props.info}</h3>
//             </div>
//         </>
//     )
// }

function User({name,source,info}){
    return (
        <>
            <div className="box">
                <h1>Name of user is : {name}</h1>
                <img src={source} alt="Image is loading..." className="image" /> {/* This is self closing tag */}
                <br />
                <h3>{info}</h3>
            </div>
        </>
    )
}

export default User;