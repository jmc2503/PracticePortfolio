import "../css/AlbumCard.css";
import { FaHeadphones } from "react-icons/fa";
import { Link } from "react-router-dom";

interface AlbumCardProps {
  album: {
    collectionId: number;
    collectionName: string;
    artistName: string;
    releaseDate: string;
    artworkUrl100: string;
  };
}

function AlbumCard({ album }: AlbumCardProps) {
  return (
    <div className="album-card">
      <Link to={`/album/${album.collectionId}`}>
        <div className="album-art">
          <img
            src={album.artworkUrl100.replace(/100x100/, "600x600")}
            alt={album.collectionName}
          ></img>
        </div>
      </Link>
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
  );
}

export default AlbumCard;
