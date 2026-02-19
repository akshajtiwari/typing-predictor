import pandas as pd


csv_path="/home/akshajtiwari/Desktop/typing_predictor/raw_data/results.csv"

def pre_process_csv(csv_path):

    def load_csv(csv_path):
        data=pd.read_csv(csv_path)
        df= pd.DataFrame(data)
        return df

    def drop_columns(df):
        df.drop(columns=['afkDuration','restartCount','incompleteTestSeconds', 'funbox', 'lazyMode', 'blindMode','bailedOut', 'tags'],inplace=True)
        return df 
    
    def remove_nan(df):
        columns_drop=['wpm','acc']
        df = df.dropna(subset=columns_drop)
        # consistency median, language unknown
        median=df['consistency'].median()
        df['consistency']=df['consistency'].fillna(median)
        df['language']=df['language'].fillna("unknown")
        return df

    def change_dtypes(df):
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')    
        df['isPb']=df['isPb'].astype('bool')
        df['mode2']=df['mode2'].replace("custom",-1).astype(int) # -1 represents custom time durations 
        return df

    def split_char_stats(df):
        char_split = df["charStats"].str.split(";", expand=True)
        df["correct_chars"] = char_split[0].astype(int)
        df["incorrect_chars"] = char_split[1].astype(int)
        df["extra_chars"] = char_split[2].astype(int)
        df["missed_chars"] = char_split[3].astype(int)
        # Drop original column
        df = df.drop(columns=["charStats"])
        return df
    
    def rename_columns(df):
        df.rename(columns={
            # "_id": "id_data",
            "timestamp": "test_time",
            "rawWpm": "raw_wpm",
            "acc": "accuracy",
            "isPb": "is_pb",
            "quoteLength": "quote_length",
            "testDuration": "test_duration",
            "_id": "test_id"
        }, inplace=True)
        return df

    def outliers(df):
        df = df[(df['wpm'] > 0) & (df['wpm']<250)]
        df = df[(df['accuracy'] > 0) & (df['accuracy'] <= 100)]
        # df = df[df['consistency'] <= 100]
        return df

    def sort_by_time(df):
        df=df.sort_values(by=["test_time"])
        df = df.reset_index(drop=True) # reset index to start from 0 instead of last test index
        return df
        #df['days'] = (df['timestamp'] - df['timestamp'].iloc[0]).dt.days
    #     daily_avg = df.groupby('days').agg({
    #     'wpm':'mean',
    #     'acc':'mean',
    #     'rawWpm':'mean'
    # }).reset_index()
        # return df


    # CALL THE FUNCTIONS
    df = load_csv(csv_path)
    df = drop_columns(df)
    df = remove_nan(df)
    df = change_dtypes(df)
    df = split_char_stats(df)
    df = rename_columns(df)
    df = outliers(df)
    df = sort_by_time(df)
    return df

processed_df=pre_process_csv(csv_path)
