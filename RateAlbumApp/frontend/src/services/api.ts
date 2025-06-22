

// export const fetchPopularAlbums = async () => {
//     const response = await fetch(
//         "https://corsproxy.io/?" +
//         encodeURIComponent("https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/albums.json")
//     );    
//     const data = await response.json();
//     return data.feed.results;
// };

export const searchAlbums = async (query : string) => {
    const response = await fetch(`https://itunes.apple.com/search?term=${encodeURIComponent(query)}&entity=album&limit=25`)
    const data = await response.json();
    return data.results;
}