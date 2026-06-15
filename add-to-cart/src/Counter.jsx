import { useState } from 'react'
import './App.css'

function Counter() {
  const [count, setCount] = useState(1);
  let symbol="🗑";
  if(count==1){
    symbol="🗑";
  }
  else if(count>1){
    symbol="-"
  }
  else{
    symbol="hide";
  }

  return (
    <> 
    <h1 style={{"fontSize":"50px","textAlign":"center"}}>React Counter</h1>
    <div id='yash' style={(symbol=="-" || symbol=="🗑")?{"display":"flex"}:{"display":"none"}}>
    
    <button onClick = {()=>{setCount(count-1)}} className='btn' > {symbol} </button>  
    <h3 className='btn'>{count}</h3>
    <button onClick = {()=>{setCount(count+1)}} className='btn'> + </button>
    
    </div>
    
    </>
  )
}

export default Counter
