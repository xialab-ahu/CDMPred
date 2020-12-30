import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import argparse

# 装载训练集保存的数据预处理MinMax方法的对象
with open("./scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--inputfile",dest='i',type=str, help="input file", required=True)
    args = parser.parse_args()
    return args

# 导入测试集数据
# test=pd.read_csv("../data/Independent.csv",sep=",")
args = parse_args()
test=pd.read_csv(args.i,sep=",")  # 输入测试命令：python predict_final.py -i "./for_test.csv"

# features = ['ExonSnpDensity', 'ExonConservation', 'ExonHapMapSnpDensity', 'MGAPHC',\
#        'MGAEntropy', 'HMMEntropy', 'UniprotREP', 'PredBFactorM', 'AAPolarity',\
#        'PredBFactorS']# 选出的top10特征

features =['UniprotDOM_PostModEnz', 'MGAPHC', 'UniprotCARBOHYD', 'UniprotREP',\
       'ExonSnpDensity', 'ExonConservation', 'UniprotMETAL', 'MGAEntropy',\
       'ExonHapMapSnpDensity', 'UniprotDOM_MMBRBD']
testX=test[features].values
testX = scaler.transform(testX)

# 导入模型并进行预测
filename = './finalized_model_top10features1031.pkl'
loaded_model = pickle.load(open(filename, 'rb'))
pTest=loaded_model.predict_proba(testX)[:,1] #预测的概率值
print('predicted probability:',pTest)
y_pred=loaded_model.predict(testX)# 预测出的类别信息
print('predicted label:',y_pred)




