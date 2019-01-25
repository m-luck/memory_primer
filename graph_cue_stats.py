import matplotlib.pyplot as plt
import ast
filename = "cue_stats.txt"
file = open(filename, "r")
cue_stats = ast.literal_eval(file.readline())
for cue in cue_stats:
    X = []
    for info_set in cue_stats[cue]:
        for pause in info_set[1]:
            X.append(pause)
    plt.plot(X, label=str(cue))
# Add legend
plt.legend(loc='lower left')
# Add title and x, y labels
plt.title("Random Walk Example", fontsize=16, fontweight='bold')
plt.suptitle("Random Walk Suptitle", fontsize=10)
plt.xlabel("Number of Steps")
plt.ylabel("Accumulative Sum")
plt.show()
