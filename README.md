# Beer recommendation system

Реализовать рекомендательную систему по подбору пива на основе предоставленного датасета [«BeerAdvocate»](https://www.kaggle.com/datasets/thedevastator/1-5-million-beer-reviews-from-beer-advocate/data)

> «BeerAdvocate» – набор данных, содержащий информацию о пиве, его оценках и отзывах, собранных с веб-сайта BeerAdvocate 
(онлайн-сообщество, посвященное пиву, где пользователи могут делиться своими впечатлениями о различных сортах пива, 
публиковать отзывы и оценивать напитки). Скачать датасет и ознакомиться с его описанием можно здесь.

Для достижения поставленной цели необходимо выполнить следующие задачи:
1. Провести предварительный анализ данных
2. Выбрать 3-4 модели рекомендательных систем и обучить их
3. На основе выбранных вами метрик качества моделей (требуется аргументировать свой выбор) выберите наиболее оптимальную модель. Для выбранной модели реализуйте приложение API, которое обрабатывает входящие пользовательские списки предпочтений пива (пример: [«Budweiser», «Amstel Light», «Bud Light»]) и возвращает топ-7 рекомендованных марок пива (можно в формате json)
4. Обернуть свое решение в Docker
5. Результат проделанной работы представите в структурированном виде в GitHub.


## Program Launch


Before running the program, ensure that the following components are installed:

- Python (version 3.x)
- Docker (if necessary)

### Installing Dependencies

1. Open a terminal.
2. Navigate to the directory containing the program.
3. Install dependencies by executing the following command:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Program in a Local Environment

1. Navigate to the directory containing the program.
2. Launch the API server by executing the command:

    ```bash
    uvicorn app:app --host 0.0.0.0 --port 8000
    ```

3. Open a new terminal.
4. Navigate to the directory containing the program.
5. Run the script to send requests by executing the command:

    ```bash
    python send_requests.py
    ```

## Running the Program Using Docker

1. Navigate to the directory containing the program.
2. Build the Docker image by executing the command:

    ```bash
    docker build -t your_image_name .
    ```

3. Run a container using the built image by executing the command:

    ```bash
    docker run -d -p 8000:8000 your_image_name
    ```

4. Run the script to send requests by executing the command:

    ```bash
    python send_requests.py
    ```

## Testing Functionality

After running the request-sending script, you should have access to the results of the API server interaction. Verify that the results match the expected outcomes.

