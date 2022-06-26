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
    pass


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    new_dict = {}
    with open(input_json_path, 'r') as input:
        new_dict = json.load(input)
    output_dict = {}
    for id, student in new_dict.items():
        for course in student["registered_courses"]:
            output_dict[course] = 0
    for course_name, students in output_dict:
        students = len(names_of_registered_students(input_json_path), course_name)
    with open(output_file_path, 'w') as output:
        for course_name, students in output_dict:
            output.write(course_name)
            output.write(" ")
            output.write(students)
            output.write("\n")

def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    new_dict = {}
    output_dict = {}
    for file in json_directory_path:
        if file.endswith(".json"):
            with open(file, 'r') as json_file:
                new_dict = json.load(json_file)
            for id, stats in new_dict:
                addition = [elem for elem in stats["lecturers"] if elem not in output_dict[stats["course_name"]]]
                output_dict[stats["course_name"]].extend(addition)
    final_dict = {}
    for course, lecturers in output_dict:
        for elem in lecturers:
            final_dict[elem] = course
    file_name = func3_output
    completeName = os.path.join(output_json_path, file_name)
    output_file = open(completeName, "w")
    json.dump(final_dict, output_file, indent = 4)
    output_file.close()


