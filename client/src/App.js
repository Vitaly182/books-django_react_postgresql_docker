import Navbar from "./components/Navbar/Navbar";
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Authors from "./components/Authors/Authors";
import Books from "./components/Books/Books";
import Genres from "./components/Genres/Genres";
import Publishers from "./components/Publishers/Publishers";

function App() {

  return (
    <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path="authors" element={<Authors />} exact/>
        <Route path="books" element={<Books />} exact/>
        <Route path="genres" element={<Genres />} exact/>
        <Route path="publishers" element={<Publishers />} exact/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
