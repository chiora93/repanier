# -*- coding: utf-8
from django.forms import Widget


class ButtonTestMailConfigWidget(Widget):
    template_name = 'repanier/widgets/button_test_mail_config.html'

    def __init__(self, attrs=None):
        super(ButtonTestMailConfigWidget, self).__init__(attrs=attrs)

    def get_context(self, name, value, attrs):
        context = super(ButtonTestMailConfigWidget, self).get_context(name, value, attrs)
        return context

    # class Media:
    #     js = (
    #         'js/button_test_mail_config_script.js',
    #     )
    #     css = {
    #         'all': (
    #             'css/button_test_mail_config_widget.css',
    #         )
    #     }
