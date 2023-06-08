"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for key, val in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story_1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
)

story_2 = Story(
    [
        "noun",
        "adjective",
        "noun",
        "noun",
        "noun",
        "noun",
        "type_of_food",
        "noun",
        "noun",
        "adjective",
    ],
    """Planting a vegetable garden is not only fun, it also helps save {noun}. 
    You will need a piece of {adjective} land. You may need a {noun} to keep the {noun} and {noun} out. 
    As soon as {noun} is here you can go out there with your {type_of_food} and plant all kinds of {noun}. 
    Then in a few months you will have corn on the {noun} and big, {adjective} flowers.""",
)

story_3 = Story(
    [
        "person",
        "place",
        "adjective",
        "place",
        "plural_noun",
        "adjective",
        "plural_noun",
        "place",
        "verb",
        "plural_noun",
        "plural_noun",
        "noun",
        "verb",
        "noun",
        "adjective",
    ],
    """Last summer, my mom and dad took me and {person} on a trip to {place}. The weather there is very {adjective}! 
    Northern {place} has many {plural_noun}, and they make {adjective} {plural_noun} there. 
    Many people also go to {place} to {verb} or see the {plural_noun}. 
    The people that live there love to eat {plural_noun} and are very proud of their big {noun}. 
    They also like to {verb} in the sun and swim in the {noun}! It was a really {adjective} trip!""",
)
