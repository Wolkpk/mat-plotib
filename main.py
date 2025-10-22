import matpotlib.pyplot as plt

students_names=["sanjay","Rahul","Karan","Wasim","Ramesh","Ajay","Sartaj","Priya"]
students_marks=[35,50,20,45,25,40,25,40]

marks_prec = []
for x in students_marks:
    res = (x/50)*100
    marks_prec.append(res)

print(marks_prec)

def line_chart():
    plt.plot(students_names,students_marks , marker="D", ms=14, mec="blue", linestyle="dotted", color="blue", linewidth=5)
    plt.title("student marks graph")
    plt.xlabel("stdent names")
    plt.ylabel("student marks")
    plt.show()

line_chart()

def bar_chart():
    plt.bar(students_names,marks_prec )
    plt.title("student persentage graph")
    plt.xlabel("stdent names")
    plt.ylabel("student persentage")
    plt.show()

bar_chart()