# Zestaw testów API i UAT

Demonstracyjny pakiet do sprawdzania przykładowej integracji systemu obsługi zleceń. Lokalny mock API zapisuje rekordy w pamięci procesu, dzięki czemu testy można wykonywać bez konta w zewnętrznej usłudze i bez prawdziwych danych.

## Zakres

- kontrakt API w OpenAPI 3.0.3;
- przypadki pozytywne, negatywne i brzegowe;
- kolekcja Postman z asercjami odpowiedzi;
- prosty serwer demonstracyjny w Pythonie, wyłącznie ze standardowej biblioteki.

## Uruchomienie

1. Wymagany jest Python 3.10 lub nowszy.
2. W terminalu w tym katalogu uruchom `python mock_server.py`.
3. W Postmanie zaimportuj `postman_collection.json`.
4. Utwórz środowisko z `baseUrl` ustawionym na `http://127.0.0.1:4010`.
5. Uruchom żądania w kolejności z kolekcji. Serwer działa lokalnie i przechowuje dane tylko do chwili zamknięcia procesu.

## Przypadki

| ID | Scenariusz | Oczekiwany wynik |
|---|---|---|
| API-01 | Stan usługi | HTTP 200 i `status=ok` |
| API-02 | Utworzenie poprawnego zlecenia | HTTP 201, zwrócony identyfikator |
| API-03 | Brak rejestracji pojazdu | HTTP 400 z kodem `VALIDATION_ERROR` |
| API-04 | Ujemna objętość | HTTP 400 z kodem `VALIDATION_ERROR` |
| API-05 | Pobranie utworzonego zlecenia | HTTP 200 i zgodny identyfikator |
| API-06 | Powtórzony `client_reference` | HTTP 409 z kodem `DUPLICATE_REFERENCE` |
| API-07 | Nieistniejące zlecenie | HTTP 404 z kodem `NOT_FOUND` |

Szczegółowa macierz znajduje się w `test-cases.csv`, a kontrakt w `openapi.yaml`.

## Ograniczenia demonstracji

Mock nie uwierzytelnia użytkowników, nie zapisuje danych po zamknięciu i nie odwzorowuje produkcyjnej integracji z urządzeniem lub dostawcą. Testy mają charakter przykładowy i nie potwierdzają zgodności z konkretnym systemem.
