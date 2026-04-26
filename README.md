# 🌿 Plant Disease Diagnosis Expert System

## 📌 Project Overview
This project is a Production System built to diagnose plant issues using **Forward Chaining** and **Backward Chaining**. The system reads from a Knowledge Base (`rules.txt`) and a Fact Base (`facts.txt`) to reach a goal.

## 🚀 Requirements
- [x] Parse `rules.txt` and `facts.txt` (No hard-coding!)
- [x] Forward Chaining from scratch
- [x] Backward Chaining from scratch
- [x] Print facts at every cycle

## 🛠 How to Run
1. Clone the repo: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the system: `python src/main.py`

## 📖 System Logic
The system evaluates rules such as:
- **Numerical:** `diameter > 10`
- **Logical:** `IF ... OR ... THEN ...`
- **Standard:** `IF A AND B THEN C`