
def sum_of_multiples(multiples, limit):
    sum = 0
    for i in range(limit):
        if any(i % m == 0 for m in multiples):
            sum += i
    return sum

if __name__ == "__main__":
    multiples = [3, 5]
    limit = 1000
    result = sum_of_multiples(multiples, limit)
    print(f"The sum of all multiples of {multiples} below {limit} is: {result}")