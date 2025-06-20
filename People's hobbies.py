import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

survey_data = pd.read_csv("young-people-survey-responses.csv")
# Set the style to "darkgrid"
sns.set_style("darkgrid")

# Set a custom color palette
color=["#39A7D0","#36ADA4"]
sns.set_palette(color)

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()

