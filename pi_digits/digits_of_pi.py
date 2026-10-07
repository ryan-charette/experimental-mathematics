import matplotlib.pyplot as plt
from scipy.stats import entropy
from random import randint
import numpy as np

def single_digit_distribution(t):

    with open('pi.txt') as fig:
        pi_str = fig.read()

    n = 10_000
    pi_str = pi_str[:n]
    pi_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

    pi_correct_predictions = 0
    pi_incorrect_predictions = 0
    pi_accuracy = []

    for i in range(n):

        pi_dict[pi_str[i]] += 1

        y = list(pi_dict.values())

        pi_prediction = str(randint(0, 9))

        try:
            if pi_prediction == pi_str[i+1]:
                pi_correct_predictions += 1
            else:
                pi_incorrect_predictions += 1

            pi_prediction_accuracy = pi_correct_predictions / (pi_incorrect_predictions + pi_correct_predictions)
            pi_accuracy.append(pi_prediction_accuracy)
        except:
            IndexError

    for _ in range(t):

        rand_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
        rand_correct_predictions = 0
        rand_incorrect_predictions = 0
        rand_accuracy = []

        for _ in range(n):

            rand_int = str(randint(0, 9))

            rand_y = list(rand_dict.values())

            rand_prediction = str(randint(0, 9))

            try:
                if rand_prediction == rand_int:
                    rand_correct_predictions += 1
                else:
                    rand_incorrect_predictions += 1

                rand_prediction_accuracy = rand_correct_predictions / (rand_incorrect_predictions + rand_correct_predictions)
                rand_accuracy.append(rand_prediction_accuracy)
            except:
                IndexError

            rand_dict[rand_int] += 1

        fig, axes = plt.subplots(1, 2)
        fig.suptitle('n={}, S_rel={}'.format(n, (1 / np.e**entropy(pk=y, qk=rand_y))))

        labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        x = np.arange(len(labels)) 
        width = 0.35 

        axes[0].bar(x - width/2, y, width, label='pi', color='tab:blue')
        axes[0].bar(x + width/2, rand_y, width, label='random', color='tab:red')

        axes[0].set_ylabel('Occurrences')
        axes[0].set_title('Digits of Pi vs RNG')
        axes[0].set_xticks(x, labels)
        axes[0].legend()


        axes[1].plot(pi_accuracy, color='tab:blue')
        axes[1].plot(rand_accuracy, color='tab:red')
        axes[1].axhline(y=0.10, color='k')
        axes[1].set_title('Random Guess Accuracy')

        plt.show()

single_digit_distribution(1)


def consecutive_digit_distribution(k):

    with open('pi.txt') as fig:
        pi_str = fig.read()

    n = 1_000_000
    pi_str = pi_str[:n]
    pi_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

    consecutives = 0
    consecutives_array = []

    for i in range(n):

        check = 0

        for j in range(k):

            try:
                if pi_str[i] == pi_str[i+j]:
                    check += 1
            except:
                IndexError

        if check == k:
            pi_dict[pi_str[i]] += 1
            consecutives += 1

        consecutives_array.append(consecutives/(i+1))

    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    x = np.arange(len(labels)) 
    y = list(pi_dict.values())

    fig, axes = plt.subplots(1, 2)
    fig.suptitle('{} Consecutive Equal Digits'.format(k))

    axes[0].set_title('Distribution')
    axes[0].bar(x, y, color='tab:blue')
    axes[0].set_ylabel('Occurrences')
    axes[0].set_xticks(x, labels)

    axes[1].plot(consecutives_array, color='tab:blue')
    axes[1].axhline(y=(0.10)**(k-1), color='k')
    axes[1].set_title('Proportion')

    plt.show()

for k in range(2, 8):
    consecutive_digit_distribution(k)


def digits_modulo_5(k):

    with open('pi.txt') as fig:
        pi_str = fig.read()

    n = 10_000
    pi_str = pi_str[:n]

    modulo = []

    for i in range(n):
        a = i % 5
        if a == k:
            modulo.append(int(pi_str[i]))

    mod_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    for i in modulo:
        mod_dict[str(i)] += 1

    fig, axes = plt.subplots(2)
    fig.suptitle('Digits Congruent {} mod 5'.format(k))

    x = list(mod_dict.keys())
    y = list(mod_dict.values())

    axes[0].bar(x, y)
    axes[0].set_title('Distribution')
    axes[1].plot(modulo, color='white', marker='o', markerfacecolor='tab:blue')
    axes[1].set_title('Position')
    plt.show()

for k in range(5):
    digits_modulo_5(k)

