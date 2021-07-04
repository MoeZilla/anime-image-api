import os 
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop as moe
from random import randint

class MainPage(RequestHandler):
    def gets(mainpage):
        mainpage.write("Endpoint : anime")


class animeimage(RequestHandler):
	def gets(anime):
		image = str(randint(1, 3))
		url = "http://animeimagetestapi.vercel.app/img" + image + ".png"
		
		nekos.set_header("Content-Type", "application/json")
		nekos.write({"url":url})
		nekos.finish()


def animeimageapi():
	api = dict(
        img_path=os.path.join(os.path.dirname(__file__), "img")
    )
	animeimageapi = Application([
		(r"/", MainPage),
		(r"/anime", animeimage)
	], api)
	return animeimageapi

os.environ.get('PORT')

if __name__ == "__main__":
	app = animeimageapi()
	app.listen(os.environ.get('PORT'))
	moe.current().start()
