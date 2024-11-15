def process_data(string_data):
    result = {}
    for string in string_data:
        name, age, *courses = string.split(',')
        result[name] = {'age': int(age), 'courses': courses}

    return result

def average_age(data):
    result = 0
    for v in data.values():
        result += v['age']

    return result / len(data)

def courses(data):
    result = set()
    for v in data.values():
        for course in v['courses']:
            result.add(course)

    return result

def most_common_courses(data):
    course_count = {}
    max_count = 0
    for v in data.values():
        for course in v['courses']:
            course_count[course] = course_count.get(course, 0) + 1
            current_count = course_count[course]
            if current_count > max_count:
                max_count = current_count

    return {k for k,v in course_count.items() if v == max_count}