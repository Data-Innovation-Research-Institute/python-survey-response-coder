import unittest

from survey_response_coder import TransformResponseCoder, MultipleChoiceResponseCoder, MultipleAnswerResponseCoder


def lower(s):
    return s.lower()


def get_response_field(source):
    return source['response']


class SpreadsheetTests(unittest.TestCase):

    def test_transform_response_coding(self):
        coder = TransformResponseCoder(lower)
        response = 'THE QUICK BROWN FOX'
        self.assertEqual(coder.code(response), 'the quick brown fox')

        coder = TransformResponseCoder(lower, accessor=get_response_field)
        self.assertEqual(coder.code(dict(response=response)), 'the quick brown fox')

    def test_multiple_choice_response_coding(self):
        coding_values = [10, 20, 30]

        coder = MultipleChoiceResponseCoder(coding_values)
        self.assertEqual(coder.code(1), 10)
        self.assertEqual(coder.code(2), 20)
        self.assertEqual(coder.code(3), 30)

        coder = MultipleChoiceResponseCoder(coding_values, accessor=get_response_field)
        self.assertEqual(coder.code(dict(response=1)), 10)
        self.assertEqual(coder.code(dict(response=2)), 20)
        self.assertEqual(coder.code(dict(response=3)), 30)

    def test_multiple_answer_response_coding(self):
        coding_values = [10, 20, 30, 40, 50]

        coder = MultipleAnswerResponseCoder(coding_values)
        self.assertEqual(coder.code([1]), 10)
        self.assertEqual(coder.code([1, 2]), 30)
        self.assertEqual(coder.code([1, 2, 3]), 60)
        self.assertEqual(coder.code([1, 2, 3, 4]), 100)
        self.assertEqual(coder.code([1, 2, 3, 4, 5]), 150)

        coder = MultipleAnswerResponseCoder(coding_values, accessor=get_response_field)
        self.assertEqual(coder.code(dict(response=[1])), 10)
        self.assertEqual(coder.code(dict(response=[1, 2])), 30)
        self.assertEqual(coder.code(dict(response=[1, 2, 3])), 60)
        self.assertEqual(coder.code(dict(response=[1, 2, 3, 4])), 100)
        self.assertEqual(coder.code(dict(response=[1, 2, 3, 4, 5])), 150)


if __name__ == '__main__':
    unittest.main()
