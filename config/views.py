"""View for main bedrock application
"""

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    """HomePage View
    """

    template_name = "index.html"
