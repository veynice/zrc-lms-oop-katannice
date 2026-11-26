from abc import ABC, abstractmethod

class AcademicTask(ABC):

    def __init__(self, title, max_points):
        self.title = title
        self.max_points = max_points
        self.is_graded = False

    @abstractmethod
    def submit_work(self):
        pass

    @abstractmethod
    def grade_work(self):
        pass

    @abstractmethod
    def get_details(self):
        pass
class StudentProfile:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.__total_score = 0
        self.__max_points = 100

    def add_points(self, points_earned):
        if points_earned < 0:
            raise ValueError("Cannot add negative points!")

        if self.__total_score + points_earned > self.__max_points:
            raise ValueError("Score exceeds maximum allowed points!")

        self.__total_score += points_earned

    def get_current_score(self):
        return self.__total_score

class CoursePortal:
    def __init__(self, course_name):
        self.course_name = course_name
        self.__is_locked = False

    def lock_portal(self):
        self.__is_locked = True
        print(f"Deadline passed. Portal locked.")
        pass

    def accept_submission(self, student_name):
        if self.__is_locked == True:
            raise ValueError(f"Error: Deadline has passed. Submission rejected.")
        else:
            print(f"Submission accepted from {student_name}.")
            pass