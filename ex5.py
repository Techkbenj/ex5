import json
import os

def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    with open(input_json_path, 'r') as file:
        dict1 = json.load(file)
    ans = []
    for student_info in dict1.values():
        if (course_name in student_info["registered_courses"]):
            ans.append(student_info["student_name"])
    return ans


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    with open(input_json_path, 'r') as input:
        new_dict = json.load(input)
    output_dict = {}
    for student in new_dict.keys():
        for course in new_dict[student]["registered_courses"]:
            if course not in output_dict.keys():
                output_dict[course] = 1
            else:
                output_dict[course] += 1
    with open(output_file_path, 'w') as output:
        for course in sorted(output_dict.keys()):
            text = "\"" + course + "\" " + str(output_dict[course]) + "\n"
            output.write(text)

def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    output_dict = {}
    for file in os.listdir(json_directory_path):
        if file.endswith(".json"):
            file_path = os.path.join(json_directory_path, file)
            with open(file_path, 'r') as input:
                new_dict = json.load(input)
            for id in new_dict.keys():
               for lecturer in new_dict[id]["lecturers"]:
                    if lecturer not in output_dict.keys():
                       output_dict[lecturer] = [new_dict[id]["course_name"]]
                    elif new_dict[id]["course_name"] not in output_dict[lecturer]:
                        output_dict[lecturer].append(new_dict[id]["course_name"])
    with open(output_json_path, "w") as output_file:
        json.dump(output_dict, output_file, indent = 4)



