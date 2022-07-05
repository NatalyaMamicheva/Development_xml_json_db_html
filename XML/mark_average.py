import xml.etree.cElementTree as ET
from xml.dom import minidom as minidom
from statistics import mean


def student_average(filename):
    global root
    doc = minidom.parse(file=filename)
    node = doc.documentElement
    subjects = doc.getElementsByTagName("subject")
    students = doc.getElementsByTagName("student")
    marks = []
    stud = []
    d = []
    for subject in subjects:
        markObj = subject.getElementsByTagName("mark")[0]
        marks.append(markObj)
    for student in students:
        studentObj = student.getElementsByTagName("subject")[0]
        stud.append(studentObj)
    for mark in marks:
        nodes = mark.childNodes
        for node in nodes:
            d.append(float(node.data))
            tree = ET.ElementTree(file=filename)
            root = tree.getroot()
    stop = 5
    res = [d[i:i + stop] for i in range(0, len(d), stop)]
    i = 1
    while i < (len(res) + 2):
        for it in root.iter(f"average{i - 1}"):
            average = str(mean(res[i - 2]))
            it.text = average
        i += 1

    tree = ET.ElementTree(root)
    with open("average.xml", "wb") as f:
        tree.write(f, "UTF-8")
        print("Значение средней оценки у каждого студента рассчитано!")


if __name__ == "__main__":
    student_average("student_list.xml")
