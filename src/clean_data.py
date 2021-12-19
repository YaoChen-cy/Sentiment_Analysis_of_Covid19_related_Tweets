import pandas as pd
import re
import os,glob

def main():

    df=pd.read_csv("clean_data.csv")
    df['text1']=df['text'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])
    df.drop_duplicates("text1", inplace=True)
    search_list = ["COVID","Vaccination", "Moderna", "Pfizer", "AstraZeneca", "Janssen"]
    #df = df[df['text'].str.contains('|'.join(search_list), case=False)]
    #df = df[df['text'].str.contains("covid", case=False)]
    df.reset_index(inplace=True)
    df=df.iloc[:,3:5]
    print(df)
    df.to_csv('final_clean_data.csv')
    """
    path = "/Users/chenyao/Downloads/COMP598_final_project"

    all_files = glob.glob(os.path.join(path, "clean_data_Nov*.csv"))
    df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
    df_merged = pd.concat(df_from_each_file, ignore_index=True)
    df_merged.to_csv("clean_data.csv")
    """



if __name__ == "__main__":
    main()