from cgitb import reset
import os
from urllib import response
import requests
from todo_app.data.list import List
from todo_app.data.card import Card


def get_list_cards(list_id, status):
    result = requests.get(f'https://api.trello.com/1/lists/{list_id}/cards?key={os.getenv("SECRET_KEY")}&token={os.getenv("TOKEN")}')
    if (result.status_code == 200):
        card_array = []
        for card in result.json():
            card_array.append(
                Card(card["id"], card["name"], status, card["desc"])
            )
    return card_array

def get_lists():
    result = requests.get(f'https://api.trello.com/1/boards/{os.getenv("BOARD_ID")}/lists?key={os.getenv("SECRET_KEY")}&token={os.getenv("TOKEN")}')
    if (result.status_code == 200):
        list_json = result.json()
        list_array = []
        for list in list_json:
            list_array.append(
                List(list["id"], list["name"])
            )
        return list_array

# def get_astronomy_pic_of_day():
#     r = requests.get(
#         f'https://api.nasa.gov/planetary/apod?api_key={os.getenv("API_KEY")}')
#     if (r.status_code == 200):
#         return r.json()


# def get_mars_pic(date_to_get):
#     r = requests.get(
#         f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date_to_get}&page-1&api_key={os.getenv("API_KEY")}')
#     if (r.status_code == 200):
#         return r.json()



# components
# <div class="d-flex flex-wrap">
#   {% for item in data %} {{ image_block(item["img_src"], "test") }} {% endfor %}
# </div>

# {% macro image_block(image_url, description) %}
#   <div class="card">
#     <img class="card-img-top" src="{{image_url}}" />
#     {% if description %}
#     <div class="card-body">
#       <p class="card-text">{{ description }}</p>
#     </div>
#     {% endif %}
#   </div>
# {% endmacro %}
