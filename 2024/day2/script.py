#!/usr/bin/env python

# rules
#
# [7 6 4 2 1]: Safe because the levels are all decreasing by 1 or 2.
# [1 2 7 8 9]: Unsafe because 2 7 is an increase of 5.
# [9 7 6 2 1]: Unsafe because 6 2 is a decrease of 4.
# [1 3 2 4 5]: Unsafe because 1 3 is increasing but 3 2 is decreasing.
# [8 6 4 4 1]: Unsafe because 4 4 is neither an increase or a decrease.
# [1 3 6 7 9]: Safe because the levels are all increasing by 1, 2, or 3.
#
# So, in this example, 2 reports are safe.
# ========================================================================

MAX = 3
MIN = 1


class Solve:
    def __init__(self, file: str) -> None:
        self.file = file

    def parse_file(self, fptr) -> list:
        read_file = open(fptr, "r").read()
        contents = read_file.splitlines()
        return contents

    # [TODO]
    def first_challenge(self) -> None:
        parsed = self.parse_file(self.file)
        print(parsed)

    def second_challenge(self) -> None:
        return


if __name__ == "__main__":
    # put input into `./input.txt` file
    solved = Solve("./input.txt")
    first_answer = solved.first_challenge()  # solve the first challenge

    print(first_answer)
