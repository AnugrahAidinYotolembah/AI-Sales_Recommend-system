from django.apps import AppConfig
import joblib
import os


class Fitur6Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fitur_6'

    #load models
    airobosolutionandproposalrecommendation_pred_model_path = os.path.join(os.path.dirname(__file__), 'model', 'AISALES_FITUR6.joblib')
    airobosolutionandproposalrecommendation_model = joblib.load(airobosolutionandproposalrecommendation_pred_model_path)

    dataset = os.path.join(os.path.dirname(__file__), 'dataset', 'AISALES_FITUR 6.csv')
    
