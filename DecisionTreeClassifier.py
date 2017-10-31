from sklearn import tree
"""
Very basic decision tree classifier.
Works in tandem with the Google Developers series 'Machine Learning Recipes'.
Educational purposes only.
"""

features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[110, 0]])