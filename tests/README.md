# 📊 Expense Management System

![Expense Tracker Screenshot](https://github.com/pierredeveloper/expense-management-system/blob/0da8ff9745b7bcde138c1868bd977737e328afd5/expense%20management.png)

A modern, full-stack **Expense Management System** built with a **Streamlit frontend** and a **FastAPI backend**. This app allows users to easily **record, update, and analyze** their daily or monthly expenses, providing valuable insights into spending habits through clean analytics and visualizations.

---

## 📌 Key Features:

- **✅** User-Friendly Web Interface – Built using Streamlit for an interactive and intuitive experience.
- **✅** Fast & Scalable Backend – Powered by FastAPI to handle expense tracking efficiently.
- **✅** Expense Tracking – Add, update, and delete expenses seamlessly.
- **✅** Analytics & Insights – Generate expense summaries and visualize spending patterns.
- **✅** API-Driven Architecture – Allows integration with other services and applications.

---

### 🔧 Core Functionality
- **Add New Expenses**: Input expense amount, category, and description tied to a date.
- **Update Existing Records**: Modify or overwrite previously logged expenses.
- **Daily Expense View**: Retrieve and display all expenses on a selected date.

### 📊 Analytics & Insights
- **Date Range Analysis**: View expense summaries across any given date range.
- **Category Breakdown**: Detailed insight into spending distribution (e.g., Food, Transport, Entertainment).
- **Monthly Reports**: Automatically groups expenses by month for trend analysis.
- **Spending Percentages**: See how each category contributes to your total expenses.

### 🌐 API-Driven Architecture
- Full REST API built with FastAPI.
- Swagger documentation available by default at `/docs`.
- Easy integration with other tools or frontend interfaces.

### ⚡ High Performance & Scalability
- Built on FastAPI for asynchronous and high-speed backend performance.
- Modular structure with clearly separated backend and frontend logic.

### 🎨 Modern Frontend
- Built with Streamlit for an interactive and intuitive experience.
- Form-based data entry and dynamic filters.
- Real-time updates and responsive UI.

### 🧪 Testing & Maintainability
- Unit tests available for backend logic.
- Clean folder structure for scalability and ease of updates.

---

## Example Use Cases

- **✅** Personal Budgeting: Monitor daily or monthly expenses and ensure you stay within limits.
- **✅** Business Expense Tracking: Track office-related expenses, travel reimbursements, and more.
- **✅** Financial Analysis: Use percentage-based breakdowns to analyze spending behavior and cut unnecessary costs.
- **✅** Project Expense Tracking: Track costs related to a specific project or event, such as a marketing campaign, company event, or team-building activities.
- **✅** Financial Wellness for Students: Students can track daily spending and develop budgeting habits.

---

## ⚙️ Tech Stack

| Layer       | Technology            |
|-------------|------------------------|
| Frontend    | [Streamlit](https://streamlit.io)      |
| Backend     | [FastAPI](https://fastapi.tiangolo.com) |
| Database    | SQLite (via Python's `sqlite3`) |
| Testing     | [pytest](https://docs.pytest.org)       |
| API Docs    | Swagger UI (built-in with FastAPI) |
| HTTP Client | `requests` (for frontend-backend communication) |

---

## 🗂️ Project Structure

![Expense Tracker Screenshot](https://github.com/pierredeveloper/expense-management-system/blob/9b602939b7f342291982a0f48d372a7be8ecff49/project_structure.png)
---

## 🛠️ Setup Instructions

1. **Clone the repository**:
```bash
git clone https://github.com/pierredeveloper/expense-management-system.git
cd expense-management-system
```
1. **Install dependencies:**:
```commandline
pip install -r requirements.txt
```
1. **Run the FastAPI server:**:
```commandline
uvicorn server.server:app --reload
```
1. **Run the Streamlit app:**:
```commandline
streamlit run frontend/app.py
```
---

🧾 Conclusion
The Expense Management System is a comprehensive and scalable solution for tracking and analyzing 
expenses in real time. Whether you're a student managing a budget or a business professional 
monitoring company spending, or for personal budget and expenses. this tool provides the structure and flexibility to keep your finances
organized. 