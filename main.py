from datetime import datetime

# 資料儲存
fruit = {}

while True:
    time_now = datetime.now().strftime("%m/%d %H:%M:%S")
    category = input("Category (q to quit) : ")
    if category.lower() == "q":
        break

    amount = int(input("Amount : "))
    fruit[f"{category} - {time_now}"] = amount