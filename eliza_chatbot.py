# importing regex and random module which is used to select a value at random from list
import re
import random

# declaring a dictionary of responses for few general statements
qes_ans = {'[Hh]ow are you?': [r"I'm fine, thank you."],
           
           "[Ii] need (.*)" : [r"Why and what for, do you need \1?",
                               r"Would it really be useful if you got \1?",
                               r"Are you certain you require \1?"
                              ],
           
           "[Ii] am (.*)"   : [r"Are you here as you are \1?",
                               r"Why do you think you are \1?",
                               r"What is making you \1?"
                              ],
           
           "[Ii] think (.*)": [r"What makes you think that?",
                               r"Are you sure?",
                               r"You think \1 because of?"
                              ],
           
           "[Ii] feel (.*)" : [r"Could you elaborate about this?",
                               r"On a scale of 1-10 how strong is this feeling of \1?",
                               r"How often do you usually feel \1?",
                               r"Since when are you feeling this \1?"
                              ],
           
           "[Ii] have (.*)" : [r"How do you feel since you have \1?",
                               r"Why do you have \1?",
                               r"Keeping in mind that you have \1, what has changed?"
                              ],
           
           "[Ii] would (.*)": [r"Could you explain why you would \1?",
                               r"Why would you \1?",
                               r"Who else knows that you would \1?"
                              ],
           
           "[Ii] want (.*)" : [r"What would it mean to you if you got \1?",
                               r"Why do you want \1?",
                               r"What would you do if you got \1?",
                               r"If you got \1, then what would you do?"
                              ],
           
           "[Ii] (don't|dont) (.*)": [r"Are you sure about this?",
                                      r"Why don't you want \2?",
                                      r"Do you want to not\2?"
                                     ],
           
           "[Ii] (can't|cant) (.*)": [r"Why are you so sure you can't \2?",
                                      r"If you tried harder maybe you could \2",
                                      r"What motivation do you need to \2?"
                                     ],
           
           "[Bb]ecause (.*)": [r"Is that the real reason?", 
                               r"Can you think of any more reasons?", 
                               r"It may or may not be true.",
                               r"Are you planning to overcome that?"
                              ],
           
           "\b[Yy]es\b"         : [r"You seem quite sure.",
                               r"OK, but how are you so sure?"],
           
           "\b[Nn]o\b"          : [r"Why not?"],
           
           "Can you (.*)": [r"What makes you think I can't \1?", 
                            r"If I could \1, then what?", 
                            r"Why do you ask if I can \1?"],
           
           "Can I (.*)"  : [r"Perhaps you don't want to \1.", 
                            r"Do you want to be able to \1?",
                            r"If you could \1, would you?"],
           
           "(.+)"        : [r"Please tell me more.",
                            r"Let's change focus a bit... Tell me about your family.",
                            r"Can you elaborate on that?",
                            r"Why do you say that",
                            r"I see.",
                            r"Very interesting.",
                            r"I see.  And what does that tell you?",
                            r"How does that make you feel?",
                            r"How do you feel when you say that?"
                           ],
           
          "[Qq]uit"      : [r"Thank you for talking with me.",
                            r"Good-bye.",
                            r"Looking forward to talking with you again",
                            r"Thank you.  Hope you have a good day!"
                           ],
          }

# function response which takes input and matches with all the keys in the dictionay and replaces with the value
def response(sen):
# iterating throught the dictionary
    for key, val in qes_ans.items():
# finding the match with keys in dictionary
        match = re.match(key, sen)
# checking if there is match
        if match is not None:
# if there is a match then replacing it with one of the random response from the list with the help of random module
            res = re.sub(key, random.choice(val), sen)
            return res

# Main Program
print("Hello.  How are you feeling today?")
sentence = ""
# running a loop until the user inputs quit and by default taking an empty statement
while sentence != "quit":
# taking input from user    
    sentence = input(">")
# checking if the statement is ending with a dot or exclamation and removing it    
    if sentence[-1] in "!.":
        sentence = sentence[:-1]
# calling the response function which checks the dictionay and gives the exact response        
    print(response(sentence))