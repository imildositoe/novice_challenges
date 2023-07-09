import numpy as np
import pandas as pd

def main():
    dictionary = {"col 1": [1., 2., 3., 4., 5.],
                  "col 2": [6., 7., 8., 9., 10.],
                  "col 3": ["um", "dois", "tres", "quatro", "cinco", "seis"]
                 }
    
    df_data = pd.DataFrame(data=dictionary)
    print(df_data)
    
    # Testing next function with loop statement 
    while (df_data.next() != None):
        print(df_data.next())

if __name__ == '__main__':
    main()