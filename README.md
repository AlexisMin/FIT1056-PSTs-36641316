# FIT1056 - Music School Management System (MSMS)

**Student Name:** Min Htut Hein  
**Student ID:** 36641316  
**Unit:** FIT1056 - Introduction to Software Engineering  
**Assignment:** Problem Solving Tasks (PST) 1–5

---

## 📖 Project Overview

This repository contains the complete implementation of the Music School Management System (MSMS). The application has evolved from a simple script into a robust, object-oriented application with a Graphical User Interface (GUI), automated quality assurance tests, and full financial tracking.

This final iteration (PST5) focuses on the **Quality & Finance Gate**, ensuring the application is "crash-proof" and adding critical business tools.

## ✨ PST5 Key Features

- **Finance Engine (`app/schedule.py`):** Tracks payments using a `finance_log`. Includes methods to `record_payment`, retrieve a student's `get_payment_history`, and `export_report` to CSV.
- **Finance GUI (`gui/finance_pages.py`):** A Streamlit interface with tabs to securely record new payments, view payment history, and export financial reports.
- **Admin Utilities (`app/admin_utils.py`):**
  - `init_logger()`: Logs important business events (like payments and app launches) to `msms.log`.
  - `backup_data()`: Automatically creates timestamped backups of the `msms.json` data file to prevent data loss.
- **Automated Testing (`tests/test_schedule_manager.py`):** A `pytest` suite using temporary data fixtures to verify finance logic and error handling without corrupting real data.

---

## 🚀 How to Run the Application

**Prerequisites:** Ensure you have Python installed and your virtual environment set up.

### Step 1: Navigate to the Repository Root

Open your terminal and navigate to the root folder of this repository:

\`\`\`bash
cd FIT1056-PSTs-36641316
\`\`\`

### Step 2: Activate the Virtual Environment

For Windows:

\`\`\`bash
.venv\Scripts\activate
\`\`\`

For macOS/Linux:

\`\`\`bash
source .venv/bin/activate
\`\`\`

### Step 3: Navigate into the Application Folder

\`\`\`bash
cd PST5_Materials
\`\`\`

### Step 4: Launch the Streamlit Application

\`\`\`bash
streamlit run main.py
\`\`\`

### Step 5: View the Application

A browser window should automatically open at:

`http://localhost:8501`

Use the sidebar to navigate to the **Payments** page to test the finance features.

---

## 🧪 How to Run the Automated Tests

To verify the backend logic and ensure the application is crash-proof, run the test suite using `pytest`.

### Step 1: Open the Terminal in the Application Folder

Ensure you are in the `PST5_Materials` folder in your terminal.

### Step 2: Run the Tests

\`\`\`bash
python -m pytest -v
\`\`\`

### Step 3: Check the Test Results

The expected output should indicate that all three tests passed:

\`\`\`text
tests/test_schedule_manager.py::test_create_course PASSED
tests/test_schedule_manager.py::test_record_payment_and_history PASSED
tests/test_schedule_manager.py::test_get_payment_history_no_results PASSED

======================== 3 passed in 0.15s ========================
\`\`\`

*Note: The output above is an example. Actual execution time and test results may differ.*

---

## 🧠 Design Choices & Assumptions

### 1. Crash-Proofing

The `record_payment` method validates that the student exists, the amount is greater than zero, and the payment method is valid.

If the input is invalid, the method raises a `ValueError`. The GUI catches the exception and displays a friendly error message using `st.error`, preventing the application from crashing.

### 2. Persistence

The `finance_log` is saved directly into `msms.json` alongside the student and course data to keep the storage simple and atomic.

### 3. Testing

Tests use `tmp_path` fixtures to create isolated JSON files. This ensures that running the test suite does not corrupt the actual application database.

---

## 📤 How to Commit and Push the README

After saving `README.md`, open your terminal and navigate to the repository root.

If you are still inside `PST5_Materials`, run:

\`\`\`bash
cd ..
\`\`\`

Then stage, commit, and push the README:

\`\`\`bash
git add README.md
git commit -m "docs: comprehensive README with run and test instructions"
git push origin individual
\`\`\`

---

## ✅ How to Preview the README in VS Code

1. Create or open `README.md` in the root folder of your repository.
2. Paste the Markdown content into the file.
3. Save the file using `Ctrl + S`.
4. In VS Code, open the Markdown preview by pressing `Ctrl + Shift + V`, or click the **Open Preview to the Side** icon in the editor.
5. Check that the headings, bullet points, code blocks, and sections display correctly.

Once everything looks correct, commit and push your changes to your Git repository.