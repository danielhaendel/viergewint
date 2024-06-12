class SmartFastField:
    def __init__(self, x=7, y=6):
        self.fieldX = x
        self.fieldY = y

        self.row = []

        i = 0
        while i < self.fieldY+1:
            self.row.append([])
            j = 0
            while j < self.fieldX+1:
                self.row[i].append(0)
                j+=1

            i += 1

    def insert(self, key, value):
        column = self.row[int(key[0])-1]
        column.insert(int(key[1])-1, value)

    def get(self, key):
        return self.row[int(key[0])-1][int(key[1])-1]