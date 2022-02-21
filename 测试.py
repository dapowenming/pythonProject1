# import pandas as pd
# io =r'C:\Users\xfang\Desktop\2021\october\tableau\HZ manufacture dashboard\non_conforming_products_disposition.xlsx'
# data = pd.read_excel(io,sheet_name=0)
# print(data.head())


from sklearn import datasets  # 导入库

boston = datasets.load_boston()  # 导入波士顿房价数据
print(boston.keys())  # 查看键(属性)     ['data','target','feature_names','DESCR', 'filename']
print(boston.data.shape,boston.target.shape)  # 查看数据的形状 (506, 13) (506,)
print(boston.feature_names)  # 查看有哪些特征 这里共13种
print(boston.DESCR)  # described 描述这个数据集的信息
print(boston.filename)  # 文件路径