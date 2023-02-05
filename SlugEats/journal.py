import matplotlib.pyplot as plt
import numpy as np

# Labels for macro pie chart
macro_names = ['Protein (25-40%)', 'Carbohydrates (35-55%)', 'Fats (25-40%)']
# Colors for sections on pie chart
macro_colors = ['#DC6037', '#50403B', '#DDA63B']


def create_pie_chart(days_protein, days_carbs, days_fats):
    """Creates pie chart used to display macronutrient intake for the day"""
    # Stores the amount of macros consumed in an array
    macros = np.array([days_protein, days_carbs, days_fats])
    # Takes array and puts it into a pie chart, labels, adds color, and shows what percent of your caloric intake comes
    # from which macro
    plt.pie(macros, labels=macro_names, colors=macro_colors, autopct='%1.2f%%')
    # Adds title to pie chart
    plt.title('Today\'s Macronutrients (Suggested Amount)')
    # Display chart
    plt.show()

# Calculated daily limit for caffeine based on body weight
def calculate_caffeine_limit(weight_in_lbs):
    caffeine_limit = (int(weight_in_lbs)*3)/100
    return caffeine_limit


# Creates underlying bar graph for daily limit of micronutrient
def create_daily_limit_graph(nutrient, daily_limit):  # Creates underlying bar graph for daily limit of micronutrient
    nutrient_label = np.array(nutrient)
    limit = np.array(daily_limit)
    plt.figure(figsize=(6, 6))
    plt.barh(nutrient_label, limit, height=.1)
    plt.show()

# Creates overlay bar graph to show how much of a nutrient has been consumed today in comparison to daily limit
def create_bar_graph(nutrient, days_micronutrient):
    nutrient_amount = np.array(days_micronutrient)
    nutrient_name = np.array(nutrient)
    plt.figure(figsize=(6, 6))
    plt.barh(nutrient_name, nutrient_amount, height=.1)
    plt.show()


