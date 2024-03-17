import matplotlib.pyplot as plt


p_01 = [
    0,
    0,
    0,
    0.25,
    0.20,
    0.33,
    0.29,
    0.38,
    0.44,
    0.4

]

#p_01.reverse()
r_01 = [
0,
0,
0,
0.1,
0.1,
0.2,
0.2,
0.3,
0.4,
0.4



]

rel_doc = [1,1,2,2,3,3,4,4,4,5]


x_values = [r*1 for r in r_01]
y_values = [p*100 for p in p_01]

plt.plot(x_values, y_values, linewidth=2)

plt.title("Multi Level Precision", fontsize=24)

plt.xlabel("Recall", fontsize=14)
plt.ylabel("Precision", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=10)

plt.show()

# slt.scatter() creates pointed graphs

from die import Die

# Create a D6.
die = Die()
# Make some rolls, and store results in a list.
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []


for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(results)