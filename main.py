from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

data = [
  {
    "id": 1,
    "name": "Фродо Бэггинс",
    "born": "22 сентября 2968 Третьей Эпохи",
    "died": "Неизвестно (покинул Средиземье в Четвертой Эпохе)",
    "image": "https://example.com/images/frodo.jpg"
  },
  {
    "id": 2,
    "name": "Гэндальф Серый",
    "born": "До начала времён",
    "died": "Неизвестно (становление Гэндальфом Белым)",
    "image": "https://example.com/images/gandalf.jpg"
  },
  {
    "id": 3,
    "name": "Арагорн",
    "born": "1 марта 2931 Третьей Эпохи",
    "died": "1 марта 120 Четвертой Эпохи",
    "image": "https://example.com/images/aragorn.jpg"
  },
  {
    "id": 4,
    "name": "Леголас",
    "born": "Неизвестно (Третья Эпоха)",
    "died": "Неизвестно (покинул Средиземье после Войны Кольца)",
    "image": "https://example.com/images/legolas.jpg"
  },
  {
    "id": 5,
    "name": "Гимли",
    "born": "2879 Третьей Эпохи",
    "died": "Неизвестно (покинул Средиземье вместе с Леголасом)",
    "image": "https://example.com/images/gimli.jpg"
  },
  {
    "id": 6,
    "name": "Сэмвайз Гэмджи",
    "born": "6 апреля 2980 Третьей Эпохи",
    "died": "Неизвестно (покинул Средиземье в Четвертой Эпохе)",
    "image": "https://example.com/images/samwise.jpg"
  },
  {
    "id": 7,
    "name": "Боромир",
    "born": "2978 Третьей Эпохи",
    "died": "26 февраля 3019 Третьей Эпохи",
    "image": "https://example.com/images/boromir.jpg"
  },
  {
    "id": 8,
    "name": "Голлум (Смеагол)",
    "born": "около 2430 Третьей Эпохи",
    "died": "25 марта 3019 Третьей Эпохи",
    "image": "https://example.com/images/gollum.jpg"
  },
  {
    "id": 9,
    "name": "Элронд",
    "born": "около 532 Первой Эпохи",
    "died": "Неизвестно (покинул Средиземье в Четвертой Эпохе)",
    "image": "https://example.com/images/elrond.jpg"
  },
  {
    "id": 10,
    "name": "Арвен Ундомиэль",
    "born": "241 Третьей Эпохи",
    "died": "121 Четвертой Эпохи",
    "image": "https://example.com/images/arwen.jpg"
  }
]


@app.get("/characters")
async def get_characters(
    name: Optional[str] = Query(None, description="Поиск по имени"),
    page: int = Query(1, ge=1, description="Номер страницы"),
    size: int = Query(10, ge=1, description="Размер страницы")
) -> dict:
    filtered_data = (
        [item for item in data if name.lower() in item["name"].lower()]
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
