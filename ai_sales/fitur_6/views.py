"""
Module containing API views for airobosolutionandProposalRecommendation.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from fitur_6.function.feature import need_recommendation

class AirobosolutionandProposalRecommendation(APIView):
    """
    API view for airobosolutionandProposalRecommendation.
    """
    def post(self, request, format=None):  # pylint: disable=W0622
        """
        Handles POST requests for airobosolutionandProposalRecommendation.

        Parameters:
        - request: The HTTP request object.
        - format: The format of the response (default is None)[Unused argument].

        Returns:
        - Response: The HTTP response.
        """
        try:
            result = need_recommendation(request.data)
            return Response(build_result(result), status=status.HTTP_200_OK)
        except Exception as error_exception:  # pylint: disable=C0103,W0703
            error_message = str(error_exception)
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

def build_result(result):
    """
    Builds a standardized result structure.

    Parameters:
    - result: The result data.

    Returns:
    - dict: The standardized result structure.
    """
    result_dict = {
        "status": 200,
        "message": "success",
        "result": result
    }

    return result_dict
