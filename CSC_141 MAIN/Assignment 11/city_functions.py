#Darwyn Avila-Medina
#11-1 City, Country 
def city_country (city, country):
    return f"{city.title()}, {country.title()}"

#11-2 Population 
# def city_country (city, country, population):
def city_country (city, country, population=None):
    if population:
        return f"{city.title()}, {country.title()}, - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
