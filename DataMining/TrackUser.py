from sqlite3 import connect
import tweepy
from tweepy import OAuthHandler, Stream, StreamListener

# claves de acceso de la ap

access_token =
access_token_secret =
consumer_key =
consumer_secret =


# print resultados
class tweetListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


# seteamos credenciales
if __name__ == '__main__':
    l = tweetListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(follow=['2831923512'])



    # filtro de busqueda!!!!!!!!!! solo buscara mensajes que contengan los siguientes caracteres
    #stream.filter(track=['python', 'java', 'javascript', 'c#', 'c++'], is_async=True)
    # twitterStream.filter(track=['UserName']) worked for me.
    # filtro ,languages =['es']
