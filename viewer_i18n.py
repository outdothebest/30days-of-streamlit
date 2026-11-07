"""Language negotiation for the course viewer using standard HTTP preferences."""


def choose_language(requested, accept_language, available):
    if requested in available:
        return requested
    preferences = []
    for item in accept_language.split(","):
        tag, *parameters = item.strip().split(";")
        quality = 1.0
        for parameter in parameters:
            if parameter.strip().startswith("q="):
                try:
                    quality = float(parameter.strip()[2:])
                except ValueError:
                    quality = 0.0
        if 0 < quality <= 1:
            preferences.append((quality, tag.lower().replace("_", "-").split("-")[0]))
    for _, language in sorted(preferences, key=lambda item: item[0], reverse=True):
        if language in available:
            return language
    return "en" if "en" in available else available[0]
