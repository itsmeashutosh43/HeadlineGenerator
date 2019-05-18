import os
import stopwords
import pandas as pd

def loadData():
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        BASE_DIR=BASE_DIR+'/HeadlineGenerator/dataset/onlineKhabar.csv'
        df=pd.read_csv(BASE_DIR,delim_whitespace=True)




def main():
        loadData()



if __name__=="__main__":
        main()