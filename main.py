import matplotlib.pyplot as plt
import numpy as np
import random
import os
from collections import Counter

def summarize_results(results):
    counts = Counter(results)
    print(f"Heads: {counts['Heads']}")
    print(f"Tails: {counts['Tails']}")

def coin_toss():
    return random.choice(['Heads', 'Tails'])

def sumilate_tosses(num_tosses):
    if not int(num_tosses):
        print("Please enter valid number.")
        raise Exception

    print(f'\nTossing for {num_tosses} times')
    tosses = []
    for i in range(num_tosses):
        res = coin_toss()
        print(f"Toss #{i}: {res}")
        tosses.append(res)

    return tosses

def display_probabilities(results):
    total = len(results)
    heads = results.count('Heads')
    tails = total - heads
    print(f"\nHeads: {heads/total:.2%}")
    print(f"Tails: {tails/total:.2%}")

def plot(tosses):
    counts = Counter(tosses)
    plt.figure(figsize=(6,6))
    plt.bar(counts.keys(), counts.values(), color=['gold', 'silver'])
    plt.title('Coin Toss Simulation')
    plt.xlabel('Outcome')
    plt.ylabel('frequency')
    plt.show()

def main():
    num_of_tosses = int(input('How many times would you like to toss the coin?\n'))
    tosses = sumilate_tosses(num_of_tosses)
    summarize_results(tosses)
    display_probabilities(tosses)
    plot(tosses)



if __name__ == '__main__':
    main()