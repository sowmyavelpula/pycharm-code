import re  #for rejects
import response as resp #a file which stores the responses

# the following def is used to calculate the probability of message given by the user matching with the predefined message
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0 #the percentage of words given by user matched with the message
    has_required_words = True

    #counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    #calculatee the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    #checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_messages(message):
        highest_prob_list = {} #empty dictionary

        # Simplifies response creation / adds it to the dict
        def response(bot_response, list_of_words, single_response=False, required_words=[]):
            nonlocal highest_prob_list
            highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
        response('I\m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
        response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

        response(resp.R_NAME, ['what', 'is', 'your', 'name'], required_words=['what', 'name'])
        response(resp.R_ARTIFICIAL, ['what', 'is', 'artificial intelligence'], required_words=['what', 'artificial intelligence'])
        response(resp.R_GIT, ['what', 'is', 'github'], required_words=['what', 'github'])

        best_match = max(highest_prob_list, key=highest_prob_list.get)
        #print(highest_prob_list)

        return resp.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())   #split is to split the word by which we can analyse every word and the symbols which we provided will remove that symbols from the words
    response = check_all_messages(split_message)
    return response


#TESTING THE RESPONSE System
#for infinite while loops, So we can always get new responses
while True:
    print('Bot: ' + get_response(input('You: ')))



