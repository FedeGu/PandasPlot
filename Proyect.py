# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:19:56 2023

@author: FGurr
"""

import pandas as pd
import matplotlib.pyplot as plt

biblio = pd.read_csv("Bibliotecas.csv")
museo = pd.read_csv("Museos.csv")
cines = pd.read_csv("Cines.csv")

cines_df = cines[["Provincia", "Categoría"]].groupby("Provincia").count()
museo_df = museo[["Provincia", "Categoría"]].groupby("Provincia").count()
biblio_df = biblio[["Provincia", "Categoría"]].groupby("Provincia").count()

Provin_df = cines_df.merge(biblio_df, on="Provincia") \
    .merge(museo_df, on="Provincia")


Provin_df = Provin_df.rename(columns={"Categoría_x": "Cines",
                                      "Categoría_y": "Bibliotecas",
                                      "Categoría": "Museos"})


Provin_df.plot(kind="bar", figsize=(12,8))

plt.title('Recuento de propuestas culturales por provincia')
plt.xlabel('Provincia')
plt.ylabel('Recuento')

plt.show()
