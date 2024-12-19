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
