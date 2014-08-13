import urllib2
import csv

class DotaDumper():
    def __init__(self):
        with open("HeroList.txt") as file_list:
            self.hero_list = file_list.readlines()
            self.list_length = len(self.hero_list)
            for i in range(0, self.list_length):
                self.hero_list[i] = self.hero_list[i].lower().replace(" ", "-").translate(None,"'").replace("\n", "")

    # Writes the table of match-up data into a csv file
    def write_table(self):
        with open ("data.csv", "wb+") as f_out:
            csvwriter = csv.DictWriter(f_out, fieldnames = self.hero_list)
            csvwriter.writeheader()
            for i in range(0, self.list_length):
                csvwriter.writerow(self.save_source_code(self.hero_list[i]))
                print int(i), "/", int(self.list_length)

    # Fetches the source code for the matchup page of the passed hero
    def save_source_code(self, hero):
        response = urllib2.urlopen("http://dotabuff.com/heroes/"+str(hero)+"/matchups")
        source_code = response.read()
        row = {}
        for match_up in self.hero_list:
            index = source_code.index(match_up+'"')
            if hero == match_up:
                row[match_up] = ""
            else:
                row[match_up] = self.get_val(source_code, index)
        return row

    # gets the match-up value at the passed index
    def get_val(self, source_code, index):
        val_index = str(source_code).index("%", index)
        val = str(source_code[val_index-6:val_index])
        val = float(val.translate(None,"<td>"))
        return val
'''
dumper = DotaDumper()
print dumper.hero_list
dumper.write_table()
'''