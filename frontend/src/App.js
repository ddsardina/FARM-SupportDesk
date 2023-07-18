import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import PrivateRoute from './componenets/PrivateRoute'
import { ToastContainer } from 'react-toastify'
import "react-toastify/dist/ReactToastify.css"
import Home from './pages/Home'
import Register from './pages/Register'
import Login from './pages/Login'
import Header from './componenets/Header'
import NewTicket from './pages/NewTicket'

function App() {
  return <>
    <Router>
      <div className='container'>
        <Header/>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/login' element={<Login />} />
          <Route path='/register' element={<Register />} />
          <Route path='/new-ticket' element={<PrivateRoute />}>
            <Route path='/new-ticket' element={<NewTicket />}/>
          </Route>
        </Routes>
      </div>
    </Router>
    <ToastContainer />
  </>
  
}

export default App;
