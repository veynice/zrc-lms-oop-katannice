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
            print(f"Error: Deadline has passed. Submission rejected.")
        else:
            print(f"Submission accepted from {student_name}.")
        pass
