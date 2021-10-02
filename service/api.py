from flask import Flask, request

from service.geobase import Geobase, DEFAULT_LIMIT


def configure(flask_app: Flask, geobase_module: Geobase):
    @flask_app.route('/search/<text>')
    def search(text):
        limit = int(request.args.get("limit", DEFAULT_LIMIT))
        return "<br />".join(geobase_module.search(text, limit))
