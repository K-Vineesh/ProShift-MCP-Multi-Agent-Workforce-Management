# SmartShift MCP: Multi-Agent Collaborative Workforce Scheduling System

Automate complex workforce scheduling, leave management, and fair task assignment using a modular, agent-driven Python system inspired by the Multi-Agent Collaborative Process (MCP) architecture.

---

## 📖 Project Overview

**SmartShift MCP** is a production-grade simulation and automation tool for workforce management in dynamic environments like warehouses, logistics, or factories.  
It uses specialized agents to independently handle staff availability, optimal zone assignments, and fair allocation of unproductive days, working together under a Supervisor for full process transparency and modularity.

The project includes **ready-to-run sample data files** and **example output reports** for instant demonstration.

---

## ⚙️ Key Features

- **Multi-Agent Collaborative Process (MCP):** Each agent is responsible for a single step—absence handling, zone assignment, UP day allocation—collaborating through a supervisor orchestrator.
- **Automated Absence and Leave Management:** Workers on leave are excluded automatically, with extra staff called in as needed.
- **Dynamic Task & Zone Assignment:** Assigns available staff to the right zone/shift/task based on daily demand and workload.
- **Unproductive (UP) Day Assignment:** Fairly distributes unproductive (off) days, avoiding repeated or unfair assignments.
- **Extensive Daily Reporting:** Generates both CSV and human-readable text reports for each day.
- **Extensible Architecture:** Add new “agents” for skills, fatigue, advanced fairness, or machine learning optimizations as your process grows.

---



## 📝 Data Files

- **`workers.csv`** — List of all workers, including zone preferences, extra status, leave history, and more.
- **`leave_requests.csv`** — Records of workers who have requested leave, by worker ID and date.
- **`workload_schedule.csv`** — Daily requirements for each zone or task, including peak days (e.g., "prime day").

> All **sample data files** are included in the `data/` folder for instant testing and demonstration.

---

## 📊 Sample Output

Here’s an example of a daily assignment report (generated in both `.csv` and `.txt` formats in the `reports/` folder):


> Several **sample output reports** are already available in the `reports/` folder.

---

## 🛠️ Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/K-Vineesh/ProShift-MCP-Multi-Agent-Workforce-Management.git
    cd ProShift-MCP-Multi-Agent-Workforce-Management

    ```

2. **(Optional but recommended) Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Usage

1. Make sure your data files (`workers.csv`, `leave_requests.csv`, `workload_schedule.csv`) are in the `data/` folder.  
   *(Sample data already included for instant use!)*
2. Run the automation:
    ```bash
    python main.py
    ```
3. Find the generated assignment reports (both CSV and TXT) for each day in the `reports/` folder.

---

## 🤖 How the MCP Architecture Works

The process is modular and collaborative, mirroring real organizational structure:

- **AbsenceAgent**: Filters out workers on leave or unavailable.
- **ZoneAssignmentAgent**: Assigns available workers to each shift/zone/task, using extra staff as needed to meet demand.
- **UPAgent**: Assigns unproductive days (UP) fairly, so extra or unassigned staff have distributed time off.
- **Supervisor**: Orchestrates the workflow—invokes agents in sequence, passes results along, gathers notes, and produces all output.

Agents are completely independent and can be swapped out or enhanced without touching the rest of the code.

---

## 💡 Extending the System

- Add new agents (SkillAgent, FatigueAgent, SwapAgent, ComplianceAgent) for more advanced rules.
- Integrate with dashboards, notification systems, or HR databases for real-time feedback.
- Implement ML/AI-driven optimization or forecasting as additional agents.
- Adapt the assignment rules to your industry or site's unique needs.

---

## 📃 License

Licensed under the MIT License.

---

## 👤 Author

Vineesh Koppay  
Email: vineeshbijuselvi@gmail.com
---

**If you find this project useful, please star ⭐ or fork it!  
Feel free to open issues or submit pull requests for improvements.**

