import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
dataset = pd.read_csv(r"C:\Users\SRUJANA\Downloads\New Facebook Ads Optimization.csv")
print(dataset.head())
N = 15000
num_ads = 10
ads_selected = []
num_of_rewards_1 = [0] * num_ads
num_of_rewards_0 = [0] * num_ads
total_reward = 0
for n in range(0, N):
  ad = 0
  max_random = 0
  for i in range(0, num_ads):
    random_beta = random.betavariate(num_of_rewards_1[i] + 1, num_of_rewards_0[i] + 1)
    if (random_beta > max_random):
      max_random = random_beta
      ad = i
  ads_selected.append(ad)
  reward = dataset.values[n, ad]
  if reward == 1:
    num_of_rewards_1[ad] = num_of_rewards_1[ad] + 1
  else:
    num_of_rewards_0[ad] = num_of_rewards_0[ad] + 1
  total_reward = total_reward + reward
  plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()