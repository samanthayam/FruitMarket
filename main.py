from datetime import datetime
import matplotlib.pyplot as plt

# 資料儲存
fruit = {}

plt.ion()  # interactive mode for live updates

while True:
    time_now = datetime.now().strftime("%m/%d %H:%M:%S")
    category = input("Category (q to quit) : ")
    if category.lower() == "q":
        break

    amount = int(input("Amount : "))
    fruit[f"{category} - {time_now}"] = amount
    print("\nCurrent Entries:")
    for k, v in fruit.items():
        print(f"{k}: ${v}")

    # ===== Pie Chart =====
    plt.clf()

    labels = [k for k in fruit.keys()]
    values = [v for v in fruit.values()]

    # Colors (cycle through pastel colors)
    colors = plt.cm.Pastel1.colors
    colors = [colors[i % len(colors)] for i in range(len(values))]

    # Explode the largest slice
    max_index = values.index(max(values))
    explode = [0.05 if i == max_index else 0 for i in range(len(values))]

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        colors=colors,
        explode=explode,
        shadow=True
    )

    plt.title("Fruit Market Expenses by Entry", fontsize=16)
    plt.axis('equal')  # make pie circular
    plt.pause(0.1)

plt.ioff()
plt.show()
