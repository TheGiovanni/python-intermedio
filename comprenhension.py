#se recomienda usar list comprension para crear listas en donde sea
#fácil de leer
#cuando no es tan fácil de leer, es smejor seguir usando el modo tradicional


sample_articles = [
    {'title': 'Python logra nuevo éxito', 'source': {'name': 'TechNews'}, 'description': 'Gran noticia', 'category': 'Tecnología'},
    {'title': 'Mercado en crisis', 'source': {'name': 'Finance'}, 'description': 'Análisis completo', 'category': 'Economía'},
    {'title': 'Nueva tecnología', 'source': {'name': 'TechNews'}, 'description': 'Innovación', 'category': 'Tecnología'},
    {'title': 'Deportes hoy', 'source': {'name': 'Sports'}, 'description': 'Resultados', 'category': 'Deportes'},
    {'title': 'Política actual', 'source': {'name': 'News'}, 'description': 'Actualidad', 'category': 'Política'},
    {'title': 'Ciencia avanza', 'source': {'name': 'Science'}, 'description': 'Descubrimientos', 'category': 'Ciencia'}
]

#for tradicional
def extrac_titles_traditional(articles):
    titles = []
    for article in articles:
        titles.append(article["title"])
    return titles

print(extrac_titles_traditional(sample_articles))

print("############# ###############################")

#con list comprehension
def extract_titles_comprehension(articles):
    return [article["title"] for article in articles]

print(extract_titles_comprehension(sample_articles))
print("############# ###############################")
#retorna  titulo y descripción
def extrac_title_description (articles):
    return [(article["title"], article["description"]) for article in articles]
print(extrac_title_description(sample_articles))

#diccionarios con comprension
def extract_titles_description_dict(articles):
    return {article["title"]: article["description"] for article in articles}
print(extract_titles_description_dict(sample_articles))
print("############# ###############################")
#imprime los titulos y fuentes sin repetir fuentes
def extract_titles_sources(articles):
    return {article["source"]["name"] for article in articles}
print(extract_titles_sources(sample_articles))
print(type(extract_titles_sources(sample_articles))) #el tipo debe ser set


