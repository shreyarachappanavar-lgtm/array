import sys

# Check if user gave arguments
if len(sys.argv) > 1:
    scores = sys.argv[1:]
    print("User-provided scores:")
else:
    print("No input given – using the default scores")
    scores = ["85", "90", "78"]

# Convert all scores to integers
scores = [eval(x) for x in scores]

# Calculate total
total = sum(scores)
average = total / len(scores)

# Print results
print("Scores:", scores)
print("Total =", total)
print("Average =", average)