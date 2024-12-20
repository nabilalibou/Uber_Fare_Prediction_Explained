https://www.kaggle.com/code/pankajkumar90/cab-fare-prediction/code
https://medium.com/@azimkhan8018/vehicle-price-prediction-with-machine-learning-9e642afdf19e
https://www.linkedin.com/pulse/machine-learning-approach-forecast-car-rental-demand-pratik-nabriya/
https://github.com/piyushpandey758/Uber-Fare-Prediction
https://www.kaggle.com/code/yasserh/uber-fare-prediction-comparing-best-ml-models


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