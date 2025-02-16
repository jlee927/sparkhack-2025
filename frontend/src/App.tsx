import './App.css'
import Home from './pages/Home'
import Setup from './pages/Setup';
import Interview from './pages/Interview';
import Dictaphone from './pages/Dictaphone';
import { BrowserRouter, Route, Routes } from "react-router-dom";

const App = () => {
  return (
    <BrowserRouter>
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/setup" element={<Setup />} />
          <Route path="/interview" element={<Interview />} />
        </Routes>
      </main>
    </BrowserRouter>
  )
}

export default App
