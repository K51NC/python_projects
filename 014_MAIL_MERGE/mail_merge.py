class MailMerge:

    def __init__(self):
        pass

    def get_file_contents(self, names_file):
        with open(names_file, "r") as file:
            return file.read()
        
    def output_new_file(self, output_file, file_name, output_location):
        with open(f"{output_location}{file_name}.txt", "w") as file:
            file.write(output_file)
    
    def replace_name(self, name, letter):
        new_letter = letter.replace("[name]", name)
        return new_letter