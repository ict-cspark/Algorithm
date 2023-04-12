def solution(genres, plays):
    answer = []

    music = {}
    music_total = {}

    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g not in music:
            music[g] = [(idx, p)]
        else:
            music[g].append((idx, p))

        if g not in music_total:
            music_total[g] = p
        else:
            music_total[g] += p

    music_total = sorted(music_total, key=lambda x: music_total[x], reverse=True)

    for g in music_total:
        music_temp = sorted(music[g], key=lambda x: x[1], reverse=True)
        for idx, p in music_temp[:2]:
            answer.append(idx)

    return answer
