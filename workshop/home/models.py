from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.search import index

from workshop.core.models import BasePage


class HomePage(BasePage):
    template = "pages/home/home_page.html"

    # Only allow creating HomePages at the root level
    parent_page_types = ["wagtailcore.Page"]

    strapline = models.CharField(blank=True, max_length=255)
    call_to_action = models.ForeignKey(
        "core.CallToActionSnippet",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    search_fields = BasePage.search_fields + [index.SearchField("strapline")]

    content_panels = BasePage.content_panels + [
        FieldPanel("strapline"),
        FieldPanel("call_to_action"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["vertical_cards"] = [
            {
                "title": "Card title 1",
                "description": "Card description 1",
                "href": "https://www.torchbox.com",
                "posted_on": "2020-01-01",
            },
            {
                "title": "Card title 2",
                "description": "Card description 2",
                "href": "https://www.torchbox.com",
                "posted_on": "2020-01-01",
            },
            {
                "title": "Card title 3",
                "description": "Card description 3",
                "href": "https://www.torchbox.com",
                "posted_on": "2020-01-01",
            },
        ]

        context["horizontal_cards"] = [
            {
                "title": "Card title 1",
                "description": "Card description 1",
                "href": "https://www.torchbox.com",
            },
            {
                "title": "Card title 2",
                "description": "Card description 2",
                "href": "https://www.torchbox.com",
            },
            {
                "title": "Card title 3",
                "description": "Card description 3",
                "href": "https://www.torchbox.com",
                
            },
        ]

        return context