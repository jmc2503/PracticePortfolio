import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import Counter from "./components/Counter";
import OnOff from "./components/OnOff";
import Timer from "./components/Timer";
import ListGroup from "./components/ListGroup";

function App() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount((prev) => prev + 1);
  };

  return (
    <>
      <Counter count={count} />
      <Timer click={handleClick}>Reset</Timer>
      <ListGroup />
    </>
  );
}

export default App;
