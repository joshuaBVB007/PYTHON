import pickle 

fichero=open("lista","rb")

lectura=pickle.load(fichero)

print(lectura)
