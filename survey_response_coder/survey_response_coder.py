class SurveyResponseCoder:
    """The abstract base class for response coders"""

    def __init__(self, accessor=None):
        self.accessor = accessor

    def access_value(self, source):
        """If there's an accessor callable, use it to access the value in the source"""
        if self.accessor:
            return self.accessor(source)
        else:
            return source


class TransformResponseCoder(SurveyResponseCoder):
    """Apply a transformer callable to the source"""

    def __init__(self, transformer, accessor=None):
        super().__init__(accessor)
        self.transformer = transformer

    def code(self, source):
        value = self.access_value(source)
        return self.transformer(value)


class MultipleChoiceResponseCoder(SurveyResponseCoder):
    """Map the single numeric index source onto an element of the values list"""

    def __init__(self, values, accessor=None):
        super().__init__(accessor)
        self.values = values

    def code(self, source):
        value = self.access_value(source)
        index = int(value) - 1
        return self.values[index]


class MultipleAnswerResponseCoder(SurveyResponseCoder):
    """Return the sum of the values indexed by the source"""

    def __init__(self, values, accessor=None):
        super().__init__(accessor)
        self.values = values

    def code(self, source):
        indexes = self.access_value(source)
        total = 0
        for index in indexes:
            total += self.values[int(index) - 1]
        return total
