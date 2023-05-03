import random

R_NAME = "My name is chat bot!"
R_ARTIFICIAL = "Artificial intelligence is the simulation of human intelligence processes by machines, especially computer systems."
R_GIT = "GitHub is an online software development platform. It's used for storing, tracking, and collaborating on software projects."
def unknown():
    response = ['could you please re-phrase that?',
                "...",
                "sounds about right",
                "what does that mean?"][random.randrange(4)]
    return response