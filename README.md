
---

## Data Files

- `workers.csv`: List of all warehouse workers, their status, zone preference, extra status, and history.
- `leave_requests.csv`: List of worker leave requests (worker_id, date).
- `workload_schedule.csv`: Per-day workforce needs (number of workers required per zone, prime day flag, etc.).

> **Sample data files are provided. Update or expand as needed for your scenario.**

---

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/K-Vineesh/warehouse_automation.git
    cd warehouse_automation
    ```

2. **(Optional but recommended) Create a virtual environment**
    ```bash
    python -m venv venv
    # Activate:
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. Place your data files (`workers.csv`, `leave_requests.csv`, `workload_schedule.csv`) in the `data/` folder.
2. Run the automation:
    ```bash
    python main.py
    ```
3. Reports (CSV and TXT) will be generated in the `reports/` folder for each day in your workload schedule.

---

## MCP (Multi-Agent Collaborative Process) Explained

This project uses a true **MCP architecture**, where:

- Each agent (AbsenceAgent, ZoneAssignmentAgent, UPAgent) handles a specialized process step.
- The Supervisor orchestrates the overall workflow, invoking each agent in order and collecting results.
- Agents communicate by passing structured data, making the system flexible, testable, and easy to extend (add new agents for more rules, smarter logic, etc.).
- Example: To add fatigue management or worker skill matching, simply add a new agent and call it from the Supervisor.

---

## Extending the System

- Add new agents for more complex rules (e.g., SkillAgent, FatigueAgent, SwapAgent).
- Integrate with dashboards or notification services for real-time feedback.
- Add fairness checks or machine-learning components for optimization.
- Adjust the assignment logic as needed for your workflow.

---

## Example Report (Human-Readable)

