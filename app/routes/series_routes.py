from flask import Blueprint, render_template, request
from app.services.series_service import SeriesService

series_bp = Blueprint("series", __name__)
series_service = SeriesService()

@series_bp.route("/", methods=["GET"])
def home():
    query = request.args.get("query", "").strip()
    data = None

    if query:
        data = series_service.search_series_data(query)

    return render_template("index.html", data=data, query=query)

@series_bp.route("/offline", methods=["GET"])
def offline():
    return render_template("offline.html")