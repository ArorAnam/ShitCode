import random

class TimeStamp:
    def __init__(self) -> None:
        self.values_dict = {}
        self.timestamp_dict = {}

    # set timestamp data variables
    def set_value(self, key, value, timestamp):
        if key in self.values_dict:
            if value != self.values_dict[key][len(self.values_dict[key]) - 1]:
                self.values_dict[key].append(value)
                self.timestamp_dict[key].append(timestamp)
        else:
            self.values_dict[key] = [value]
            self.timestamp_dict[key] = [timestamp]

    def search_index(self, n, key, timestamp):
        left = 0
        right = n
        mid = 0
        while left < right:
            mid = left + (right - left) // 2

            if self.timestamp_dict[key][mid] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return left-1


    # get timestamp data variables
    def get_value(self, key, timestamp):
        if key not in self.values_dict:
            return ""
        else:
            index = self.search_index(len(self.timestamp_dict[key]), key, timestamp)
            if index > -1:
                return self.values_dict[key][index]

            return ""


def main():
    ts = TimeStamp()
    num = 1
    random_value = 0
    input = (
        ("course", "OOP", 3),
        ("course", "PF", 5),
        ("course", "OS", 7),
        ("course", "ALGO", 9),
        ("course", "DB", 10),
    )

    for i in input:
        ts.set_value(i[0], i[1], i[2])
        random_value = random.randint(0, 10)
        res = ts.get_value("course", random_value)
        print(res)


if __name__ == "__main__":
    main()