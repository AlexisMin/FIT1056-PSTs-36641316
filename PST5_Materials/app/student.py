from app.user import User

class StudentUser(User):
    """Represents a student, inheriting from the base User class."""
    
    def __init__(self, user_id, name, enrolled_course_ids=None):
        # Call the parent class's __init__ method using super().
        super().__init__(user_id, name)
        
        # Initialize 'enrolled_course_ids'. If a list is provided (like when 
        # loading from JSON), use it. Otherwise, start with an empty list.
        if enrolled_course_ids is not None:
            self.enrolled_course_ids = enrolled_course_ids
        else:
            self.enrolled_course_ids = []