import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { QRCodeCanvas } from "qrcode.react";

const EmployeePage = () => {
  const { code } = useParams();
  const [employee, setEmployee] = useState(null);

  useEffect(() => {
    fetch("/merged_employees.json")
      .then((res) => res.json())
      .then((data) => {
        const emp = data.find((e) => e.code === code);
        setEmployee(emp);
      });
  }, [code]);

  if (!employee) return <div>Employee not found or invalid code.</div>;

  return (
    <div style={{ direction: "ltr", textAlign: "left", margin: 40 }}>
      <h2>Employee Information</h2>
      <p><b>Name:</b> {employee.name}</p>
      <p><b>Department:</b> {employee.department}</p>
      <p><b>Employee Code:</b> {employee.code}</p>
      <p>
        certificates:{" "}
        <a
          href={`/certificates/${employee.code}.pdf`}
          target="_blank"
          rel="noopener noreferrer"
        >
          certificates.pdf
        </a>
      </p>
      <div style={{ marginTop: 20, marginBottom: 20 }}>
        <QRCodeCanvas value={window.location.href} />
        <div>QR code for this page</div>
      </div>
      <h3>Courses</h3>
      <table border="1" cellPadding="8" style={{ borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th>Course Name</th>
            <th>Date of Course</th>
            <th>Date of Expiry</th>
            <th>Department</th>
          </tr>
        </thead>
        <tbody>
          {employee.courses.map((course, idx) => (
            <tr key={idx}>
              <td>{course.course_name}</td>
              <td>{course.date_of_course}</td>
              <td>{course.date_of_expiry}</td>
              <td>{course.department}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EmployeePage;