function ListGroup() {
  const movies = [
    { name: "Fortnite", year: "2024" },
    { name: "Minecraft", year: "2024" },
    { name: "Oo", year: "2024" },
  ];

  return (
    <>
      {movies.map((movie) => (
        <div>
          <h1>{movie.name}</h1>
          <h2>{movie.year}</h2>
        </div>
      ))}
    </>
  );
}

export default ListGroup;
