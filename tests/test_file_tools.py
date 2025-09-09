import unittest
import os
from utils.file_tools import file_exists, append_to_file, write_file, read_file

class TestFileTools(unittest.TestCase):
    def setUp(self):
        self.test_file = "temp_test.txt"
        write_file(self.test_file, "start")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_file_exists(self):
        self.assertTrue(file_exists(self.test_file))
        self.assertFalse(file_exists("not_there.txt"))

    def test_append_to_file(self):
        append_to_file(self.test_file, " + more")
        content = read_file(self.test_file)
        self.assertEqual(content, "start + more")

if __name__ == "__main__":
    unittest.main()
