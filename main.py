from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

data = [
  {
    "id": "1",
    "attributes": {
        "name": "Frodo Baggins",
        "born": "September 22, 2968 of the Third Age",
        "died": "Unknown (departed Middle-earth in the Fourth Age)",
        "image": "https://s0.rbk.ru/v6_top_pics/media/img/5/13/347149765055135.jpeg"
    }
  },
  {
    "id": "2",
    "attributes": {
        "name": "Samwise Gamgee",
        "born": "April 6, 2980 of the Third Age",
        "died": "Unknown (departed Middle-earth in the Fourth Age)",
        "image": "https://avatars.mds.yandex.net/i?id=bd36f8dcbe6db752433057b288a5ad78c73c246e-9237081-images-thumbs&ref=rim&n=33&w=339&h=250"
    }
  },
  {
    "id": "3",
    "attributes": {
        "name": "Aragorn",
        "born": "March 1, 2931 of the Third Age",
        "died": "March 1, 120 of the Fourth Age",
        "image": "https://cdn.vox-cdn.com/thumbor/9SR6EQb0ie534xcmQxvJLh-csR8=/0x0:3840x1596/1200x800/filters:focal(2059x489:2673x1103)/cdn.vox-cdn.com/uploads/chorus_image/image/73337214/4k_fellowship_movie_screencaps.com_12336.0.jpg"
    }
  },
  {
    "id": "4",
    "attributes": {
        "name": "Gandalf",
        "born": "Unknown (known as the Maia Olórin)",
        "died": "Not applicable (immortal)",
        "image": "https://avatars.mds.yandex.net/i?id=bd36f8dcbe6db752433057b288a5ad78c73c246e-9237081-images-thumbs&ref=rim&n=33&w=339&h=250"
    }
  },
  {
    "id": "5",
    "attributes": {
        "name": "Legolas",
        "born": "Unknown (a Sindarin Elf)",
        "died": "Unknown (departed Middle-earth with Gimli)",
        "image": "https://i.pinimg.com/originals/7c/5b/a9/7c5ba9b51616b629265dfd2eb0045037.jpg"
    }
  },
  {
    "id": "6",
    "attributes": {
        "name": "Gimli",
        "born": "2879 of the Third Age",
        "died": "Unknown (departed Middle-earth with Legolas)",
        "image": "https://img.atlasobscura.com/KtyGt-W6P4O_M_qGT-8xkuWPFb0BHRx149VUttqMWGA/rt:fit/w:1280/q:81/sm:1/scp:1/ar:1/aHR0cHM6Ly9hdGxh/cy1kZXYuczMuYW1h/em9uYXdzLmNvbS91/cGxvYWRzL2Fzc2V0/cy85Nzk3YTZiZC03/NTI4LTRjNjItYjZj/MC0wYjkwMDM3M2Yw/NzhhNzA3YTNiYzY2/YWVlMDYzNzhfR2lt/bGkgaW4gVEhFIExP/UkQgT0YgVEhFIFJJ/TkdTX1RIRSBUV08g/VE9XRVJTX1JZQ0sx/OC5qcGc.jpg"
    }
  },
  {
    "id": "7",
    "attributes": {
        "name": "Boromir",
        "born": "2978 of the Third Age",
        "died": "February 26, 3019 of the Third Age",
        "image": "https://avatars.mds.yandex.net/i?id=bd36f8dcbe6db752433057b288a5ad78c73c246e-9237081-images-thumbs&ref=rim&n=33&w=339&h=250"
    }
  },
  {
    "id": "8",
    "attributes": {
        "name": "Galadriel",
        "born": "Unknown (one of the first Elves of Middle-earth)",
        "died": "Not applicable (departed Middle-earth in the Fourth Age)",
        "image": "https://avatars.mds.yandex.net/i?id=bd36f8dcbe6db752433057b288a5ad78c73c246e-9237081-images-thumbs&ref=rim&n=33&w=339&h=250"
    }
  },
  {
    "id": "9",
    "attributes": {
        "name": "Sauron",
        "born": "Unknown (known as a Maia)",
        "died": "Third Age 3019 (loss of physical form)",
        "image": "https://avatars.mds.yandex.net/i?id=bd36f8dcbe6db752433057b288a5ad78c73c246e-9237081-images-thumbs&ref=rim&n=33&w=339&h=250"
    }
  },
  {
    "id": "10",
    "attributes": {
        "name": "Gollum (Sméagol)",
        "born": "Circa 2430 of the Third Age",
        "died": "March 25, 3019 of the Third Age",
        "image": "https://avatars.mds.yandex.net/i?id=bd36f8dcbe6db752433057b288a5ad78c73c246e-9237081-images-thumbs&ref=rim&n=33&w=339&h=250"
    }
  }
]


@app.get("/characters")
async def get_characters(
    name: Optional[str] = Query(None, description="Поиск по имени"),
    page: int = Query(1, ge=1, description="Номер страницы"),
    size: int = Query(10, ge=1, description="Размер страницы")
) -> dict:
    filtered_data = (
        [item for item in data if name.lower() in item["attributes"]["name"].lower()]
        if name else data
    )

    start_index = (page-1) * size
    end_index = page * size
    paginated_data = filtered_data[start_index:end_index]

    return {
        "meta": {
          "pagination": {
              "next": page+1
          }
        },
        "data": paginated_data
    }
