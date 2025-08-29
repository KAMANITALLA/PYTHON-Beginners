# Créé par GENERAL STORES, le 27/12/2024 en Python 3.7

"use client";
import React from "react";

function MainComponent() {
  const [display, setDisplay] = useState("0");
  const [memory, setMemory] = useState(null);

  const handleNumber = (num) => {
    setDisplay(display === "0" ? num : display + num);
  };

  const handleOperation = (operation) => {
    switch (operation) {
      case "C":
        setDisplay("0");
        setMemory(null);
        break;
      case "=":
        try {
          setDisplay(eval(display).toString());
        } catch {
          setDisplay("Error");
        }
        break;
      case "sin":
        setDisplay(Math.sin(parseFloat(display)).toString());
        break;
      case "cos":
        setDisplay(Math.cos(parseFloat(display)).toString());
        break;
      case "tan":
        setDisplay(Math.tan(parseFloat(display)).toString());
        break;
      case "sqrt":
        setDisplay(Math.sqrt(parseFloat(display)).toString());
        break;
      case "^2":
        setDisplay(Math.pow(parseFloat(display), 2).toString());
        break;
      case "log":
        setDisplay(Math.log10(parseFloat(display)).toString());
        break;
      default:
        setDisplay(display + operation);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="bg-white rounded-lg shadow-lg p-6 w-full max-w-md">
        <input
          type="text"
          value={display}
          className="w-full p-4 text-right text-2xl mb-4 bg-gray-50 rounded"
          readOnly
        />

        <div className="grid grid-cols-4 gap-2">
          <button
            onClick={() => handleOperation("sin")}
            className="bg-blue-500 text-white p-4 rounded hover:bg-blue-600"
          >
            sin
          </button>
          <button
            onClick={() => handleOperation("cos")}
            className="bg-blue-500 text-white p-4 rounded hover:bg-blue-600"
          >
            cos
          </button>
          <button
            onClick={() => handleOperation("tan")}
            className="bg-blue-500 text-white p-4 rounded hover:bg-blue-600"
          >
            tan
          </button>
          <button
            onClick={() => handleOperation("C")}
            className="bg-red-500 text-white p-4 rounded hover:bg-red-600"
          >
            C
          </button>

          <button
            onClick={() => handleOperation("sqrt")}
            className="bg-blue-500 text-white p-4 rounded hover:bg-blue-600"
          >
            √
          </button>
          <button
            onClick={() => handleOperation("^2")}
            className="bg-blue-500 text-white p-4 rounded hover:bg-blue-600"
          >
            x²
          </button>
          <button
            onClick={() => handleOperation("log")}
            className="bg-blue-500 text-white p-4 rounded hover:bg-blue-600"
          >
            log
          </button>
          <button
            onClick={() => handleOperation("/")}
            className="bg-blue-500 text-white p-4 rounded hover:bg-blue-600"
          >
            /
          </button>

          <button
            onClick={() => handleNumber("7")}
            className="bg-gray-200 p-4 rounded hover:bg-gray-300"
          >
            7
          </button>
          <button
            onClick={() => handleNumber("8")}
            className="bg-gray-200 p-4 rounded hover:bg-gray-300"
          >
            8
          </button>
          <button
            onClick={() => handleNumber("9")}
            className="bg-gray-200 p-4 rounded hover:bg-gray-300"
          >
            9
          </button>
          <button
            onClick={() => handleOperation("*")}
            className="bg-blue-500 text-white p-4 rounded hover:bg-blue-600"
          >
            ×
          </button>

          <button
            onClick={() => handleNumber("4")}
            className="bg-gray-200 p-4 rounded hover:bg-gray-300"
          >
            4
          </button>
          <button
            onClick={() => handleNumber("5")}
            className="bg-gray-200 p-4 rounded hover:bg-gray-300"
          >
            5
          </button>
          <button
            onClick={() => handleNumber("6")}
            className="bg-gray-200 p-4 rounded hover:bg-gray-300"
          >
            6
          </button>
          <button
            onClick={() => handleOperation("-")}
            className="bg-blue-500 text-white p-4 rounded hover:bg-blue-600"
          >
            -
          </button>

          <button
            onClick={() => handleNumber("1")}
            className="bg-gray-200 p-4 rounded hover:bg-gray-300"
          >
            1
          </button>
          <button
            onClick={() => handleNumber("2")}
            className="bg-gray-200 p-4 rounded hover:bg-gray-300"
          >
            2
          </button>
          <button
            onClick={() => handleNumber("3")}
            className="bg-gray-200 p-4 rounded hover:bg-gray-300"
          >
            3
          </button>
          <button
            onClick={() => handleOperation("+")}
            className="bg-blue-500 text-white p-4 rounded hover:bg-blue-600"
          >
            +
          </button>

          <button
            onClick={() => handleNumber("0")}
            className="bg-gray-200 p-4 rounded hover:bg-gray-300 col-span-2"
          >
            0
          </button>
          <button
            onClick={() => handleNumber(".")}
            className="bg-gray-200 p-4 rounded hover:bg-gray-300"
          >
            .
          </button>
          <button
            onClick={() => handleOperation("=")}
            className="bg-green-500 text-white p-4 rounded hover:bg-green-600"
          >
            =
          </button>
        </div>
      </div>
    </div>
  );
}

export default MainComponent;
