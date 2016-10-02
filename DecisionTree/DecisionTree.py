from math import log
import operator 
def createDataSet():
	dataSet=[[1,1,'yes'],
	[1,0,'no'],[0,1,'no'],
	[0,1,'no'],[1,1,'yes']
	]
	labels=['no surfacing','flippers']
	return dataSet,labels
myDat,labels=createDataSet()
#print myDat;
#print labels;
def calShannonEnt(dataSet):
	numEntries=len(dataSet);
	labelCount={};
	for featVec in dataSet:
		currentLabel=featVec[-1];
		if currentLabel not in labelCount.keys():
			labelCount[currentLabel]=0;
		labelCount[currentLabel]+=1
	shannonEnt=0.0
	for key in labelCount:
		prob=float(labelCount[key])/numEntries
		shannonEnt-=prob*log(prob,2)
	return shannonEnt
print calShannonEnt(myDat)
def splitDataSet(dataSet,axis,value):
	retDataSet=[]
	for featVec in dataSet:
		if featVec[axis]==value:
			reducedFeatVec=featVec[:axis];
			reducedFeatVec.extend(featVec[axis+1:]);
			retDataSet.append(reducedFeatVec)
	return retDataSet
print splitDataSet(myDat,0,1)
def chooseFeatureToSplit(dataSet):
	numFeatures=len(dataSet[0])-1;
	baseEntropy=calShannonEnt(dataSet)
	bestInfoGain=0.0;
	bestFeature=-1;
	for i in range(numFeatures):
		featList=[example[i] for example in dataSet]
		uniqueVals=set(featList)
		newEntroy=0.0
		for value in uniqueVals:
			subDataSet=splitDataSet(dataSet,i,value)
			prob=len(subDataSet)/float(len(dataSet))
			newEntroy+=prob*calShannonEnt(subDataSet)
		inforGain=baseEntropy-newEntroy
		if (inforGain>bestInfoGain):
			bestInfoGain=inforGain
			bestFeature=i;
	return bestFeature
print chooseFeatureToSplit(myDat);
def majorityCnt(classList):
	classCount={}
	for vote in classList:
		if vote not in classCount.keys():
			classCount[vote]=0
		classCount[vote]+=1
	sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True);
	return sortedClassCount[0][0]



