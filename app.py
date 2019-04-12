from parser import RatingRunetaParser


urls = [
    'http://www.ratingruneta.ru/seo/1-200/',
    'http://www.ratingruneta.ru/web/1-200/',
    'http://www.ratingruneta.ru/seo+context/1-200/',
]

p = RatingRunetaParser()

for url in urls:
    result = p.perform_parsing(url)
    p.save_result_to_file(result)
