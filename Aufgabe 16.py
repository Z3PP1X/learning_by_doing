import pandas as pd

class Statistics:

    def __init__(self, input_values:list) -> None:
        self.input_values = input_values
        self.check_value_type()
        self.DataFrame = pd.DataFrame(input_values, columns=["Numbers"])
        


    def check_value_type(self):
        for input in self.input_values:
            if not isinstance(input, (int, float)):
                raise ValueError(f'Your passed input is not of type int or float: {input}')
    
    def min_value(self):
        return self.DataFrame['Numbers'].min()
    
    def max_value(self):
        return self.DataFrame['Numbers'].max()
    
    def mean(self):
        return self.DataFrame['Numbers'].mean()

    def median(self):
        return self.DataFrame['Numbers'].median()
    
    def std_dev(self):
        return self.DataFrame['Numbers'].std(ddof=0)




Test = Statistics([10,'str'])
print(Test.std_dev())