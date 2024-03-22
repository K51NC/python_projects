import pandas

class FileHandler:

    def __init__(self):
        pass

    def load(self, save_location):
        save_data = pandas.read_csv(save_location, index_col=0).to_dict()
        return save_data

    def save(self, data, save_loc, current_time, time_loc):
        save_file = pandas.DataFrame(data)
        save_file.to_csv(save_loc)
        with open(time_loc, "w") as file:
            file.write(str(round(current_time, 2)))

    def create_default(self):
        data = {
            "state": {},
            "x": {},
            "y": {}
            }
        return data
    
    def reset(self, save_loc, time_loc):
        while True:
            try:
                with open(save_loc, "w") as file:
                    file.write("")
                with open(time_loc, "w") as file:
                    file.write("0")
                break
            except:
                print("ERROR: FileHandler.reset failed to reset save file data.")
                break