''' The Response class takes in what is to
    be sent to the user according to their mood.
'''
import http.client
import json


class Response:
    '''Takes in the mood of the user as the parameter'''
    def __init__(self, the_mood):
        self.the_mood = the_mood

    '''Calls the appropriate function based on the mood'''
    def caller(self):

        if self.the_mood == "fear" or self.the_mood == "anger":
            return Response.get_joke()
        else:
            return Response.get_quote()

    '''Get jokes from an API'''
    @staticmethod
    def get_joke():
        conn = http.client.HTTPSConnection("webknox-jokes.p.rapidapi.com")

        headers = {
            'x-rapidapi-key': "bde030e572msh1318307d4a97d77p10602djsn3c5afcc9078c",
            'x-rapidapi-host': "webknox-jokes.p.rapidapi.com"
        }

        conn.request("GET", "/jokes/random?maxLength=100&minRating=8", headers=headers)

        res = conn.getresponse()
        data = res.read()
        joke = data.decode("utf-8")
        return joke

    '''Gets quotes from an API'''
    @staticmethod
    def get_quote():

        conn = http.client.HTTPSConnection("andruxnet-random-famous-quotes.p.rapidapi.com")

        headers = {
            'x-rapidapi-key': "bde030e572msh1318307d4a97d77p10602djsn3c5afcc9078c",
            'x-rapidapi-host': "andruxnet-random-famous-quotes.p.rapidapi.com"
        }

        conn.request("POST", "/?cat=movies&count=10", headers=headers)

        res = conn.getresponse()
        data = res.read()
        json1_data = json.loads(data)
        return json1_data[0]["quote"]


if __name__ == "__main__":
    mood = "sadness"
    mood2 = "fear"
    test_Response = Response(mood2)
    print(test_Response.caller())


