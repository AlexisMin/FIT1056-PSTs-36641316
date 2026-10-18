import json
from app.student import StudentUser
from app.teacher import TeacherUser, Course

class ScheduleManager:
    """The main controller for all business logic and data handling."""
    
    def __init__(self, data_path="data/msms.json"):
        self.data_path = data_path
        self.students = []
        self.teachers = []
        self.courses = []
        self.finance_log = []  
        self.next_lesson_id = 1
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                
                # Load Students
                for s in data.get('students', []):
                    self.students.append(StudentUser(**s))
                    
                # Load Teachers
                for t in data.get('teachers', []):
                    self.teachers.append(TeacherUser(**t))
                    
                # Load Courses
                for c in data.get('courses', []):
                    self.courses.append(Course(**c))
                    
                # Load Finance Log (NEW for PST5)
                self.finance_log = data.get('finance_log', [])
                
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")
    
    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        # Convert objects to dictionaries. We use vars() which turns an object into a dict.
        data_to_save = {
            "students": [vars(s) for s in self.students],
            "teachers": [vars(t) for t in self.teachers],
            "courses": [vars(c) for c in self.courses],
            "finance_log": self.finance_log  # <-- Save finance log (NEW for PST5)
        }
        
        with open(self.data_path, 'w') as f:
            json.dump(data_to_save, f, indent=4)

    def create_course(self, name, instrument, teacher_id):
        """Create a new course, generate an ID, and save it."""
        # Automatically generate an ID based on how many courses exist
        course_id = len(self.courses) + 1 
        
        # Now we pass all 4 arguments to match your Course class
        new_course = Course(course_id, name, instrument, teacher_id)
        
        self.courses.append(new_course)
        self._save_data()
        return new_course
    
    # PST5 Payment Sector
    # record payment
    def record_payment(self, student_id, amount, method):
        """Record a payment from a student."""
        payment = {
            "student_id": student_id,
            "amount": float(amount),
            "method": method
        }
        self.finance_log.append(payment)
        self._save_data()
        return payment

    # get payment history
    def get_payment_history(self, student_id):
        """Return all payments for a specific student."""
        return [p for p in self.finance_log if p["student_id"] == student_id]