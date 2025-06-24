import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import EmployeePage from "./pages/EmployeePage";
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/employee/:code" element={<EmployeePage />} />
        <Route path="*" element={<div>الصفحة غير موجودة</div>} />
      </Routes>
    </Router>
  );
}

export default App;
