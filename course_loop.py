import pandas as pd
import time



liste = [
    "pomme",
    "patate",
    "poire",
    "banane",
    ]


   
liste.append("concombre")


    

 
liste_code = list()
for elt in liste:
    code = elt[0:3].upper()
    liste_code.append(code)
#print(liste_code)

liste_code = [elt[0:3].upper() for elt in liste]
print(liste_code)


liste_code = [elt[0:3].upper() for elt in liste if elt[0]=="p"]
print(liste_code)

liste_code = [elt[0:3].upper() if elt[0]=="p" else "NAN" for elt in liste]
print(liste_code)

df = pd.DataFrame({
    'Fruit':liste,
    'Code':liste_code,
})
print(df)

def fonction_perso(elt):
    elt_new = elt*3
    elt_new = elt_new.lower()
    return elt_new




start_time = time.time()
df["test_time"] = ""
for i,elt in df.iterrows():
    df.loc[i,"test_time"] = fonction_perso(df.loc[i,"Code"])
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time for iterrows method:", elapsed_time, "seconds")  
    
start_time = time.time()
df["test_time"] = df["Code"].apply(fonction_perso)
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time for apply method:", elapsed_time, "seconds")



df = pd.concat([df] * 100000, ignore_index=True)

start_time = time.time()
df["test_time"] = ""
for i,elt in df.iterrows():
    df.loc[i,"test_time"] = fonction_perso(df.loc[i,"Code"])
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time for iterrows method:", elapsed_time, "seconds")  
    
start_time = time.time()
df["test_time"] = df["Code"].apply(fonction_perso)
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time for apply method:", elapsed_time, "seconds")

