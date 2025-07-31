import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { QRCodeCanvas } from "qrcode.react";

const EmployeePage = () => {
  const { code } = useParams();
  const [employee, setEmployee] = useState(null);
  const [imgError, setImgError] = useState(false);
  const [loading, setLoading] = useState(true);

  const photoUrlJpg = `/employees_photos/${code}.jpg`;
  const photoUrlPng = `/employees_photos/${code}.png`;

  useEffect(() => {
    setLoading(true);
    fetch("/merged_employees.json")
      .then((res) => res.json())
      .then((data) => {
        const emp = data.find((e) => e.code === code);
        setEmployee(emp);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching employee data:", error);
        setLoading(false);
      });
  }, [code]);

  // Function to check if course is expired
  const isCourseExpired = (expiryDate) => {
    const today = new Date();
    const expiry = new Date(expiryDate);
    return today > expiry;
  };

  // Function to format date
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  };

  if (loading) {
    return (
      <div className="loading">
        <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>⏳</div>
        <h2>Loading employee data...</h2>
      </div>
    );
  }

  if (!employee) {
    return (
      <div className="error">
        <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>❌</div>
        <h2>Employee not found or invalid code</h2>
        <p>Please check the URL and try again</p>
      </div>
    );
  }

  return (
    <div>
      {/* Header */}
      <header className="header">
        <div className="header-content">
          <div className="logo">
            {/* Company Logo - Replace src with your actual logo path */}
            <img
              src=" /pico-Logo-tran.png"
              alt="PICO Energy Logo"
              className="company-logo"
              onError={(e) => {
                // Fallback to text logo if image fails to load
                e.target.style.display = "none";
                e.target.nextSibling.style.display = "flex";
              }}
            />
          </div>
          <nav>
            <ul className="nav-menu">
              <li>
                <a href="#profile">Profile</a>
              </li>
              <li>
                <a href="#courses">Courses</a>
              </li>
              <li>
                <a href="#certificates">Certificates</a>
              </li>
            </ul>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-content">
          <div className="hero-text">
            <h1>
              Employee Profile
              <br />
              <span className="highlight">Professional Excellence</span>
            </h1>
            <p>
              Access comprehensive employee information, training records, and
              professional certifications in our integrated employee management
              system.
            </p>
          </div>
          <div className="hero-card">
            <h2>
              Welcome to <span className="pico-red">PICO Energy</span>
            </h2>
            <p>
              Our employee portal provides secure access to training records,
              certifications, and professional development information. All data
              is maintained with the highest standards of confidentiality and
              accuracy.
            </p>
          </div>
        </div>
      </section>

      {/* Main Content */}
      <main className="main-content">
        {/* Employee Profile */}
        <div className="employee-profile" id="profile">
          <div className="profile-header">
            {!imgError ? (
              <img
                src={photoUrlJpg}
                alt={employee.name}
                className="profile-photo"
                onError={(e) => {
                  if (e.target.src.endsWith(".jpg")) {
                    e.target.src = photoUrlPng;
                  } else {
                    setImgError(true);
                  }
                }}
              />
            ) : (
              <div
                className="profile-photo"
                style={{
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontSize: "3rem",
                  backgroundColor: "var(--pico-gray-light)",
                }}
              >
                👤
              </div>
            )}
            <div className="profile-info">
              <h2>{employee.name}</h2>
              <p>
                <strong>Department:</strong> {employee.department}
              </p>
              <p>
                <strong>Employee Code:</strong>{" "}
                <span className="employee-code">{employee.code}</span>
              </p>
            </div>
          </div>

          <div className="profile-body">
            {/* Certificates Section */}
            <div>
              <h3 className="section-title">Certificates & Documents</h3>
              <a
                href={`/certificates/${employee.code}.pdf`}
                target="_blank"
                rel="noopener noreferrer"
                className="certificates-link"
              >
                📄 View Certificates (PDF)
              </a>
            </div>

            {/* QR Code Section */}
            <div className="qr-section">
              <h3>Page QR Code</h3>
              <QRCodeCanvas
                value={window.location.href}
                size={200}
                style={{ margin: "1rem auto", display: "block" }}
              />
              <p style={{ marginTop: "1rem", color: "var(--pico-gray)" }}>
                Scan this QR code for quick access to this page
              </p>
            </div>
          </div>
        </div>

        {/* Courses Section */}
        <div id="courses">
          <h3 className="section-title">Training Courses</h3>
          <div style={{ overflowX: "auto" }}>
            <table className="courses-table">
              <thead>
                <tr>
                  <th>Course Name</th>
                  <th>Course Date</th>
                  <th>Expiry Date</th>
                  <th>Department</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {employee.courses.map((course, idx) => {
                  const isExpired = isCourseExpired(course.date_of_expiry);
                  return (
                    <tr key={idx}>
                      <td>
                        <strong>{course.course_name}</strong>
                      </td>
                      <td>{formatDate(course.date_of_course)}</td>
                      <td>{formatDate(course.date_of_expiry)}</td>
                      <td>{course.department}</td>
                      <td>
                        <span
                          className={
                            isExpired ? "status-expired" : "status-active"
                          }
                        >
                          {isExpired ? "Expired" : "Active"}
                        </span>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      </main>

      {/* Back to Top Button */}
      <a href="#top" className="back-to-top" title="Back to Top">
        ↑
      </a>
    </div>
  );
};

export default EmployeePage;