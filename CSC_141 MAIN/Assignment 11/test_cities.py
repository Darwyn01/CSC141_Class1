from city_functions import city_country

def test_city_country():
    formatted_name = city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'

def test_city_country_population():
    formatted_name = city_country ('santiago', 'chile', 5000000)
    assert formatted_name == 'Santiago, Chile, - population 5000000'
