import unittest
import converter

INPUT_CODE_DELIMITER = '# ---end----'

class Testconv(unittest.TestCase):

    def test_read(self):
        result = converter.read_data('solution.py')
        self.assertTrue(result)

    def test_write(self):
        content = converter.read_data('solution.py')
        data = converter.convert_data(content)
        result = converter.write_data('matrix.md',data)

    def test_add(self):
        content = converter.read_data('solution.py')
        data = converter.convert_data(content)
        add_data=converter.add_data(data,data)
        self.assertIsNotNone(add_data)

    def test_prepraremd(self):
        content = converter.read_data('solution.py')
        data = converter.convert_data(content)
        a = converter.prepare_md_titles(data)
        self.assertIsNotNone(a)

    def test_convert(self):
        content = converter.read_data('solution.py')
        md = converter.convert_data(content)
        self.assertTrue(md)



if __name__ == '__main__':
    unittest.main()