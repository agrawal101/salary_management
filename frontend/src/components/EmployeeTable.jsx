import {
  useEffect,
  useState,
} from "react";

import {
  Button,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from "@mui/material";

import {
  deleteEmployee,
  getEmployees,
} from "../api/employeeApi";

import EmployeeForm
from "./EmployeeForm";

function EmployeeTable() {
  const [employees,
    setEmployees] =
    useState([]);

  useEffect(() => {
    fetchEmployees();
  }, []);

  const fetchEmployees =
    async () => {
      try {
        const data =
          await getEmployees();

        setEmployees(
          data
        );
      } catch (error) {
        console.error(
          error
        );
      }
    };

  const handleDelete =
    async (id) => {
      await deleteEmployee(
        id
      );

      fetchEmployees();
    };

  return (
    <>
      <EmployeeForm
        onEmployeeAdded={
          fetchEmployees
        }
      />

      <TableContainer
        component={Paper}
      >
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>
                Name
              </TableCell>

              <TableCell>
                Job Title
              </TableCell>

              <TableCell>
                Country
              </TableCell>

              <TableCell>
                Salary
              </TableCell>

              <TableCell>
                Actions
              </TableCell>
            </TableRow>
          </TableHead>

          <TableBody>
            {employees.map(
              (
                employee
              ) => (
                <TableRow
                  key={
                    employee.id
                  }
                >
                  <TableCell>
                    {
                      employee.full_name
                    }
                  </TableCell>

                  <TableCell>
                    {
                      employee.job_title
                    }
                  </TableCell>

                  <TableCell>
                    {
                      employee.country
                    }
                  </TableCell>

                  <TableCell>
                    {
                      employee.salary
                    }
                  </TableCell>

                  <TableCell>
                    <EmployeeForm
                      employeeToEdit={
                        employee
                      }
                      onEmployeeAdded={
                        fetchEmployees
                      }
                    />

                    <Button
                      color="error"
                      onClick={() =>
                        handleDelete(
                          employee.id
                        )
                      }
                    >
                      Delete
                    </Button>
                  </TableCell>
                </TableRow>
              )
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </>
  );
}

export default EmployeeTable;