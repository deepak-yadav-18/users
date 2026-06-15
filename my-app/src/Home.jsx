
import "./MyCss.css"

export const num = 100;
function Home(){
    // return <h1>This is from Home Page</h1>
    return(
        <>
            <h1>heading1</h1>
            <table border={10}>
                <tr>
                    <th>Name</th>
                    <th>Age</th>
                </tr>
                <tr>
                    <td>Ram</td>
                    <td>21</td>
                </tr>
                <tr>
                    <td>Ram</td>
                    <td>21</td>
                </tr>
                <tr>
                    <td>Ram</td>
                    <td>21</td>
                </tr>
            </table>
        </>
    );
}

export default Home