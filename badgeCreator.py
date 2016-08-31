def create_badge(template, **kwargs):
    for key, value in kwargs.iteritems():
        template = template.replace('{{' + key + '}}', value if isinstance(value, str) or isinstance(value, unicode) else repr(value))
    return template
