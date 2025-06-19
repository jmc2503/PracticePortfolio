import { useState } from "react";
function OnOff() {
  const [flag, setFlag] = useState(false);

  const handleClick = () => {
    setFlag((prev) => !prev);
  };

  return (
    <>
      {flag ? <h1>On</h1> : <h1>Off</h1>}
      <button onClick={handleClick}>On Off</button>
    </>
  );
}

export default OnOff;
