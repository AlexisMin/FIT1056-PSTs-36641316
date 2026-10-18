# gui/finance_pages.py
import streamlit as st
import pandas as pd

def show_finance_page(manager):
    """Renders the UI for all financial operations."""
    st.header("💰 Finance & Payments")

    # Create a dictionary mapping student names to IDs for easy lookup
    # (Assuming manager.students contains objects with .name and .id)
    student_list = {s.name: s.id for s in manager.students}

    if not student_list:
        st.warning("No students found in the system. Please add a student first.")
        return

    # Use tabs to keep the interface clean
    tab1, tab2 = st.tabs(["Record Payment", "Payment History & Export"])

    # ==========================================
    # TAB 1: Record a Payment
    # ==========================================
    with tab1:
        st.subheader("Record New Payment")
        
        # clear_on_submit=True resets the form after a successful payment
        with st.form("payment_form", clear_on_submit=True):
            selected_student_name = st.selectbox("Select Student", list(student_list.keys()))
            
            amount = st.number_input("Payment Amount ($)", min_value=0.01, step=1.0, format="%.2f")
            
            method = st.selectbox("Payment Method", ["Credit Card", "Bank Transfer", "Cash"])
            
            submitted = st.form_submit_button("Record Payment")
            
            if submitted:
                student_id = student_list[selected_student_name]
                try:
                    # Call the backend method we wrote in schedule.py
                    manager.record_payment(student_id, amount, method)
                    st.success(f"✅ Successfully recorded ${amount:.2f} payment for {selected_student_name}.")
                except Exception as e:
                    st.error(f"❌ Error recording payment: {e}")

    # ==========================================
    # TAB 2: View History & Export
    # ==========================================
    with tab2:
        st.subheader("View Student Payment History")
        
        history_student_name = st.selectbox("Select Student to View History", list(student_list.keys()))
        
        if history_student_name:
            history_student_id = student_list[history_student_name]
            history = manager.get_payment_history(history_student_id)
            
            if history:
                # Convert the list of dictionaries to a pandas DataFrame
                df = pd.DataFrame(history)
                st.dataframe(df, use_container_width=True)
                
                # Calculate and display total
                total_paid = sum(item['amount'] for item in history)
                st.info(f"**Total Paid:** ${total_paid:.2f}")
            else:
                st.info("This student has no payment history yet.")
                
        st.divider()
        
        # --- Export Section (Fragment 5.1 requirement) ---
        st.subheader("Export Data")
        if st.button("📥 Export All Payments to CSV"):
            try:
                # Ensure the data folder exists so the export doesn't crash
                import os
                os.makedirs("data", exist_ok=True)
                
                out_path = "data/payment_report.csv"
                manager.export_report("payments", out_path)
                st.success(f"✅ Report exported successfully to `{out_path}`")
            except Exception as e:
                st.error(f"❌ Failed to export report: {e}")