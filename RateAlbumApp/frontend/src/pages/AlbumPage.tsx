import { useParams } from "react-router-dom";
import { fetchAlbumWithTracks } from "../services/api";
import { useEffect, useState } from "react";
import type { Album } from "../services/api";
import { FaHeadphones } from "react-icons/fa";

function AlbumPage() {
  const { id } = useParams<{ id: string }>();
  const [album, setAlbum] = useState<Album | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!id) {
      setError("No album ID provided.");
      setLoading(false);
      return; // Exit early if no id
    }

    const loadSelectedAlbum = async () => {
      try {
        const results = await fetchAlbumWithTracks(id);
        setAlbum(results);
      } catch (err) {
        console.log(err);
        setError("Error getting album");
      } finally {
        setLoading(false);
      }
    };

    loadSelectedAlbum();
  }, [id]);

  if (!album || loading) return <p>Loading...</p>;

  if (error) return <p>{error}</p>;

  return (
    <div className="album-page">
      <div className="album-card">
        <div className="album-art">
          <img
            src={album.artworkUrl100.replace(/100x100/, "600x600")}
            alt={album.collectionName}
          ></img>
        </div>
        <div className="album-buttons">
          <button className="favorite-btn">❤</button>
          <button className="listened-btn">
            <FaHeadphones />
          </button>
        </div>
        <div className="album-info">
          <h2>{album.collectionName}</h2>
          <h3>{album.artistName}</h3>
          {<p>{album.releaseDate.split("-")[0]}</p>}
        </div>
      </div>
      <div className="track-list">
        {album.tracks.map((track) => (
          <li key={track.trackNumber}>
            {track.trackNumber}. {track.trackName}
          </li>
        ))}
      </div>
    </div>
  );
}

export default AlbumPage;
