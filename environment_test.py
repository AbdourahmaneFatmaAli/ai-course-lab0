import sys
import platform
import os

def verify_environment():
    results = []

    results.append(f"Python: {sys.version.split()[0]}")
    results.append(f"OS: {platform.system()}")

    packages = ["numpy", "pandas", "matplotlib", "seaborn"]

    for p in packages:
        try:
            mod = __import__(p)
            results.append(f"{p}: {mod.__version__}")
        except:
            results.append(f"{p}: NOT INSTALLED")

    return "\n".join(results)

if __name__ == "__main__":
    print(verify_environment())