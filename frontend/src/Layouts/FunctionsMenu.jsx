import React from "react";
import RouteItem from "../Components/RouteItem";

const FunctionsMenu = () => {
  return (
    <>
      <ul className="w-[30rem] h-full bg-black opacity-90 absolute left-0 top-24">
        <RouteItem text="Newton's Method Calculator" path="newton" />
        <RouteItem text="Derivative Calculator" path="diff" />
        <RouteItem text="Limit Calculator" path="limit" />
        <RouteItem text="Taylor Series Calculator" path="taylor"/>
        <RouteItem text="Simpson's 1/3 Rule Calculator" path="simpson"/>
        <RouteItem text="Trapezoidal Rule Calculator" path="trapezoid"/>

      </ul>
    </>
  );
};

export default FunctionsMenu;
