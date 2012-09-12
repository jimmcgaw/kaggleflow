from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt

def make_submission():
	print "reading data from file..."
	dataset = genfromtxt(open("/Users/jimmcgraw/djangoprojects/learning/biological/train.csv", "r"), delimiter=",", dtype="f8")[1:]
	target = [x[0] for x in dataset]
	print "TARGET"
	print target
	train = [x[1:] for x in dataset]
	print "TRAIN"
	print train
	test = genfromtxt(open('/Users/jimmcgraw/djangoprojects/learning/biological/test.csv', 'r'), delimiter=",", dtype="f8")[1:]
	print "TEST"
	print test
	
	rf = RandomForestClassifier(n_estimators=100)
	rf.fit(train, target)
	predicted_probs = [x[1] for x in rf.predict_proba(test)]
	print "PREDICTED PROBS"
	print predicted_probs
	
	savetxt("/Users/jimmcgraw/djangoprojects/learning/biological/submission.csv", predicted_probs, delimiter=",", fmt="%f")