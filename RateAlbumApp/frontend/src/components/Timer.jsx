import { useEffect, useState } from "react";

function Timer({ children, click }) {
  const [time, setTime] = useState(10);

  useEffect(() => {
    if (time === 0) return;

    const interval = setInterval(() => {
      setTime((prev) => prev - 1);
    }, 1000);

    return () => clearInterval(interval);
  }, [time]);

  const reset = () => {
    setTime(10);
  };

  return (
    <>
      <h1>{time}</h1>
      <button
        onClick={() => {
          reset();
          click();
        }}
      >
        {children}
      </button>
    </>
  );
}

export default Timer;
