def compute_average(scores, size):
    total = 0;

    for i in range(size):
        total += scores[i]

    return total / size

def find_best_city(cities, scores, size):
    best_idx = 0

    for i in range(1, size):
        if scores[i] > scores[best_idx]:
            best_idx = i

    return cities[best_idx]

if __name__ == "__main__":
    SIZE = 4
    cities[SIZE] = ["Melbourne", "Sydney", "Brisbane", "Perth"]
    scores[SIZE] = [85, 72, 90, 68]

    avg = compute_average(scores, SIZE)
    best = find_best_city(cities, scores, SIZE)

    print("Average score: ", avg)
    print("Best cities: ", best)