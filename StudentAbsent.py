import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


student_data = pd.read_csv("student-alcohol-consumption.csv")





# Create a point plot that uses color to create subgroups
sns.catplot(
    x="romantic",
    y="absences",
    data=student_data,
    kind="point",
    hue="school",
)



# Show plot
plt.show()