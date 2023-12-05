# class FileReader:
#     def __init__(self,descriptions):
#         self.descriptions=descriptions
#     def __iter__(self):
#         self.file=open(file=self.descriptions)
#         return self
#     def __next__(self):
#         line=self.descriptions.readline()
#         if not line:
#             self.file.close()
#             raise StopIteration
#         return line.strip()
#
# if __name__=='__main__':
#     for line in FileReader("descriptions.txt"):
#         print(line)

#

import csv

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        self.file = open(self.file_path, 'r')
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()

if __name__ == '__main__':
    # Fayl nomi va CSV fayli nomini aniqlang
    input_file_path = "descriptions/001.txt"
    output_csv_path = "descriptions/descriptions/output.csv"

    data = []
    for line in FileReader(input_file_path):
        parts = line.split("|")
        cleaned_parts = [part.strip() for part in parts]
        data.append(cleaned_parts)

    with open(output_csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='|')
        csv_writer.writerows(data)

    print(f"Ma'lumotlar CSV fayliga saqlandi: {output_csv_path}")
    print(line)


