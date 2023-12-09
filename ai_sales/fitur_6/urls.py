from django.urls import path
from .views import AirobosolutionandProposalRecommendation

urlpatterns = [
    path('sistemrekomendasi-AI Robo Solution & Proposal Recommendation', AirobosolutionandProposalRecommendation.as_view(), name= 'sistemrekomendasi-AI Robo Solution & Proposal Recommendation'),
]