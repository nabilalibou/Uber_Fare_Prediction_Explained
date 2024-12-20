import pandas as pd
import matplotlib.pyplot as plt
import requests
import gzip
import shutil

"""
> Regression problem.

> Formatter les dates, heures, adresses. Vérifier les valeurs manquantes, mal formatées etc pour merger toute les colonnes
en un seul tableau de feature 'df'.

>  Hypothèses à vérifier avec quelques graphs: 
- Fee varie en fonction de la meteo: rain_level (barplot) ou temperature (plot).
- Fee varie en fonction du jour (plot) ou de l'heure (plot): matin/midi/aprem/soir/nuit (barplot, boxplot).
- Fee varie en fonction de la distance entre les adresses: comparer la distance cartésienne (x,y) entre la localisation 
de départ et d'arrivée. 
- Fee varie en fonction de l'arrondissement de départ ou d'arrivée. Biai éventuel sur le milieu social de la personne.
(Eventuellement => graph de tout les points (x,y), ainsi que 
tout les points (lat,lon) pour la localisation de départ/D'arrivée + ajouter une color map dépendant de la valeur de 
'fee').
> Ajouter les features de distance cartésiennes (x,y), distance géodésique (lat, lon). Ajouter 

> Check les corrélations entre les features (rain et meteo) (distance (x,y) et distance (lat,lon)).

> Rescale les coordonnées. 

> Split train/Test pour une cross-validation.

> Commencer avec un Estimateur scikit-learn pour une Regression avec Lasso. Si ça underfit, tester un shallow neural network.
Si ça overfit, simplifier les features en remplacer par des catégories: gelé/froid/tempéré, distance courte/moyenne/longue, 
etc ou changer de régularisation ou PCA?
> Fine-Tune

> Metric to use: Mean Square Error (MSE)
"""


# url = "https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-75.csv.gz"
# destination_path = "data/paris_adress_info.csv"
# response = requests.get(url, stream=True)
# response.raise_for_status()
#
# with gzip.open(response.raw, 'rb') as f_in, open(destination_path, 'wb') as f_out:
#     shutil.copyfileobj(f_in, f_out)

hubert_data = pd.read_csv("data/hubert.csv")
meteo = pd.read_csv("data/meteo_france.csv")
paris_adress_info = pd.read_csv("data/paris_adress_info.csv", delimiter=';')
df = hubert_data.copy()
# print(df.shape)
# df.info()
# min_fee = df['fee'].min()
# max_fee = df['fee'].max()
# print(min_fee)
# print(max_fee)
df = df.dropna()
df['day'] = pd.to_datetime(df['timestamp']).dt.day
df['hour'] = (df['timestamp'].str.split().str[1].str.split(':').apply(lambda x: int(x[0]) + (int(x[1]) >= 30)) % 24)

meteo = meteo.dropna()
meteo['day'] = pd.to_datetime(meteo['timestamp']).dt.day
meteo['hour'] = (meteo['timestamp'].str.split().str[1].str.split(':').apply(lambda x: int(x[0]) + (int(x[1]) >= 30)) % 24)

df = df.merge(meteo, on=['day', 'hour'], how='left')
df['rain_level'] = df['rain_level'].astype(int)
df['temperature'] = df['temperature'].astype(int)

# Merge the coordinates values from paris_adress_info in DF according to numero/nom_voie/nom_commune and
# raw_start_location or raw_end_location

# Plot fee according to time of the day

print("a")


##
# # Count the occurrences of each street to filter out the outliers (arrondissements not appearing more than once)
# arr_counts = paris_adress_info['nom_commune'].value_counts()
# filtered_df = paris_adress_info[paris_adress_info['nom_commune'].isin(arr_counts[arr_counts > 1].index)]
#
# # Compute the mean coordinates for each arrondissements
# mean_coordinate_arr = filtered_df.groupby('nom_commune')[['x', 'y', 'lon', 'lat']].mean().reset_index()
#
# df['start_arr'] = df['raw_start_location'].str.extract(r'(\d+)')
# df['end_arr'] = df['raw_end_location'].str.extract(r'(\d+)')
# mean_coordinate_arr['arr'] = mean_coordinate_arr['nom_commune'].str.extract(r'(\d+)')
#
# df = df.merge(mean_coordinate_arr, left_on='start_arr', right_on='arr', how='left')

# df = df.drop(['start_arr', 'start_arr'], axis=1)