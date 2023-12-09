"""
Module containing functions for recommendation feature.
"""

import pandas as pd
from ..apps import Fitur6Config
# from ..libraries import utils

def get_recommendations(need, cosine_sim, data):
    """
    Get recommendations based on input need, cosine similarity matrix, and data.

    Parameters:
        - need (str): The input need.
        - cosine_sim (array): The cosine similarity matrix.
        - data (pd.DataFrame): The input data.

    Returns:
        pd.DataFrame: DataFrame of recommendations.
    """
    search_recommendations = len(data)
    idx = data.loc[(data['need'] == need)].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:search_recommendations+1]
    company_indices = [i[0] for i in sim_scores]
    return data[['training_name']].iloc[company_indices].drop_duplicates()

def transform_input(data):
    """
    Transforms input data into a DataFrame.

    Parameters:
        data (dict): Input data.

    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    data = {key: [value] for key, value in data.items()}
    data_frame = pd.DataFrame(data)
    return data_frame

def need_recommendation(data):
    """
    Get recommendations for training needs based on input data.

    Parameters:
        data (dict): Input data.

    Returns:
        dict: Dictionary of recommended training names.
    """
    my_data = transform_input(data)
    need = my_data['need'].iloc[0]
    data = pd.read_csv(Fitur6Config.dataset)
    model = Fitur6Config.airobosolutionandproposalrecommendation_model
    recommendations = get_recommendations(need, model, data)[:10]

    recommendations['score'] = range(1, len(recommendations) + 1)
    recommendations_sorted = recommendations.sort_values(by='score', ascending=True)

    for i, row in recommendations_sorted.iterrows():
        score_percent = (len(recommendations) - row['score'] + 1) / len(recommendations) * 100
        result_string = f"{row['training_name']} (compatibility: {score_percent:.2f}%)"
        recommendations_sorted.loc[i, 'training_name'] = result_string

    recommendations_sorted = recommendations_sorted.drop(['score'], axis=1)
    dict_from_df = recommendations_sorted.to_dict(orient='list')
    return dict_from_df
