import matplotlib.pyplot as plt
import pandas as pd


def plotting(df):

    plt.figure(figsize=(12, 6))  
    df.T.plot(kind='line', marker='o')  
    plt.title('Yearly Data for Selected Countries (2000-2022)')
    plt.xlabel('Year')
    plt.ylabel('GDP (USD Billion)')
    plt.legend(title='Country')
    plt.grid()
    plt.xticks(rotation=45)  
    plt.tight_layout()  
    plt.show()