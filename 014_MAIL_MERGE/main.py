from mail_merge import MailMerge

merger = MailMerge()


# change these according to your own file locations
names_file = "./014_MAIL_MERGE/input/names.txt"
letter_template_file = "./014_MAIL_MERGE/input/letter_template.txt"
output_location = "./014_MAIL_MERGE/output/"


names = merger.get_file_contents(names_file).split()
letter = merger.get_file_contents(letter_template_file)


for name in names:
    new_filename = "letter_for_" + name
    new_letter = merger.replace_name(name, letter)
    merger.output_new_file(new_letter, new_filename, output_location)
