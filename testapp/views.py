from django.shortcuts import render
from django.http import JsonResponse
from . import data as dt
from .modules import doriane as md
from .modules import emmanuelle as me
from .modules import jonas as mjo
from .modules import jerome as mje
from .modules import solenne as ms
from . import utilities as utils


def index(request):
    return render(
        request,
        "testapp/index.html",
    )

def search_data(request):
    if request.method == "POST":
        question = request.body.decode('utf-8').lower()
        parsed_text = ms.parse_text(question)
        place_name = utils.wiki_request_place_name(parsed_text)
        place_json = md.request_place_geodata(place_name)
        story = me.request_place_storydata(place_name)
        return JsonResponse({
            "story": story,
            "lat": place_json["lat"],
            "lon": place_json["lon"],
        })