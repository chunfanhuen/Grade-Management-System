import matplotlib.pyplot as plt

# 功能1：输入学生基本信息并保存到文件（至少输入10条数据）
def input_student_info():
    with open('students.txt', 'a') as f:
        while True:
            student_id = input("请输入学号 (输入0结束): ")
            if student_id == '0':
                break
            name = input("请输入姓名: ")
            gender = input("请输入性别: ")
            major_class = input("请输入专业班级: ")
            f.write(f"{student_id},{name},{gender},{major_class}\n")

# 功能2：输入学生成绩并保存到文件（至少输入10条数据）
def input_grades():
    with open('grades.txt', 'a') as f:
        while True:
            student_id = input("请输入学号 (输入0结束): ")
            if student_id == '0':
                break
            course_id = input("请输入课程编号: ")
            grade = input("请输入成绩: ")
            f.write(f"{student_id},{course_id},{grade}\n")

# 功能3：输入课程信息并保存到文件（至少输入10条数据）
def input_courses():
    with open('courses.txt', 'a') as f:
        while True:
            course_id = input("请输入课程编号 (输入0结束): ")
            if course_id == '0':
                break
            course_name = input("请输入课程名称: ")
            course_credit = input("请输入课程学分: ")
            f.write(f"{course_id},{course_name},{course_credit}\n")

# 功能4：从文件中读取学生基本信息并显示
def read_student_info():
    with open('students.txt', 'r') as f:
        for line in f:
            student_id, name, gender, major_class = line.strip().split(',')
            print(f"学号: {student_id}, 姓名: {name}, 性别: {gender}, 专业班级: {major_class}")

# 功能5：从文件中读取学生成绩并显示
def read_grades():
    with open('grades.txt', 'r') as f:
        for line in f:
            student_id, course_id, grade = line.strip().split(',')
            print(f"学号: {student_id}, 课程编号: {course_id}, 成绩: {grade}")

# 功能6：从文件中读取课程信息并显示
def read_courses():
    with open('courses.txt', 'r') as f:
        for line in f:
            course_id, course_name, course_credit = line.strip().split(',')
            print(f"课程编号: {course_id}, 课程名称: {course_name}, 课程学分: {course_credit}")

# 功能7：修改或删除学生信息
def modify_or_delete_student_info():
    student_id = input("请输入要修改或删除的学生学号: ")
    lines = []
    with open('students.txt', 'r') as f:
        for line in f:
            if line.startswith(student_id):
                action = input("输入1修改学生信息，输入2删除学生信息: ")
                if action == '1':
                    name = input("请输入新姓名: ")
                    gender = input("请输入新性别: ")
                    major_class = input("请输入新专业班级: ")
                    lines.append(f"{student_id},{name},{gender},{major_class}\n")
                # 删除学生信息则不添加到 lines
            else:
                lines.append(line)
    with open('students.txt', 'w') as f:
        f.writelines(lines)

# 功能8：修改或删除学生成绩
def modify_or_delete_grades():
    student_id = input("请输入要修改或删除成绩的学生学号: ")
    course_id = input("请输入要修改或删除的课程编号: ")
    lines = []
    with open('grades.txt', 'r') as f:
        for line in f:
            sid, cid, grade = line.strip().split(',')
            if sid == student_id and cid == course_id:
                action = input("输入1修改成绩，输入2删除成绩: ")
                if action == '1':
                    new_grade = input("请输入新成绩: ")
                    lines.append(f"{sid},{cid},{new_grade}\n")
                # 删除成绩则不添加到 lines
            else:
                lines.append(line)
    with open('grades.txt', 'w') as f:
        f.writelines(lines)

# 功能9：根据学生姓名查询成绩
def query_grades_by_name():
    name = input("请输入要查询成绩的学生姓名: ")
    student_id = None
    with open('students.txt', 'r') as f:
        for line in f:
            sid, sname, _, _ = line.strip().split(',')
            if sname == name:
                student_id = sid
                break
    if student_id:
        with open('grades.txt', 'r') as f:
            for line in f:
                sid, cid, grade = line.strip().split(',')
                if sid == student_id:
                    print(f"课程编号: {cid}, 成绩: {grade}")
    else:
        print("未找到该学生信息")

# 功能10：按专业班级查询课程最高分的学生信息
def highest_grade_by_class():
    major_class = input("请输入专业班级: ")
    course_id = input("请输入课程编号: ")
    highest_grade = -1
    student_info = None
    with open('grades.txt', 'r') as f:
        for line in f:
            sid, cid, grade = line.strip().split(',')
            if cid == course_id and int(grade) > highest_grade:
                highest_grade = int(grade)
                student_info = sid
    if student_info:
        with open('students.txt', 'r') as f:
            for line in f:
                sid, name, gender, mclass = line.strip().split(',')
                if sid == student_info and mclass == major_class:
                    print(f"学号: {sid}, 姓名: {name}, 性别: {gender}, 专业班级: {mclass}, 最高分: {highest_grade}")
                    break
    else:
        print("未找到该课程的学生信息")

