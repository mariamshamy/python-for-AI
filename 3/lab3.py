print("\n----------------------- t1: ------------------")
readings = []
with open("3/sensor_log.txt", "r") as fp:
    for line in fp:
        readings.append(line.strip())
print(readings)

print("\n----------------------- t2: ------------------")
model_names = ["logistic_regression", "random_forest", "svm"]
model_names.append("your_name")
with open("model_registry.txt", "w") as fp:
 for name in model_names:
 fp.write(name + "\n")