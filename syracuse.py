
import json
import matplotlib.pyplot as plt

def plot(n_lst: list):
    for lst in n_lst:
        plt.plot(lst, label=f"{lst[0]}: {len(lst)} iterations")
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.xlabel("nb of iterations")
    plt.ylabel("value")
    plt.legend()
    plt.title("Syracuse conjecture")
    plt.show()

def syracuse_algo(n: int):
    values = []
    while n != 1:
        values.append(int(n))
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    return values

if __name__ == "__main__":
    try:
        param = json.load(open("args.json", "rb"))
        numbers = param["numbers"]
        if not all(2 < x <= 100000 for x in numbers):
            raise ValueError("Error: value < 2 or value > 100000")
        if len(numbers) > 10:
            raise ValueError("Error: max number of values = 10")
        numbers.sort()
        result = []
        for n in numbers:
            result.append(syracuse_algo(n))
        plot(result)
    except Exception as e:
        print(e)