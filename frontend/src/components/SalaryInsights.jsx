import { useState } from "react";

import {
  Button,
  Card,
  CardContent,
  TextField,
  Typography,
} from "@mui/material";

import {
  getJobTitleAverageSalary,
  getSalaryInsights,
} from "../api/employeeApi";

function SalaryInsights() {
  const [country, setCountry] =
    useState("");

  const [jobTitle, setJobTitle] =
    useState("");

  const [data, setData] =
    useState(null);

  const fetchInsights =
    async () => {
      if (!country.trim()) {
        alert(
          "Please enter country"
        );
        return;
      }

      try {
        console.log(
          "Country:",
          country
        );

        const countryData =
          await getSalaryInsights(
            country
          );

        console.log(
          "Country API:",
          countryData
        );

        let jobAverage =
          "N/A";

        if (
          jobTitle.trim()
        ) {
          try {
            const jobData =
              await getJobTitleAverageSalary(
                country,
                jobTitle
              );

            console.log(
              "Job API:",
              jobData
            );

            jobAverage =
              jobData.average_salary;
          } catch (
            error
          ) {
            console.error(
              error
            );

            jobAverage =
              "No data found";
          }
        }

        const result = {
          ...countryData,
          jobAverage,
        };

        console.log(
          "Final Result:",
          result
        );

        setData(result);
      } catch (error) {
        console.error(
          "Error fetching insights:",
          error
        );

        alert(
          "Failed to fetch salary insights"
        );
      }
    };

  return (
    <div
      style={{
        marginTop: "40px",
      }}
    >
      <Typography
        variant="h5"
        gutterBottom
      >
        Salary Insights
      </Typography>

      <div
        style={{
          display: "flex",
          gap: "10px",
          marginBottom:
            "20px",
        }}
      >
        <TextField
          label="Country"
          value={country}
          onChange={(e) =>
            setCountry(
              e.target.value
            )
          }
        />

        <TextField
          label="Job Title"
          value={jobTitle}
          onChange={(e) =>
            setJobTitle(
              e.target.value
            )
          }
        />

        <Button
          variant="contained"
          onClick={
            fetchInsights
          }
        >
          Get Insights
        </Button>
      </div>

      {data && (
        <Card>
          <CardContent>
            <Typography>
              <strong>
                Country:
              </strong>{" "}
              {data.country}
            </Typography>

            <Typography>
              <strong>
                Min Salary:
              </strong>{" "}
              {
                data.minimum_salary
              }
            </Typography>

            <Typography>
              <strong>
                Max Salary:
              </strong>{" "}
              {
                data.maximum_salary
              }
            </Typography>

            <Typography>
  <strong>
    Country Average Salary:
  </strong>{" "}
  {data.average_salary}
</Typography>

<Typography>
  <strong>
    {jobTitle || "Selected Job"} Average Salary:
  </strong>{" "}
  {data.jobAverage}
</Typography>
          </CardContent>
        </Card>
      )}
    </div>
  );
}

export default SalaryInsights;