import pandas as pd
import numpy as np
import math
import random

class DataPreprocessing:
    def __init__(self, input_file_path, output_file_path):
        self.df = pd.read_csv(input_file_path)
        self.output_file_path = output_file_path

    def calculate_column_means(self):
        numeric_columns = self.df.select_dtypes(include=[np.number])
        total = {}
        count = {}
        for index, values in numeric_columns.iterrows():
            for column, value in values.items():
                if pd.notna(value):
                    total[column] = total.get(column, 0) + value
                    count[column] = count.get(column, 0) + 1
        self.mean = {column: total[column]/count[column] for column in total}
        for column, value in numeric_columns.items():
            for col,val in enumerate(value):
                if math.isnan(float(val)):
                    numeric_columns[column][col]=self.mean[column]
        numeric_columns.to_csv(self.output_file_path, index=False)
    def scale_numeric_columns(self):
        self.newdf = pd.read_csv(self.output_file_path)
        numeric_columns = self.newdf.select_dtypes(include=[np.number])
        weight = numeric_columns['Weight']
        sweetness=numeric_columns['Sweetness']
        min_values=[min(weight),min(sweetness)]
        max_values=[max(weight),max(sweetness)]
        for i in range(len(numeric_columns)):
            numeric_columns.iloc[i,1] =(numeric_columns.iloc[i,1] -min_values[0]) / (max_values[0] - min_values[0])
            numeric_columns.iloc[i,2] =(numeric_columns.iloc[i,2] -min_values[1]) / (max_values[1] - min_values[1])
        numeric_columns.to_csv(self.output_file_path,index=False)

    def one_hot_encode(self, column_name):
        self.newdf = pd.read_csv(self.output_file_path)
        self.newdf[column_name] = self.df[column_name]
        column = self.newdf[column_name]
        mode = column.mode().iloc[0]
        column.fillna(mode, inplace=True)
        self.newdf.to_csv(self.output_file_path,index=True)
        unique_values = column.unique()

        for value in unique_values:
            self.newdf[value] = (self.newdf[column_name] == value).astype(int)

    def label_encode(self, column_name, target_value):
        self.newdf[column_name] = self.df[column_name]
        column = self.newdf[column_name]
        self.newdf[column_name] = (column == target_value).astype(int)

    def save_to_csv(self):
        self.newdf.to_csv(self.output_file_path, index=False)
    
    def split_data(self, test_size=0.2):
        data = self.newdf.values.tolist()
        random.shuffle(data)
        split_index = int(len(data) * (1 - test_size))
        train_data = data[:split_index]
        test_data = data[split_index:]
        train_df = pd.DataFrame(train_data, columns=self.newdf.columns)
        test_df = pd.DataFrame(test_data, columns=self.newdf.columns)
        train_df.to_csv('Preprocess_train.csv', index=False)
        test_df.to_csv(('Preprocess_test.csv'), index=False)


def main():
    preprocessor = DataPreprocessing(input_file_path='ML-Set1.csv', output_file_path='ML-Set2.csv')
    preprocessor.calculate_column_means()
    preprocessor.scale_numeric_columns()
    preprocessor.one_hot_encode(column_name='Country')
    preprocessor.save_to_csv()
    preprocessor.label_encode(column_name='Quality', target_value='good')
    preprocessor.save_to_csv()
    preprocessor.split_data(test_size=0.2)
main()
