Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... # REGRESI LINEAR
... 
... import numpy as np                                    #untuk simbol-simbol
... from sklearn.linear_model import LinearRegression     #memanggil library regresi linear
... 
... #database
... #x = Data, y = target
... x = [[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]] 
... y = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22]               #x dikali 2
... 
... regr = LinearRegression().fit(x,y)                    #untuk fitting grafik
... regr.score(x, y)                                      #untuk menentukan grafik
... 
... #data uji
... predict = np.array([[121]])                            #nilai yang di prediksi
... 
... #menampilkan data prediksi (menampilkan karakter)
... print ("Prediksi") 
... print ("input = ", predict)
