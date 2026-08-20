print("\n----------------------- t1: ------------------")
readings = []
with open("3/sensor_log.txt", "r") as fp:
    for line in fp:
        readings.append(line.strip())
print(readings)

print("\n----------------------- t2: ------------------")
model_names = ["logistic_regression", "random_forest", "svm"]
model_names.append("mariam-refaat")
with open("3/model_registry.txt", "w") as fp:
 for name in model_names:
     fp.write(name + "\n")

print(model_names)
print("\n----------------------- t3: ------------------")     
from metrics_toolkit import my_functions
print(f"sum of 2,3 using metrics_toolkit : {my_functions.sum_values(2,3)}")