import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(6, 6))
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    res = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, color="red")

    # Create second line of best fit
    res = linregress(
        x=df.loc[df["Year"] >= 2000, "Year"],
        y=df.loc[df["Year"] >= 2000, "CSIRO Adjusted Sea Level"],
    )
    x_pred = pd.Series([i for i in range(2000, 2051)])
    y_pred = res.slope * x_pred + res.intercept

    plt.plot(x_pred, y_pred, color="green")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
