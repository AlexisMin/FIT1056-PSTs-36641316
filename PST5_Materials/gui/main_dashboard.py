# gui/main_dashboard.py
import streamlit as st
from app.schedule import ScheduleManager
from gui.student_pages import show_student_management_page
from gui.roster_pages import show_roster_page
# NEW: Import the finance page we just created
from gui.finance_pages import show_finance_page

def launch():
    """Sets up the main Streamlit application window and navigation."""
    st.set_page_config(layout="wide", page_title="Music School Management System")

    # Instantiate the "brain" of our app ONCE and store it in the session state.
    if 'manager' not in st.session_state:
        st.session_state.manager = ScheduleManager()

    st.sidebar.title("MSMS Navigation")
    
    # UPDATED: Changed "Payments (stub)" to just "Payments"
    page = st.sidebar.radio("Go to", ["Student Management", "Daily Roster", "Payments"])

    # Use an if/elif block to call the correct function to render the selected page.
    if page == "Student Management":
        show_student_management_page(st.session_state.manager)
    elif page == "Daily Roster":
        show_roster_page(st.session_state.manager)
    elif page == "Payments":
        # UPDATED: Call your new finance page instead of showing the warning
        show_finance_page(st.session_state.manager)