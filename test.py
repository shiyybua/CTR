from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder()
ret = enc.fit_transform([[1], [2], [3], [1]])
print(ret.toarray())