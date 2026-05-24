import { useEffect, useState }
from "react";

import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  TextField,
} from "@mui/material";

import {
  createEmployee,
  updateEmployee,
} from "../api/employeeApi";

function EmployeeForm({
  onEmployeeAdded,
  employeeToEdit,
}) {
  const [open, setOpen] =
    useState(false);

  const [employee, setEmployee] =
    useState({
      full_name: "",
      job_title: "",
      country: "",
      salary: "",
    });

  useEffect(() => {
    if (employeeToEdit) {
      setEmployee(
        employeeToEdit
      );
    }
  }, [employeeToEdit]);

  const handleChange = (
    event
  ) => {
    setEmployee({
      ...employee,
      [event.target.name]:
        event.target.value,
    });
  };

  const handleSubmit =
    async () => {
      try {
        const payload = {
          ...employee,
          salary: Number(
            employee.salary
          ),
        };

        if (
          employeeToEdit
        ) {
          await updateEmployee(
            employee.id,
            payload
          );
        } else {
          await createEmployee(
            payload
          );
        }

        onEmployeeAdded();
        alert("Employee saved successfully");
        setOpen(false);

        setEmployee({
          full_name: "",
          job_title: "",
          country: "",
          salary: "",
        });
      } catch (error) {
        console.error(
          error
        );
      }
    };

  return (
    <>
      <Button
        variant="contained"
        onClick={() =>
          setOpen(true)
        }
        style={{
          marginBottom:
            "20px",
        }}
      >
        {employeeToEdit
          ? "Edit"
          : "Add Employee"}
      </Button>

      <Dialog
        open={open}
        onClose={() =>
          setOpen(false)
        }
      >
        <DialogTitle>
          {employeeToEdit
            ? "Edit Employee"
            : "Add Employee"}
        </DialogTitle>

        <DialogContent>
          <TextField
            fullWidth
            margin="dense"
            label="Full Name"
            name="full_name"
            value={
              employee.full_name
            }
            onChange={
              handleChange
            }
          />

          <TextField
            fullWidth
            margin="dense"
            label="Job Title"
            name="job_title"
            value={
              employee.job_title
            }
            onChange={
              handleChange
            }
          />

          <TextField
            fullWidth
            margin="dense"
            label="Country"
            name="country"
            value={
              employee.country
            }
            onChange={
              handleChange
            }
          />

          <TextField
            fullWidth
            margin="dense"
            type="number"
            label="Salary"
            name="salary"
            value={
              employee.salary
            }
            onChange={
              handleChange
            }
          />
        </DialogContent>

        <DialogActions>
          <Button
            onClick={() =>
              setOpen(false)
            }
          >
            Cancel
          </Button>

          <Button
            variant="contained"
            onClick={
              handleSubmit
            }
          >
            Save
          </Button>
        </DialogActions>
      </Dialog>
    </>
  );
}

export default EmployeeForm;