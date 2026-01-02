import matplotlib.pyplot as plt

# Student Data
std_names = ["Sanjay", "Rahul", "Karan", "Ramesh", "Ajay", "Priya"]
std_marks = [35, 50, 20, 45, 25, 40]

# Calculate percentage (assuming total marks = 50)
marks_perc = [(marks / 50) * 100 for marks in std_marks]

# Line chart for raw marks
def marks_line_chart():
    plt.plot(std_names, std_marks, marker = 'o', linestyle = '-', color = 'blue')
    plt.title("Students Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Marks out of 50")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Bar chart for percentage
def percentage_bar_chart():
    plt.bar(std_names, marks_perc, color = 'green')
    plt.title("Students Percentage Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()

# Run both charts
marks_line_chart()
percentage_bar_chart()