import csv
import numpy as np
import matplotlib.pyplot as plt

csv_file_path = 'wealth-distribution-2025-05-30-15-23-26.csv'

def gini_coefficient(wealth_list):
    wealth_list = np.array(wealth_list)
    total_wealth = wealth_list.sum()
    wealth_list = np.sort(wealth_list)
    cumulative_wealth = np.cumsum(wealth_list) / total_wealth
    cumulative_percentage = np.linspace(0, 1, len(wealth_list))
    s1 = 0
    s2 = 0
    for i in range(0, len(wealth_list)):
        s1 += np.abs(cumulative_percentage[i] - cumulative_wealth[i])
        s2 += np.abs(cumulative_percentage[i])
    gini = s1/s2
    return gini

def plot_lorenz_curve(wealth_list):
    wealth_list = np.array(wealth_list)
    total_wealth = wealth_list.sum()
    wealth_list = np.sort(wealth_list)
    cumulative_wealth = np.cumsum(wealth_list) / total_wealth
    cumulative_percentage = np.linspace(0, 1, len(wealth_list))

    plt.figure(figsize=(8, 6))
    plt.plot(cumulative_percentage, cumulative_wealth, label='Lorenz Curve', marker='o')
    plt.plot([0, 1], [0, 1], color='r', linestyle='--', label='Equality Line')
    plt.fill_between(cumulative_percentage, cumulative_percentage, cumulative_wealth, color='skyblue', alpha=0.5)
    plt.xlabel('Cumulative % of Population')
    plt.ylabel('Cumulative % of Wealth')
    plt.title('Lorenz Curve')
    plt.legend()
    plt.grid(True)
    # plt.show()

def plot_gini_indices(gini_indices):
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(gini_indices)+1), gini_indices, marker='o', color='b', linestyle='-')
    plt.xlabel('Time')
    plt.ylabel('Gini')
    plt.title('Gini-Index v. Time')
    plt.ylim(0, 1)  # 设置 y 轴范围
    plt.grid(True)
    plt.show()

def calculate_quantiles_and_plot(data):
    data = np.array(data)
    quantile_33 = np.max(data) / 3
    quantile_66 = np.max(data) * 2 / 3

    low_count = np.sum(data < quantile_33)
    mid_count = np.sum((data >= quantile_33) & (data < quantile_66))
    up_count = np.sum(data >= quantile_66)

    counts = [low_count, mid_count, up_count]
    categories = ['Low', 'Mid', 'Up']

    plt.figure(figsize=(8, 6))
    plt.bar(categories, counts, color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title('Counts in Different Categories')
    plt.show()
    return low_count, mid_count, up_count

def plot_multiple_lines(low_list, mid_list, up_list):
    plt.figure(figsize=(8, 6))

    plt.plot(range(len(low_list)), low_list, marker='o', color='r', label='low')
    plt.plot(range(len(mid_list)), mid_list, marker='s', color='g', label='mid')
    plt.plot(range(len(up_list)), up_list, marker='^', color='b', label='up')

    plt.xlabel('Time')
    plt.ylabel('Turtles')
    plt.title('Class Plot')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        gini_list = []
        low_list = []
        mid_list = []
        up_list = []
        for row in csv_reader:
            float_row = [float(num) for num in row]
            gini = gini_coefficient(float_row)
            print("Gini index is {}".format(gini))
            gini_list.append(gini)
            plot_lorenz_curve(float_row)
            low, mid, up = calculate_quantiles_and_plot(float_row)
            low_list.append(low)
            mid_list.append(mid)
            up_list.append(up)
            pass
        plot_multiple_lines(low_list, mid_list, up_list)
        plot_gini_indices(gini_list)

