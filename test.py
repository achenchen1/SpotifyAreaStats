from math import log

ln = log


def attempt_a(x, T):
    return ln(T + 1) * x / T


def attempt_b(x, T):
    return 1 / (ln(T + 2)) * x


def attempt_c(x, T):
    result = 0
    for i in range(x):
        result += 1 / (result + 1)
    return result


def attempt_d(x, T):
    return 1 / (10 * ln(T) + 1) * x**0.8


attempts = [attempt_b, attempt_d]

test_cases = [
    ("John Mayer", 430, 1000),
    ("Jason Mraz", 46, 100),
    ("Jason Mraz", 46, 100),
    ("Jason Mraz", 46, 100),
    ("Jason Mraz", 46, 100),
    ("Madison Cunningham", 27, 100),
    ("Ed Sheeran", 19, 100),
    ("Jack Johnson", 11, 100),
    ("Mac Miller", 5, 10),
    ("ATCQ", 5, 10),
    ("ATCQ", 1, 1000),
    ("Bach", 1, 3),
    ("Brahms", 2, 3),
]


for algo in attempts:
    print("Algo: ", algo.__name__)
    results = {}
    for t in test_cases:
        r = algo(t[1], t[2])
        if t[0] in results:
            results[t[0]][1] += r
            results[t[0]][2] += t[1]
            results[t[0]][3] += t[2]
        else:
            results[t[0]] = [t[0], r, t[1], t[2]]

    normalization = max(results.values(), key=lambda i: i[1])[1]

    for i in results:
        results[i][1] /= normalization
    print(
        *sorted(list(results.values()), key=lambda i: i[1], reverse=True),
        sep="\n",
        end="\n\n"
    )
