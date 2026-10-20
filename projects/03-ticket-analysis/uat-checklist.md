# Checklista UAT — szablon

Publiczne opracowanie na podstawie praktyki testowania zmian. Nie zawiera historycznych przypadków ani danych konkretnej firmy.

## Rejestr testu

| Pole | Do uzupełnienia |
|---|---|
| ID przypadku |  |
| Funkcja lub obszar |  |
| Warunki wstępne |  |
| Dane testowe bez danych osobowych |  |
| Kroki testu |  |
| Oczekiwany rezultat |  |
| Rzeczywisty rezultat |  |
| Status: zaliczony / niezaliczony / zablokowany |  |
| Dowód bez danych wrażliwych |  |
| Właściciel poprawki i termin |  |
| Wynik retestu |  |

## Przegląd pokrycia

- [ ] Ścieżka pozytywna: poprawne dane i typowe użycie.
- [ ] Ścieżka negatywna: brak pola wymaganego lub niepoprawne dane.
- [ ] Przypadek skrajny: granica zakresu, nietypowy format lub powtórzenie działania.
- [ ] Uprawnienia i widoczność danych sprawdzone w zakresie testowanej roli.
- [ ] Błędy opisane wraz z wpływem, krokami odtworzenia i oczekiwanym zachowaniem.
- [ ] Po poprawce wykonano retest oraz sprawdzenie regresji w powiązanym obszarze.

## Zasady zapisu

Używaj syntetycznych danych testowych w samym środowisku UAT, ale nie publikuj ich w tym repozytorium. W opisie problemu podawaj tylko informacje potrzebne do odtworzenia i przekazania poprawki.

