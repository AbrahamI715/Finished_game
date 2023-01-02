import csv


class FileInteractions:
    def __init__(self):
        self.level_scores_data = [{"level": 1, "kills": 0, "coins": 0},
                                  {"level": 2, "kills": 0, "coins": 0},
                                  {"level": 3, "kills": 0, "coins": 0},
                                  {"level": 4, "kills": 0, "coins": 0}
                                  ]

    def load(self):  # LOAD FROM FILE INTO CLASS
        high_scores_data = []  # temporary empty list
        # open the file and assign it to the variable "csv_file"
        with open('high_scores_data.csv', 'r') as csv_file:
            # the DictReader acts like a record data structure
            # it will return a list of dictionaries
            # each line is one dictionary
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                # write each dictionary to the temporary list
                high_scores_data.append(line)
            # copy temporary list into top ten
            self.level_scores_data = high_scores_data

    def save(self):  # SAVE FROM CLASS INTO FILE
        # open the file and assign it to the variable "csv_file"
        with open('high_scores_data.csv', 'w') as csv_file:
            # these are the headers e.g. the headers in a normal table
            field_names = ['level', 'kills', 'coins']
            # here we write the headers of the table
            # you have to rewrite the headers every time you write
            # because "write" deletes the entire contents of the file every time
            csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
            csv_writer.writeheader()  # write the headers
            for line in self.level_scores_data:  # loop through list
                csv_writer.writerow(line)  # write the data into file

    def add_high_score(self, level, player_kills, player_coins):

        # level_scores_data is a list of dictionaries
        # so we first use [level] as an index to find the dict we want
        # then we use "score" to get the "score" bit of the dictionary
        # and check if the player's score is bigger than the current high score for that level
        current_kills = self.level_scores_data[level - 1]["kills"]
        current_coins = self.level_scores_data[level - 1]["coins"]
        if int(current_kills) < player_kills:
            self.level_scores_data[level - 1]["kills"] = player_kills
        if int(current_coins) < player_coins:
            self.level_scores_data[level - 1]["coins"] = player_coins


