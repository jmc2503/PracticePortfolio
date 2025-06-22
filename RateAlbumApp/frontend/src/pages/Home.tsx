import { useState } from "react";
import AlbumCard from "../components/AlbumCard";
import { searchAlbums } from "../services/api";
import "../css/Home.css";

function Home() {
  const [searchQuery, setSearchQuery] = useState("");

  const [albums, setAlbums] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  // useEffect(() => {
  //   const loadPopularAlbums = async () => {
  //     try {
  //       const popularAlbums = await fetchPopularAlbums();
  //       setAlbums(popularAlbums);
  //     } catch (err) {
  //       console.log(err);
  //       setError("Failed to load popular albums");
  //     } finally {
  //       setLoading(false);
  //     }
  //   };

  //   loadPopularAlbums();
  // }, []);

  const handleSearch = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!searchQuery.trim()) {
      return;
    }
    if (loading) {
      return;
    }

    setLoading(true);
    try {
      const searchResults = await searchAlbums(searchQuery);
      setAlbums(searchResults);
      setError("");
    } catch (err) {
      console.log(err);
      setError("Failed to search albums...");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="home">
      <form onSubmit={handleSearch} className="search-form">
        <input
          type="text"
          placeholder="Search for albums"
          className="search-input"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        ></input>
        <button type="submit" className="search-button">
          Search
        </button>
      </form>
      {error && <div className="error-message">{error}</div>}
      {loading ? (
        <div className="loading">Loading...</div>
      ) : (
        <div className="albums-grid">
          {albums.map((album, index) => (
            <AlbumCard album={album} key={index} />
          ))}
        </div>
      )}
    </div>
  );
}

export default Home;
