export interface Album {
  collectionId: number;
  collectionName: string;
  artistName: string;
  artworkUrl100: string;
  releaseDate: string;
  tracks: Track[]
}

export interface Track{
    trackId: number;
    trackName: string;
    trackNumber: number;
    previewUrl: string;
    kind: string;
}

export const searchAlbums = async (query : string) => {
    const response = await fetch(`https://itunes.apple.com/search?term=${encodeURIComponent(query)}&entity=album&limit=25`)
    const data = await response.json();
    return data.results;
}

export async function fetchAlbumWithTracks(id: string): Promise<Album> {
  const res = await fetch(`https://itunes.apple.com/lookup?id=${id}&entity=song`);
  const data = await res.json();

  if (!data.results || data.results.length < 2) {
    throw new Error("No album or tracks found");
  }

  const albumInfo = data.results[0];
  const tracks = data.results
    .filter((item: any) => item.wrapperType === "track" && item.kind === "song")
    .map((track: any) => ({
      trackId: track.trackId,
      trackName: track.trackName,
      trackNumber: track.trackNumber,
      previewUrl: track.previewUrl,
      kind: track.kind,
    }));

  return {
    collectionId: albumInfo.collectionId,
    collectionName: albumInfo.collectionName,
    artistName: albumInfo.artistName,
    artworkUrl100: albumInfo.artworkUrl100,
    releaseDate: albumInfo.releaseDate,
    tracks,
  };
}