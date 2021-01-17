'''
This is a simple setup for Mood and APIResponse
'''
import Mood
import APIResponse


class Setup:

    def __init__(self, user_input):
        self.user_input = user_input

    def get_response(self):

        # Pass the data to the UserMood class which will
        # return an array of moods ["sad", "joy"...]
        user_mood = Mood.UserMood(self.user_input)
        # Get the frequent mood
        frequent_mood = user_mood.get_mood()
        # Pass in the frequent mood to Response object
        api_response = APIResponse.Response(frequent_mood)
        # return the appropriate joke or quote as needed
        return api_response.caller()


if __name__ == "__main__":

    user_response = ["i am happy", "i am sad", "i am great"]

    test_setup = Setup(user_response)
    print(test_setup.get_response())

