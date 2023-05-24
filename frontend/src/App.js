import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StudentTable = () => {
  const [students, setStudents] = useState([]);
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    axios.get('<API_backend_URL/student>')
      .then(response => {
        setStudents(response.data);
      })
      .catch(error => {
        console.error('Error fetching student data:', error);
      });

    axios.get('<API_backend_URL/employee>')
      .then(response => {
        setEmployees(response.data);
      })
      .catch(error => {
        console.error('Error fetching employee data:', error);
      });
  }, []);

  return (
    <div style={{ backgroundColor: '#f2f2f2', padding: '20px' }}>
      <h1 style={{ color: '#333', marginBottom: '20px' }}>Student List</h1>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={tableHeaderStyle}>ID</th>
            <th style={tableHeaderStyle}>Name</th>
            <th style={tableHeaderStyle}>Age</th>
            {/* Add more table headers as needed */}
          </tr>
        </thead>
        <tbody>
          {students.map(student => (
            <tr key={student.id}>
              <td style={tableCellStyle}>{student.id}</td>
              <td style={tableCellStyle}>{student.name}</td>
              <td style={tableCellStyle}>{student.age}</td>
              {/* Add more table cells based on the data structure */}
            </tr>
          ))}
        </tbody>
      </table>

      <h1 style={{ color: '#333', marginTop: '40px', marginBottom: '20px' }}>Employee List</h1>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={tableHeaderStyle}>ID</th>
            <th style={tableHeaderStyle}>Name</th>
            <th style={tableHeaderStyle}>position</th>
            {/* Add more table headers as needed */}
          </tr>
        </thead>
        <tbody>
          {employees.map(employee => (
            <tr key={employee.id}>
              <td style={tableCellStyle}>{employee.id}</td>
              <td style={tableCellStyle}>{employee.name}</td>
              <td style={tableCellStyle}>{employee.position}</td>
              {/* Add more table cells based on the data structure */}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

const tableHeaderStyle = {
  backgroundColor: '#333',
  color: '#fff',
  padding: '10px',
  textAlign: 'left',
};

const tableCellStyle = {
  padding: '10px',
  borderBottom: '1px solid #ccc',
};

export default StudentTable;
