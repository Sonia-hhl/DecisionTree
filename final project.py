import numpy
import pandas as pd
import math

class TNode:
    def __init__(self,data,level=None,children=[]):
        self.data = data
        self.children = []
        self.level = level
        # self.df = pd.read_csv("feature_train.csv")
        
    def newChild(self,node,data):
        node.children.append(TNode(data,node.level+1))

class Feature:
    def __init__(self,name):
        self.name = name
        self.data = []
        self.weight = {} 
        self.entropy = {}  
        self.labels = {} 


class Tree:
    def __init__(self,feature,label):
        self.depth = 0
        self.nodeList = []
        self.feature = feature
        self.label = label
        self.allFeatures = []

    def get_depth(self):
        return self.depth
    
    def entropy(self, labels):
        entropy = {}
        for i in labels:
            if i not in list(entropy.keys()):
                entropy[i]=1
            elif i in list(entropy.keys()):
                entropy[i]+=1
        # print(entropy)
        for i in entropy.keys():
            entropy[i] = entropy[i] / len(labels)
        # print(entropy)
        for i in entropy.keys():
            entropy[i] = entropy[i] * math.log2(entropy[i])
        #print(entropy)
        sigma = 0
        for i in entropy.keys():
            sigma += entropy[i] 
        return abs(sigma)
    
            # contribution = []
            # for i in entropyDict.keys:
            # contribution = frequency * math.log2(frequency)
            # entropy -= contribution
            # entropyList.append(entropy)
            # print(entropy)        
    def iGain(Self, weight, entropies , pEntropy):
        W_in_E = 0
        for i in  range(len(list(weight.values()))):
            W_in_E += list(weight.values())[i] * entropies[i]
        return pEntropy - W_in_E
    
    def select(self,pEntropy,data,featureList,level):
        iGains = [] # a dictionary to store iGains of all attributes
        allEntropies = []
        allLabel = [] #a list to stores lists of 
        for column in data:
            weight = 0
            weightDict={} # a dictionary to store the amount of a number in a column e.g: {0: 3} there are 3 number 0

            for value in column:
                if value not in weightDict.keys():
                    weightDict[value]=1
                elif value in weightDict.keys():
                    weightDict[value]+=1
            for i in weightDict.keys():
                weightDict[i] = weightDict[i] / len(column)
            # print(weightDict)
            entropies = [] # a list to store entropies of different amounts of an attribute
            for i in weightDict.keys():
                elements = [] # a list to store all labels with an specific amount of an attribute. e.g: all labels that don't have HighBP
                for j in range(len(column)):
                    if column[j] == i:
                        elements.append(self.label["Diabetes_012"].tolist()[j])
                    # print("elements: ", elements)
                entropies.append(self.entropy(elements))
            allEntropies.append(entropies)
            # print("entropies: ", entropies)
            # print("pEntropy:",pEntropy)
            # print("weightDict:",weightDict)
            iGains.append(self.iGain(weightDict,entropies,pEntropy))
            # print("iGain" ,iGains)
        gainmax = max(iGains)
        print(gainmax)
        for i in range(len(iGains)):
            if iGains[i] == gainmax:
                print("max entropies: ", allEntropies[i])
                index = i
        # print(self.feature.columns.tolist()[index])
        t = TNode(featureList[index],level)
        self.nodeList.append(t) 
        del featureList[index]
        print(featureList)   
        for i in range(len(allEntropies)):
            if allEntropies[index][i] == 0:
                # allweight.
                t.newChild(t,)
        del data[index]

    def makeChild(self,):
        pass

    def create_Tree(self):
        pEntropy = self.entropy(self.label["Diabetes_012"].tolist())
        data = [] # a list to store data of each column in an element
        for i in self.feature.columns.tolist():
            data.append(self.feature[i].tolist())
        # print("data: ", data)
        featureList = self.feature.columns.tolist()
        while(data):
            self.select(pEntropy,data,featureList,1)
        
    def make_features(self):
        for name in self.label.columns.tolist():
            f = Feature(name)
            f.data = self.label[name].tolist()
            for value in f.data:
                if value not in f.weight.keys():
                    f.weight[value]=1
                elif value in f.weight.keys():
                    f.weight[value]+=1
            for i in f.weight.keys():
                f.weight[i] = f.weight[i] / len(f.data)
            print(f.data, f.weight)


t = Tree(pd.read_csv("feature.csv"),pd.read_csv("label.csv"))
# print(t.entropy(t.label["Diabetes_012"].tolist()))
t.make_features()