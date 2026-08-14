modelName= "roma"
accuracy=112.3
is_deployed=True
version=2

print("\n---------------- t1: ---------------")

print(modelName,type(modelName))
print(accuracy,type(accuracy))
print(is_deployed,type(is_deployed))
print(version,type(version))

print("\n----------------- t2: ----------------    ")


raw_accuracy = "94.7"
raw_epochs = "10"

conv_int=int(raw_epochs)
conv_flo=float(raw_accuracy)

print(conv_int,type(conv_int))
print(conv_flo,type(conv_flo))
print(f"The model accuracy is {conv_flo} and it was trained for {conv_int} epochs")

print("\n----------------- t3: ----------------    ")
x = 17
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)  #3.(2/5)
print(x % y)  #2
print(x ** y) 
print(x // y) #3

print("\n")
total = 0

total += 10
print(total)

total -= 3
print(total) #7

total *= 2
print(total) #14

print("\n----------------- t4: ----------------    ")
model_name = " GpT-4  "

#print(model_name.strip())
#print(model_name[1:6])

new_str=model_name.strip()
new_str=new_str.upper()
new_str=new_str.replace("-", "_")
print(new_str)
print(len(new_str))
print(new_str[0:3])

print("\n----------------- t5: ----------------    ")
scores = [0.71, 0.85, 0.63, 0.90, 0.78]
print(scores)
scores.append(0.88)
print(scores)
scores[0] = scores[-1]
print(scores)
print(scores[3:]) 
#or
#print(scores[-3:])
print(len(scores))


print("\n----------------- t6: ----------------    ")
image_shape = (224, 224, 3)
print(image_shape[0])
print( image_shape[1])
print( image_shape[2])
# image_shape[0]=332   ==tuples are immutable.

print("\n----------------- t7: ----------------    ")
config = {'learning_rate':0.001, 'batch_size': 32}
config["epochs"]=10
config["batch_size"]=64   #no err
print(config)
print(config.keys())
print(config.values())

#for key, value in config.items():
  #print(key, "->", value)

print("\n----------------- t8: ----------------    ")
report = {'name': 'QuantumStride', 'accuracy': 0.912, 'metrics': {'precision': 0.89, 'recall': 0.87},
'sample_predictions': [0.81, 0.42, 0.95]}
print(report["name"])
print( report['metrics']['precision'])
print( report['sample_predictions'][1])
