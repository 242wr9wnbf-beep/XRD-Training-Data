import matplotlib.pyplot as plt
import pandas as pd

# --- USER SETTINGS ---
# Replace these with your actual file names or paths
file1 = "RSE8652_PVSK_Film_1-1-01_001.xy"
file2 = "sample2.xy"
file3 = "sample3.xy"

# Optional labels for the legend
labels = ["Sample 1", "Sample 2", "Sample 3"]

# --- READ FILES ---
def read_xy(filename):
    """
    Reads a .xy file assuming two columns: 2θ and intensity.
    Skips empty lines or lines starting with '#'.
    """
    df = pd.read_csv(
        filename,
        delim_whitespace=True,
        comment='#',
        names=["2Theta", "Intensity"],
        engine="python"
    )
    return df

data1 = read_xy(file1)
data2 = read_xy(file2)
data3 = read_xy(file3)

# --- PLOT ---
plt.figure(figsize=(8, 5))
plt.plot(data1["2Theta"], data1["Intensity"], label=labels[0], linewidth=1.2)
plt.plot(data2["2Theta"], data2["Intensity"], label=labels[1], linewidth=1.2)
plt.plot(data3["2Theta"], data3["Intensity"], label=labels[2], linewidth=1.2)

# --- GRAPH FORMATTING ---
plt.xlabel("2θ (degrees)")
plt.ylabel("Intensity (a.u.)")
plt.title("XRD Patterns Comparison")
plt.legend()
plt.tight_layout()
plt.grid(alpha=0.3)

plt.show()
