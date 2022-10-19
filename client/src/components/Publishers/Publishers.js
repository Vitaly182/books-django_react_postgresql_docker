import React, { useEffect, useState } from "react";
import Table from "../General/Table";
import { COLUMNS } from "./column";
import axios from "axios";

function Publishers() {
  const [data, setData] = useState([]);

  const fetchData = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/publishers/",
      );
      setData(response.data);
    } catch (err) {
        console.log(err);
    } 
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="container">
        <h1 style={{marginBottom:"50px"}}>Publishers</h1>
      <Table mockData={data} COLUMNS={COLUMNS} />
    </div>
  );
}

export default Publishers;