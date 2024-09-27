from django import template
from workshop.images.models import CustomImage
from wagtail_factories.factories import ImageFactory

register = template.Library()


# Primary nav snippets
@register.inclusion_tag("components/navigation/primary_nav.html", takes_context=True)
def primary_nav(context):
    request = context["request"]
    return {
        "primary_nav": context["settings"]["navigation"][
            "NavigationSettings"
        ].primary_navigation,
        "request": request,
    }


# Secondary nav snippets
@register.inclusion_tag("components/navigation/secondary_nav.html", takes_context=True)
def secondary_nav(context):
    request = context["request"]
    return {
        "secondary_nav": context["settings"]["navigation"][
            "NavigationSettings"
        ].secondary_navigation,
        "request": request,
    }


# Footer nav snippets
@register.inclusion_tag("components/navigation/footer_nav.html", takes_context=True)
def footer_nav(context):
    request = context["request"]
    return {
        "footer_nav": context["settings"]["navigation"][
            "NavigationSettings"
        ].footer_navigation,
        "request": request,
    }


# Footer nav snippets
@register.inclusion_tag("components/navigation/sidebar.html", takes_context=True)
def sidebar(context):
    return {
        "children": context["page"].get_children().live().public().in_menu(),
        "request": context["request"],
    }


# Footer nav snippets
@register.inclusion_tag("components/navigation/footer_links.html", takes_context=True)
def footer_links(context):
    request = context["request"]
    return {
        "footer_links": context["settings"]["navigation"][
            "NavigationSettings"
        ].footer_links,
        "request": request,
    }


@register.simple_tag()
def get_test_image():
    """
    Generate a test image for use in templates.
    """
    # Get the first image with a tag called "pattern_library"
    image = CustomImage.objects.filter(tags__name="pattern_library").first()

    if not image:
        # Generate one if it doesn't exist
        image = ImageFactory(
            file__from_path="workshop/project_styleguide/tests/assets/balloons.jpg"
        )
        assert hasattr(image, "tags")
        image.tags.add("pattern_library")

    return image
