student_roster = [
  {
    "name": "Karina M",
    "age": 8,
    "height": 48,
    "favorite_subject": "Math",
    "favorite_animal": "Dog"
  },
  {
    "name": "Yori K",
    "age": 7,
    "height": 50,
    "favorite_subject": "Art",
    "favorite_animal": "Cat"
  },
  {
    "name": "Alex C",
    "age": 7,
    "height": 47,
    "favorite_subject": "Science",
    "favorite_animal": "Cow"
  },
  {
    "name": "Esmeralda R",
    "age": 8,
    "height": 52,
    "favorite_subject": "History",
    "favorite_animal": "Rabbit"
  },
  {
    "name": "Sandy P",
    "age": 7,
    "height": 49,
    "favorite_subject": "Recess",
    "favorite_animal": "Guinea Pig"
  },
  {
    "name": "Matthew Q",
    "age": 7,
    "height": 46,
    "favorite_subject": "Music",
    "favorite_animal": "Walrus"
  },
  {
    "name": "Trudy B",
    "age": 8,
    "height": 45,
    "favorite_subject": "Science",
    "favorite_animal": "Ladybug"
  },
  {
    "name": "Benny D",
    "age": 7,
    "height": 51,
    "favorite_subject": "Math",
    "favorite_animal": "Ant"
  },
  {
    "name": "Helena L",
    "age": 7,
    "height": 53,
    "favorite_subject": "Art",
    "favorite_animal": "Butterfly"
  },
  {
    "name": "Marisol R",
    "age": 8,
    "height": 50,
    "favorite_subject": "Math",
    "favorite_animal": "Lion"
  }
]
import itertools
class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self._sorted_alpha(student_roster)

    def _sorted_alpha(self,student_roster):
        names = []
        for student_info in student_roster:
            name = student_info["name"]
            names.append(name)
        return sorted(names)

    def seat_combo(self):
        seat_combo = list(itertools.combinations(self.sorted_names,2))
        return seat_combo

    def get_students_with_subject(self,subject):
        selected_students = []
        for student in student_roster:
            if student["favorite_subject"] == subject:
                selected_students.append((student["name"],subject))
        return selected_students

classroom = ClassroomOrganizer()
classroom_iter = iter(classroom.sorted_names)
for names in classroom_iter:
    print(names)

y = ClassroomOrganizer()
subjects = y.get_students_with_subject("Math") + y.get_students_with_subject("Science")
subcombo = list(itertools.combinations(subjects,4))
print(subcombo)


























