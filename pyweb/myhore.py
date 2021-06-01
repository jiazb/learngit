import web

render = web.template.render('templates/')
urls = (
        '/(.*)','index'
        )
app = web.application(urls, globals())

class index:
    def GET(self, name):
        if not name:
            name = 'World'
        return render.index(name)

web.webapi.internalerror = web.debugerror
if __name__ == "__main__":
    app.run()
