import pandas as pd
import re
import os,glob


def main():
    #uploading the pre-clean data file
    df=pd.read_csv("clean_data.csv")
    # remove the link in the content
    df['text1']=df['text'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])
    #remove all duplicate rows
    df.drop_duplicates("text1", inplace=True)
    df.reset_index(inplace=True)
    df=df.iloc[:,3:5]
    print(df)
    df.to_csv('final_clean_data.csv')
    """
    path = "XXX"
    all_files = glob.glob(os.path.join(path, "clean_data_Nov*.csv"))
    df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
    df_merged = pd.concat(df_from_each_file, ignore_index=True)
    df_merged.to_csv("clean_data.csv")
    """


if __name__ == "__main__":
    main()
