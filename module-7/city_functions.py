def city_country(city, country, population=None):
    """Return a formatted string with city, country, and optional population."""
    if population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"

# Test calls
print(city_country('Santiago', 'Chile', 5000000))
print(city_country('Paris', 'France', 2200000))
print(city_country('Tokyo', 'Japan', 14000000))