# 功能11：输出某班某门课程的平均成绩
def average_grade_by_class():
    major_class = input("请输入专业班级: ")
    course_id = input("请输入课程编号: ")
    total_grade = 0
    student_count = 0
    with open('grades.txt', 'r') as f:
        for line in f:
            sid, cid, grade = line.strip().split(',')
            if cid == course_id:
                with open('students.txt', 'r') as sf:
                    for sline in sf:
                        ssid, _, _, mclass = sline.strip().split(',')
                        if ssid == sid and mclass == major_class:
                            total_grade += int(grade)
                            student_count += 1
                            break
    if student_count > 0:
        print(f"平均成绩: {total_grade / student_count:.2f}")
    else:
        print("未找到该班级的学生信息")

# 功能12：按专业班级对某门课程的成绩排序
def sort_grades_by_class():
    major_class = input("请输入专业班级: ")
    course_id = input("请输入课程编号: ")
    grades = []
    with open('grades.txt', 'r') as f:
        for line in f:
            sid, cid, grade = line.strip().split(',')
            if cid == course_id:
                with open('students.txt', 'r') as sf:
                    for sline in sf:
                        ssid, name, _, mclass = sline.strip().split(',')
                        if ssid == sid and mclass == major_class:
                            grades.append((ssid, name, int(grade)))
                            break
    grades.sort(key=lambda x: x[2], reverse=True)
    for sid, name, grade in grades:
        print(f"学号: {sid}, 姓名: {name}, 成绩: {grade}")

# 功能13：计算学生平均绩点并排序
def calculate_gpa():
    students = {}
    courses = {}
    with open('courses.txt', 'r') as f:
        for line in f:
            cid, cname, credit = line.strip().split(',')
            courses[cid] = int(credit)
    with open('grades.txt', 'r') as f:
        for line in f:
            sid, cid, grade = line.strip().split(',')
            if sid not in students:
                students[sid] = []
            students[sid].append((int(grade), courses[cid]))
    gpa_list = []
    with open('students.txt', 'r') as f:
        for line in f:
            sid, name, _, mclass = line.strip().split(',')
            if sid in students:
                total_points = sum(grade * credit for grade, credit in students[sid])
                total_credits = sum(credit for _, credit in students[sid])
                gpa = total_points / total_credits
                gpa_list.append((sid, name, gpa, mclass))
    gpa_list.sort(key=lambda x: x[2], reverse=True)
    for sid, name, gpa, mclass in gpa_list:
        print(f"学号: {sid}, 姓名: {name}, 平均绩点: {gpa:.2f}, 专业班级: {mclass}")

# 功能14：绘制课程成绩的柱状图
def plot_course_grades():
    course_id = input("请输入课程编号: ")
    grades = []
    with open('grades.txt', 'r') as f:
        for line in f:
            sid, cid, grade = line.strip().split(',')
            if cid == course_id:
                grades.append(int(grade))
    plt.bar(range(len(grades)), grades)
    plt.xlabel('学生')
    plt.ylabel('成绩')
    plt.title('课程成绩分布图')
    plt.show()

# 功能15：绘制学生成绩的柱状图
def plot_student_grades():
    student_id = input("请输入学生学号: ")
    grades = []
    with open('grades.txt', 'r') as f:
        for line in f:
            sid, cid, grade = line.strip().split(',')
            if sid == student_id:
                grades.append((cid, int(grade)))
    grades.sort(key=lambda x: x[0])
    plt.bar([g[0] for g in grades], [g[1] for g in grades])
    plt.xlabel('课程编号')
    plt.ylabel('成绩')
    plt.title('学生成绩分布图')
    plt.show()

# 功能入口
def main():
    while True:
        print("\n1. 输入学生基本信息")
        print("2. 输入学生成绩")
        print("3. 输入课程信息")
        print("4. 显示学生基本信息")
        print("5. 显示学生成绩")
        print("6. 显示课程信息")
        print("7. 修改或删除学生信息")
        print("8. 修改或删除学生成绩")
        print("9. 查询学生成绩")
        print("10. 查询课程最高分学生信息")
        print("11. 输出课程平均成绩")
        print("12. 对课程成绩排序")
        print("13. 计算并排序学生平均绩点")
        print("14. 绘制课程成绩柱状图")
        print("15. 绘制学生成绩柱状图")
        print("0. 退出")
        choice = input("请输入功能编号: ")
        if choice == '1':
            input_student_info()
        elif choice == '2':
            input_grades()
        elif choice == '3':
            input_courses()
        elif choice == '4':
            read_student_info()
        elif choice == '5':
            read_grades()
        elif choice == '6':
            read_courses()
        elif choice == '7':
            modify_or_delete_student_info()
        elif choice == '8':
            modify_or_delete_grades()
        elif choice == '9':
            query_grades_by_name()
        elif choice == '10':
            highest_grade_by_class()
        elif choice == '11':
            average_grade_by_class()
        elif choice == '12':
            sort_grades_by_class()
        elif choice == '13':
            calculate_gpa()
        elif choice == '14':
            plot_course_grades()
        elif choice == '15':
            plot_student_grades()
        elif choice == '0':
            break
        else:
            print("无效的选择，请重新输入")

if __name__ == "__main__":
    main()
