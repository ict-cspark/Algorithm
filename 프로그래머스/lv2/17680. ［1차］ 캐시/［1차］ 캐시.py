def solution(cacheSize, cities):
    cache = []
    answer = 0

    if cacheSize:
        for city in cities:
            city = city.lower()
            if city in cache:
                cache.pop((cache.index(city)))
                cache.append(city)
                answer += 1

            else:
                if cacheSize == len(cache):
                    cache.pop(0)
                cache.append(city)
                answer += 5

    else:
        answer = len(cities) * 5
    return answer