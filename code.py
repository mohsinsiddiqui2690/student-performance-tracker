class Student:
    def __init__(self, name, scores):
        """
        Initialize a Student object.
        :param name: The student's name.
        :param scores: A list of integers representing scores in subjects.
        """
        self.name = name
        self.scores = scores

    def calculate_average(self):
        """
        Calculate the average of the student's scores.
        :return: The average score.
        """
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        """
        Check if the student has passed all subjects.
        :param passing_score: The minimum score required to pass a subject.
        :return: True if all scores are >= passing_score, otherwise False.
        """
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        """
        Initialize a PerformanceTracker object.
        """
        self.students = {}

    def add_student(self, name, scores):
        """
        Add a new student to the tracker.
        :param name: The student's name.
        :param scores: A list of integers representing scores in subjects.
        """
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        """
        Calculate the average score across all students.
        :return: The class average score.
        """
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):
        """
        Print each student's performance including average score and pass/fail status.
        """
        print("\nStudent Performance:")
        print("-" * 30)
        for name, student in self.students.items():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Name: {name}, Average Score: {average:.2f}, Status: {status}")


def main():
    tracker = PerformanceTracker()
    print("Welcome to the Student Performance Tracker!")
    print("Enter student data (name and scores for 3 subjects). Type 'done' to finish.")

    while True:
        name = input("\nEnter the student's name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break

        try:
            scores = list(map(int, input(f"Enter scores for {name} (3 subjects, separated by spaces): ").split()))
            if len(scores) != 3:
                raise ValueError("You must enter exactly 3 scores.")
            tracker.add_student(name, scores)
            print(f"Student '{name}' added successfully!")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    # Display class performance
    if tracker.students:
        print("\n--- Class Summary ---")
        print(f"Class Average Score: {tracker.calculate_class_average():.2f}")
        tracker.display_student_performance()
    else:
        print("No student data available to display.")

    print("\nThank you for using the tracker!")


if __name__ == "__main__":
    main()
