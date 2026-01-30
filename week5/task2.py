import json
from statistics import mean
def process(input="students.json", output="students_with_avg.json"):
    with open(input, "r", encoding="utf-8") as f:
        data = json.load(f)
    for student in data:
        grades = student.get("grades", [])
        student["average_grade"] = mean(grades) if grades else None
    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
if __name__ == "__main__":
    process()
