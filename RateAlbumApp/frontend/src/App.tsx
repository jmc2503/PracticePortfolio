import "./App.css";
import NavBar from "./components/NavBar";
import Home from "./pages/Home";
import Listened from "./pages/Listened";
import AlbumPage from "./pages/AlbumPage";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <>
      <NavBar />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/listened" element={<Listened />} />
          <Route path="/album/:id" element={<AlbumPage />}></Route>
        </Routes>
      </main>
    </>
  );
}

export default App;
