from django.template.loader import get_template
import logging


def render_template(template_path: str, context_data: dict):
    """Renders a template file according to the context data"""
    try:
        template = get_template(template_path)
        rendered_data = template.render(context_data)
        return rendered_data
    except Exception as e:
        logging.exception("Error while rendering template '%s': %s", template_path, e)
        return None
