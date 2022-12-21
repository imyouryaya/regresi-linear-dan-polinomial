Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... 
... #REGRESI POLINOMIAL
... 
... #database 
... #x = data, y = Target 
... x  = [[ 2 ],[ 3 ],[ 4 ],[ 5 ],[ 6 ],[ 7 ],[ 8 ],[ 9 ],[10],[11]]
... y  = [ 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81, 100, 121 ]              #x dipangkat 2
... 
... #data uji 
... predict = np.array([[55]]) #nilai yang di prediksi 
... poly = PolynomialFeatures(degree=2) #ordo yang digunakan
... x_=poly.fit_transform(x) #fitting prediksi sumbu
... predict_ = poly.fit_transform(predict) #fitting jenis regresi
... regr = linear_model.LinearRegression() #meregresi
... regr.fit(x_,y) #menentukan grafik
... 
... #menampilkan data prediksi 
... print ("Prediksi")
... print ("input = ", predict)
