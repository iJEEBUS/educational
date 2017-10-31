from sklearn import tree
"""
Very basic decision tree classifier.
Works in tandem with the Google Developers series 'Machine Learning Recipes'.
Educational purposes only.
"""

# The data to be inputted into the decision tree classifier
# 1st number = the weight of the fruit
# 2nd number = bumpy or smooth (bumpy = 0, smooth = 1)
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

# What the actual outcomes of inputted features are.
# 1 = orange
# 0 = apple
labels = [0,0,1,1]

# Create the actual decision tree classifier
clf = tree.DecisionTreeClassifier()

# Attempts to find a pattern in the inputted data
clf = clf.fit(features, labels)

# Test for the classifier
print clf.predict([[110, 0]])