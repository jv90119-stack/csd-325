def city_country(city, country, population=None, language=None):
    result = f"{city}, {country}"
    if population is not None:
        result += f" - Population: {population}"
    if language is not None:
        result += f", {language}"
    return result   

# Function calls

if __name__ == "__main__":
    print(city_country("Paris", "France"))
    print(city_country("Paris", "France", 2000000))   
    print(city_country("Paris", "France", 2000000, "French"))
    
    print(city_country("Madrid", "Spain"))
    print(city_country("Madrid", "Spain", 3400000))
    print(city_country("Madrid", "Spain", 3400000, "Spanish"))
    
    print(city_country("Tokyo", "Japan"))
    print(city_country("Tokyo", "Japan", 37000000))
    print(city_country("Tokyo", "Japan", 37000000, "Japanese"))