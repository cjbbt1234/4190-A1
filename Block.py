class Blcok:

    def __init__(self,cell_list):
        self.cell_list = cell_list

    def count_stars(self):
        count = 0
        for x in self.cell_list:
            if self.cell_list[x].status == 1:
                count += 1
        return count




