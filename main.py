from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

data = [
  {
    "id": "1",
    "attributes": {
      "name": "Фродо Бэггинс",
      "born": "22 сентября 2968 Третьей Эпохи",
      "died": "Неизвестно (покинул Средиземье в Четвертой Эпохе)",
      "image": "https://example.com/images/frodo.jpg"
    }
  },
  {
    "id": "2",
    "attributes": {
      "name": "Сэмвайз Гэмджи",
      "born": "6 апреля 2980 Третьей Эпохи",
      "died": "Неизвестно (покинул Средиземье в Четвертой Эпохе)",
      "image": "https://example.com/images/sam.jpg"
    }
  },
  {
    "id": "3",
    "attributes": {
      "name": "Арагорн",
      "born": "1 марта 2931 Третьей Эпохи",
      "died": "1 марта 120 Четвертой Эпохи",
      "image": "https://example.com/images/aragorn.jpg"
    }
  },
  {
    "id": "4",
    "attributes": {
      "name": "Гэндальф",
      "born": "Неизвестно (известен как Майар Олорин)",
      "died": "Не применимо (бессмертен)",
      "image": "https://example.com/images/gandalf.jpg"
    }
  },
  {
    "id": "5",
    "attributes": {
      "name": "Леголас",
      "born": "Неизвестно (синдарский эльф)",
      "died": "Неизвестно (покинул Средиземье с Гимли)",
      "image": "https://example.com/images/legolas.jpg"
    }
  },
  {
    "id": "6",
    "attributes": {
      "name": "Гимли",
      "born": "2879 Третьей Эпохи",
      "died": "Неизвестно (покинул Средиземье с Леголасом)",
      "image": "https://example.com/images/gimli.jpg"
    }
  },
  {
    "id": "7",
    "attributes": {
      "name": "Боромир",
      "born": "2978 Третьей Эпохи",
      "died": "26 февраля 3019 Третьей Эпохи",
      "image": "https://example.com/images/boromir.jpg"
    }
  },
  {
    "id": "8",
    "attributes": {
      "name": "Галадриэль",
      "born": "Неизвестно (одна из первых эльфов Средиземья)",
      "died": "Не применимо (покинула Средиземье в Четвертой Эпохе)",
      "image": "https://example.com/images/galadriel.jpg"
    }
  },
  {
    "id": "9",
    "attributes": {
      "name": "Саурон",
      "born": "Неизвестно (известен как Майар)",
      "died": "Третья Эпоха 3019 (утрата физического тела)",
      "image": "https://example.com/images/sauron.jpg"
    }
  },
  {
    "id": "10",
    "attributes": {
      "name": "Голлум (Смеагол)",
      "born": "около 2430 Третьей Эпохи",
      "died": "25 марта 3019 Третьей Эпохи",
      "image": "https://example.com/images/gollum.jpg"
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
              "next": page
          }
        },
        "data": paginated_data
    }
