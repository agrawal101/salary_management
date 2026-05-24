import EmployeeTable
from "./components/EmployeeTable";

import SalaryInsights
from "./components/SalaryInsights";

function App() {
  return (
    <div
      style={{
        padding: "30px",
        maxWidth: "1200px",
        margin: "0 auto",
      }}
    >
      <h1
  style={{
    textAlign: "center",
    marginBottom: "30px",
  }}
>
  Employee Salary Management
</h1>

      <EmployeeTable />

      <SalaryInsights />
    </div>
  );
}

export default App;