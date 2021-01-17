# Class UserMood takes in an array of responses from the user
# and determines the most frequent mood the user is currently
# experiencing.
#
import Model


class UserMood:
    ''' The constructor takes in an array of user responses '''
    def __init__(self, the_user_response):
        self.the_user_response = the_user_response

    ''' The method creates a Model object from the 
    user response. The Model object returns an array of
    moods the user has and this function will return the 
    most frequent mood experienced by the user
    '''
    def get_mood(self):

        # Create the object from the Model class
        model = Model.model(self.the_user_response)

        # Get the array of the moods the user has i.e ["sad", "joy"...]
        moods = model.response()
        # Keep track of the highest frequency of mood
        mood_count = {}
        max_value = 0
        for user_mood in moods:

            if user_mood in mood_count:
                mood_count[user_mood] += 1
                max_value = max(max_value, mood_count[user_mood])
            else:
                mood_count[user_mood] = 1

        # Return the highest frequency mood
        for key, freq in mood_count.items():
            if freq == max_value:
                return key


if __name__ == "__main__":

    user_response = ["i am happy", "i am sad", "i am great"]
    test_mood = UserMood(user_response)
    print(test_mood.get_mood())



