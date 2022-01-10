# Imports
import numpy as np
import requests
import json
import pandas as pd
import configparser
import os

# Classe
class Heart:

    # Método construtor
    def __init__(self, heart):
        self.heart = heart
        config = configparser.ConfigParser()
        diretorio = os.path.abspath(__file__ + "/../")
        files_path = os.path.join(diretorio, 'frontend.ini')
        config.read(files_path)
        self.endpoint = config.get('configuracao','endpoint')

    # Método de preparação dos dados
    def prepare(self):
        # Lista de resultados
        result = np.zeros(13)
        #Idade
        result[0] = int(self.heart[0])
        #Sexo
        result[1] = int(self.heart[1])
        #Dor no peito
        result[2] = int(self.heart[2])
        #Pressao Arterial em repouso (mm Hg)
        result[3] = int(self.heart[3])
        #Colesterol da pessoa em mg / dl
        result[4] = int(self.heart[4])
        #Açúcar em jejum >=120 mg/dl
        result[5] = int(self.heart[5])
        #Medição eletrocardiográfica em repouso
        result[6] = int(self.heart[6])
        #Maxima Frequencia Cardíaca
        result[7] = float(self.heart[7])
        #Angina induzida por exercício
        result[8] = int(self.heart[8])
        #Depressão de ST induzida por exercício em relação ao repouso
        result[9] = float(self.heart[9])
        #Inclinação do segmento ST de pico do exercício
        result[10] = int(self.heart[10])
        #Principais vasos sanguíneos do coração (veias/arterias)
        result[11] = int(self.heart[11])
        #Uma doença do sangue chamada thalassemia
        result[12] = int(self.heart[12])

        return result

    # Método para as previsões
    def predict(self, heart):
        dados = np.array([heart])
        columns = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'cholesterol', 'fasting_blood_sugar', 'rest_ecg','max_heart_rate_achieved', 'exercise_induced_angina', 'st_depression', 'st_slope', 'num_major_vessels', 'thalassemia']
        df = pd.DataFrame(data=dados, columns=columns)

        jsonDados = json.loads(df.to_json(orient="records", lines=True))
        headers = {"charset": "utf-8", "Content-Type": "application/json"}
        
        response = requests.post(self.endpoint, json=jsonDados, headers=headers)
        return json.loads(response.text)

