import numpy
import pandas as pd
import math

class TNode:
    def __init__(self,data,children=[],level=None):
        self.data = data
        self.children = []
        self.level = level
        self.df = pd.read_csv("feature_train.csv")
        
    def newChild(self,node,data):
        node.children.append(TNode(data,node.level+1))

class Tree:
    def __init__(self,feature,label):
        self.depth = 0
        self.nodeList = []
        self.feature = feature
        self.label = label

    def get_depth(self):
        return self.depth
    
    def create_Tree(self):
        pass
    
    def entropy(self):
        entropyDict={}
        labels =self.label["Diabetes_012"].tolist()
        # print(labels)
        data = []
        for i in feature_train.columns.tolist():
            data.append(feature_train[i].tolist())
        for column in data:
            entropy = 0
            for value in column:
                if value not in list(entropyDict.keys()):
                    entropyDict[value]=1
            #     frequency = column.count(value) / len(column)
            #     contribution = frequency * math.log2(frequency)
            #     entropy -= contribution
            # entropyList.append(entropy)
            # print(entropy)        

    def iGain(Self):
        pass

t = Tree(pd.read_csv("feature_train.csv"),pd.read_csv("label_train.csv"))
