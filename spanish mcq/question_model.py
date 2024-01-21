import random
import pandas as pd
class Question:
    def __init__(self) -> None:
        self.df = pd.read_csv('word_data.csv')
        # there are items in the df
        rand_no = random.randint(0, self.df['Spanish'].size)
        self.text = self.df.iloc[rand_no]['Spanish']
        self.answer = self.df.iloc[rand_no]['English']
        self.options = [self.answer] + [self.df.iloc[random.randint(0, 966)]['English'] for _ in range(3)] 
        random.shuffle(self.options)
        
