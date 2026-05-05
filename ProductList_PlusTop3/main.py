def readReviews(filename):
    with open(filename, "r") as file:
        contents = file.read()

    return contents


def parseReviews(contents):
    parsed = [c.split(",") for c in contents]
    return parsed


def countReviews(reviews):
    counts = {}
    for i in reviews:
        if i[0] not in counts:
            counts[i[0]] = 1
        else:
            counts[i[0]] += 1

    return counts


def totalRatings(reviews):
    counts = {}
    for i in reviews:
        if i[0] not in counts:
            counts[i[0]] = int(i[1])
        else:
            counts[i[0]] += int(i[1])
    return counts


def calculateAverages(reviewCounts, ratingTotals):
    averages = {}
    for k, v in ratingTotals.items():
        average = v / reviewCounts[k]
        averages[k] = average

    return averages


def displayAverages(reviewCounts, averages):
    print("All Product Ratings:")
    for k, v in reviewCounts.items():
        print("%s | Reviews: %d | Average Rating: %.2f" % (k, v, averages[k]))


def getTopThreeProducts(averages):
    highest_values = {}

    min_len = 3
    if len(averages) < min_len:
        return "Not enough values"

    for i in range(3):
        highest_item = ""
        highest_v = None
        for k, v in averages.items():
            if k in highest_values:
                continue
            if highest_v is None or v > highest_v:
                highest_v = v
                highest_item = k
        highest_values[highest_item] = highest_v

    return highest_values


def main():
    reviews = readReviews("reviews2025.txt")
    reviews_list = reviews.splitlines()

    parsed_reviews = parseReviews(reviews_list)
    count_reviews = countReviews(parsed_reviews)
    total_c_reviews = totalRatings(parsed_reviews)
    review_averages = calculateAverages(count_reviews, total_c_reviews)
    top_three = getTopThreeProducts(review_averages)

    displayAverages(count_reviews, review_averages)
    print("\nTop 3 Products:")
    iterable = 1
    for k, v in top_three.items():
        print("%d. %s - %.2f" % (iterable, k, v))
        iterable += 1


main()
