import './App.css'

import Nav from './components/Nav'
import About from './components/About'
import Logo from './components/Logo'
import Posts from './components/Posts'
import NavSearchContainer from './components/NavSearchContainer'
import NavIcons from './components/NavIcons'

import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

const App = () => {
  const [confessions, setConfessions] = useState([])
  
  useEffect(
    () => {
      const fetchConfessions = async () => {
        const url = 'https://letsconfess.herokuapp.com/api/confessions/'
        const response = await fetch(url)
        const data = await response.json()
        await setConfessions(data)
        console.log(confessions)
      }
      fetchConfessions()
    }, []
  )

  return (
    <div>
      <div className="navigation">
          <Logo />
          <NavSearchContainer />
          <NavIcons />
      </div>
      <br />
      <div className="container">
      <div className='mt-5 row'>
        <section className='col-lg-8'>
          <Posts confessions={confessions} />
        </section>
        <section className='col-lg-4'>

        </section>
      </div>
      </div>
      
    </div>

  )
}

// function App() {
//   return (
//     <Router>
//       <div className="App">
//         <Nav />
//         <Switch>
//           <Route path='/' exact component={Home}/>
//           <Route path='/about' component={About}/>
//           <Route path='/shop' component={Shop}/>
//         </Switch>
//       </div>
//     </Router>
//   );
// }

// const Home = () => {
//   return (
//     <div>
//       <h1>Home</h1>
//     </div>
//   )
// }

export default App;
