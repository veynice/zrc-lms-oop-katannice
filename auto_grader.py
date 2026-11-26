class BatchGrader:
  def process_grades(self,assignment_list, student_profile):
    print(f"--- Running Auto-Grader for {student_profile.student_name} ---")

    for assignment in assignment_list:
       assignment.get_details()

       score = assignment.grade_work(student_profile.student_work)
       student_profile.add_points(score)

    print(f"\nFinal Grade Processed! Total Score: {student_profile.get_current_score()}")
