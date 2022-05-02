def solution(id_list, report, k):
    r = set(report)
    r = list(r)
    counts = [0] * len(id_list)
    names = [[]] * len(id_list)
    answer = [0] * len(id_list)
    for rp in r:
        for e, i in enumerate(id_list):
            if e == rp.split(" ")[0]:
                counts[i] = counts[i] + 1
                names[i].append(rp.split(" ")[1])
                break
    mails = []
    for e, i in enumerate(counts):
        if e >= k:
            mails.append(id_list[i])

    for n, i in enumerate(names):
        for e in n:
            for m in mails:
                if e == m:
                    answer[i] = answer[i] + 1

    return answer