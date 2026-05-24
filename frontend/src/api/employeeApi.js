import axios from "axios";

const API_BASE_URL =
  "http://localhost:8000";

export const getEmployees =
  async () => {
    const response =
      await axios.get(
        `${API_BASE_URL}/employees?page=1&size=10`
      );

    return response.data;
  };

export const createEmployee =
  async (employeeData) => {
    const response =
      await axios.post(
        `${API_BASE_URL}/employees`,
        employeeData
      );

    return response.data;
  };

export const updateEmployee =
  async (
    employeeId,
    employeeData
  ) => {
    const response =
      await axios.put(
        `${API_BASE_URL}/employees/${employeeId}`,
        employeeData
      );

    return response.data;
  };

export const deleteEmployee =
  async (employeeId) => {
    await axios.delete(
      `${API_BASE_URL}/employees/${employeeId}`
    );
  };

export const getSalaryInsights =
  async (country) => {
    const response =
      await axios.get(
        `${API_BASE_URL}/salary-insights/country/${country}`
      );

    return response.data;
  };

export const getJobTitleAverageSalary =
  async (
    country,
    jobTitle
  ) => {
    const response =
      await axios.get(
        `${API_BASE_URL}/salary-insights/job-title`,
        {
          params: {
            country,
            job_title:
              jobTitle,
          },
        }
      );

    return response.data;
  };