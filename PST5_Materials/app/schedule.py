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
                
                # --- Load Students ---
                for s in data.get('students', []):
                    s_id = s.get('id') or s.get('user_id')
                    s_name = s.get('name', 'Unknown')
                    student_obj = StudentUser(user_id=s_id, name=s_name)
                    student_obj.enrolled_course_ids = s.get('enrolled_course_ids', [])
                    self.students.append(student_obj)
                    
                # --- Load Teachers ---
                for t in data.get('teachers', []):
                    t_id = t.get('id') or t.get('user_id')
                    t_name = t.get('name', 'Unknown')
                    t_spec = t.get('speciality', 'General')
                    self.teachers.append(TeacherUser(user_id=t_id, name=t_name, speciality=t_spec))
                    
                # --- Load Courses ---
                for c in data.get('courses', []):
                    self.courses.append(Course(
                        c.get('course_id', c.get('id')), 
                        c.get('name'), 
                        c.get('instrument', 'General'), 
                        c.get('teacher_id')
                    ))
                    
                # --- Load Finance Log ---
                self.finance_log = data.get('finance_log', [])
                
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        data_to_save = {
            "students": [vars(s) for s in self.students],
            "teachers": [vars(t) for t in self.teachers],
            "courses": [vars(c) for c in self.courses],
            "finance_log": self.finance_log
        }
        
        with open(self.data_path, 'w') as f:
            json.dump(data_to_save, f, indent=4)

    def create_course(self, name, instrument, teacher_id):
        """Create a new course, generate an ID, and save it."""
        course_id = len(self.courses) + 1 
        new_course = Course(course_id, name, instrument, teacher_id)
        self.courses.append(new_course)
        self._save_data()
        return new_course
    
    # ==========================================
    # PST5 FINANCE METHODS
    # ==========================================
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

    def get_payment_history(self, student_id):
        """Return all payments for a specific student."""
        return [p for p in self.finance_log if p["student_id"] == student_id]

    # ==========================================
    # PST4 ROSTER METHOD (Restored)
    # ==========================================
    def check_in(self, student_id, course_id):
        """Check a student into a course for the Daily Roster."""
        # Find the course
        course = next((c for c in self.courses if str(c.id) == str(course_id)), None)
        
        if not course:
            return False, "Course not found."
            
        # Check if they are already enrolled
        if student_id not in course.enrolled_student_ids:
            course.enrolled_student_ids.append(student_id)
            self._save_data()  # Save changes to JSON
            return True, "Student checked in successfully."
            
        return False, "Student is already checked in for this course."