from obs import star


class SmartFastField:
    isWon = False

    def __init__(self, x=7, y=6):
        self.fieldX = x
        self.fieldY = y

        self.row = []

        i = 0
        while i < self.fieldY + 1:
            self.row.append([])
            j = 0
            while j < self.fieldX + 1:
                self.row[i].append(0)
                j += 1

            i += 1

    def insert(self, key, value): # "12"
        column = self.row[int(key[0]) - 1]
        column[int(key[1]) - 1] = value

        self.istWon(key)


    def get(self, key):
        try:
            x = int(key[0])
            y = int(key[1])
            if x > self.fieldX:
                return None

            if y > self.fieldY:
                return None

            return self.row[x - 1][y - 1]
        except:
            return None

    def insertIntoRow(self, row, value):
        column = self.fieldY
        while column >= 1:
            key = str(row) + str(column)
            field = self.get(key)
            if (field == 0):
                self.insert(key, value)
                return True
            else:
                column -= 1
                if column <= 0:
                    return False

    def istWon(self, key):
        field = self.get(key)
        star = self.star(key)
        for name, ar in star.items():
            if (field == ar[0]) and (field == ar[1]) and (field == ar[2]):
                print(name)
                self.isWon = True

    def star(self, key):
        return star.get(self, key)
