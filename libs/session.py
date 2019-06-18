import json
import pandas as pd
import os


class Session():

    def __init__(self, _user="mohsan"):
        self.user = _user
        self.json_file = os.path.join("./person", self.user, "json_data", "{}.json".format(self.user))
        self.json_store = self.read_json()
        self.defaultSaveDir = os.path.join("./person", self.user, "data/annotation")
        #self.csv_file = os.path.join("./csv_data", "{}.csv".format(self.user))
        self.batches = self.json_store['Batches']  # should have batch_name as key and csv path as value
        self.batch_list = sorted(list(self.batches.keys()))
        self.curr_batch = self.batches[self.batch_list[0]]
        self.csv_file = self.batch_list[0]

        self.data_file = self.read_data_csv()

        self.total = self.data_file.shape[0]
        self.done = self.curr_batch['Done Count']
        self.remain = len(self.data_file.loc[self.data_file['status'] == False])
        self.dirty = len(self.data_file.loc[self.data_file['dirty'] == True])
        print("THE REMAIN are =", self.remain)

    def read_data_csv(self):
        df = pd.read_csv(self.csv_file, sep="|")
        df = df.sort_values(by=['status', 'uid'])
        df = df.sort_values(by=['dirty', 'status'])
        #print(df[['img_file_path','part_en','damage_en', 'action_en']].head())
        return df

    def write_data_csv(self):
        self.data_file.to_csv(self.csv_file, sep="|", index=False)

    def read_json(self):
        with open(self.json_file, 'r') as f:
            return json.load(f)

    def close(self):
        # Save previous Batch
        self.write_data_csv()
        print("Closing Down Session ")

    def update_count(self):
        self.remain = len(self.data_file.loc[self.data_file['status'] == False])
        self.dirty = len(self.data_file.loc[self.data_file['dirty'] == True])
        self.total = self.data_file.shape[0]
#        print("RM = ", self.remain)

    def load_batch(self, batch_csv):
        # Save previous Batch
        self.write_data_csv()
        # Now load new batch
        self.csv_file = batch_csv
        self.curr_batch = self.batches[batch_csv]
        self.data_file = self.read_data_csv()
        self.update_count()
        print(self.curr_batch)
        print("THE REMAIN are =", self.remain)

        #print("load_batch ", batch_csv)
