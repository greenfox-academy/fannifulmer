# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve","Ashley","Bözsi","Kat","Jane"]
boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"]
order = []


for i in range(0,len(girls)):
    order.append(girls[i])
    order.append(boys[i])
    i += 1
order.append(boys[5])
print(order)
