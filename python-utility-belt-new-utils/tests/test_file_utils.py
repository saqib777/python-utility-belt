import unittest
import os
from utils.file_utils import read_lines

class TestFileUtils(unittest.TestCase):

    def test_read_lines_existing_file(self):
        test_file = "temp.txt"
        with open(test_file, "w", encoding="utf-8") as f:
            f.write("line1\nline2\n")
        lines = read_lines(test_file)
        self.assertEqual(lines, ["line1\n", "line2\n"])
        os.remove(test_file)

    def test_read_lines_missing_file(self):
        self.assertEqual(read_lines("missing.txt"), [])

if __name__ == '__main__':
    unittest.main()
