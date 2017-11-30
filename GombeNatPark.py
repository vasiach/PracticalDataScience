import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

summary_filename = 'data/gombe_128.csv'
ratings_filename = 'data/gombe_460.csv'

sumdf = pd.read_csv(summary_filename)
ratingsdf = pd.read_csv(ratings_filename)

impl = sumdf.impl
print('a)The median impulsiveness score is {:.2f}'.format(impl.median()))

chimcode_dig =sumdf.chimpcode[sumdf.chimpcode.str.contains(r'\d{3}.*')]
print('b)The number of chimpanzees with 3 digits in their code is {}'.format(len(chimcode_dig)))

avg_diff_decs_conv = abs((sumdf['conv']-sumdf['decs']).mean())
print('c) The average difference between conventional and decisive traits is {:.3f}'.format(avg_diff_decs_conv))

grouped_by_sex = sumdf[sumdf.columns[-6:]].copy()]groupby(['sex'])
prominence = grouped_by_sex.mean()
print(prominence)