sns.scatterplot(
    data=divorce,
    x="woman_age_marriage",
    y="income_woman",
    hue="education_woman"
)
plt.show()
