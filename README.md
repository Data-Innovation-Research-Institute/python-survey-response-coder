# python-survey-response-coder

![Travis (.org)](https://img.shields.io/travis/Data-Innovation-Research-Institute/python-survey-response-coder.svg)

Code survey responses.

## Install

```bash
pip install git+https://github.com/Data-Innovation-Research-Institute/python-survey-response-coder.git
```

## Use

Import the ```TransformResponseCoder```, ```MultipleChoiceResponseCoder```, and the ```MultipleAnswerResponseCoder``` classes:

```python
from survey_response_coder import TransformResponseCoder,
            MultipleChoiceResponseCoder, MultipleAnswerResponseCoder
```

The ```TransformResponseCoder```, ```MultipleChoiceResponseCoder```, ```MultipleAnswerResponseCoder``` classes share a common method, ```code```, for coding survey responses:

```python
def code(source):
```

Code survey responses by passing the response for a question to the ```code``` method of an instance of a ```xxxResponseCoder``` class.

## Transform Response Coding

The ```TransformResponseCoder``` class transforms a response value by sending it through a transfomer callable passed into the constructor. The following example creates a transform response coder that returns each response value after passing it through the ```lower``` function:

```python
def lower(s):
    return s.lower()

coder = TransformResponseCoder(lower)
response = 'THE QUICK BROWN FOX'
coded_response = coder.code(response)  # returns 'the quick brown fox'
```

If the response is stored in an object or other data structure, supply a callable with the ```accessor``` parameter that returns the response value from the object:

```python
def get_response_field(source):
    return source['response']

coder = TransformResponseCoder(lower, accessor=get_response_field)
response = 'THE QUICK BROWN FOX'
coded_response = coder.code(dict(response=response))  # returns 'the quick brown fox'
```

## Multiple Choice Response Coding

The ```MultipleChoiceResponseCoder``` class codes the single response from a multiple-choice question (as rendered by a set of radio buttons). The response is coded by using it as the index into a list of values passed to the contrstructor. The following example codes the possible responses from a three-option multiple choice question:

```python
coding_values = [10, 20, 30]

coder = MultipleChoiceResponseCoder(coding_values)
coded_response = coder.code(1)  # returns 10
coded_response = coder.code(2)  # returns 20
coded_response = coder.code(3)  # returns 30
```

If the response is stored in an object or other data structure, supply a callable with the ```accessor``` parameter that returns the response value from the object:

```python
def get_response_field(source):
    return source['response']

coder = MultipleChoiceResponseCoder(coding_values, accessor=get_response_field)
coded_response = coder.code(dict(response=1))  # returns 10
coded_response = coder.code(dict(response=2))  # returns 20
coded_response = coder.code(dict(response=3))  # returns 30
```

## Multiple Answer Response Coding

The ```MultipleAnswerResponseCoder``` class codes the multiple responses from a multiple answer question (as rendered by a set of checkboxes). Each item in the list of responses is used as an index into a list of values passed to the constructor. The value at each index is added to a running total. The sum of all the indexed values is returned as the coded response value. The following example codes three values from the possible five that could be selected:

```python
coding_values = [10, 20, 30, 40, 50]

coder = MultipleAnswerResponseCoder(coding_values)
coded_response = coder.code([1, 3, 4])  # returns 80
```

If the response is stored in an object or other data structure, supply a callable with the ```accessor``` parameter that returns the response value from the object:

```python
def get_response_field(source):
    return source['response']

coder = MultipleAnswerResponseCoder(coding_values, accessor=get_response_field)
self.assertEqual(coder.code(dict(response=[1, 3, 4]))  # returns 80
```
