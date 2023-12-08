"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["333388822211177"],
            "answer": "4338323127",
        },
        {
            "input": ["1"],
            "answer": "11",
        },
        {
            "input": [""],
            "answer": "",
        },
    ],
    "Extra": [
        {
            "input": ["11221122"],
            "answer": "21222122",
        },
        {
            "input": ["123456789"],
            "answer": "111213141516171819",
        },
        {
            "input": ["777777777777777"],
            "answer": "157",
        },
    ]
}
