# Analiza zgłoszeń wsparcia L1/L2

Mały projekt analityczny na syntetycznym zbiorze zgłoszeń. Łączy proste zapytania SQLite z arkuszem Excel, który pokazuje wolumen, eskalacje, powtarzalność i czas rozwiązania.

## Pliki

- `data/tickets.csv` – 120 fikcyjnych rekordów, bez danych osobowych i rzeczywistych informacji o klientach.
- `ticket-analysis.xlsx` – arkusz `Summary` z formułami i wykresami oraz arkusz `Tickets` z danymi.
- `sql/analysis.sql` – zapytania SQLite do analizy kategorii, eskalacji, trendu miesięcznego i długich spraw.
- `data-dictionary.md` – definicje pól i ograniczenia interpretacji.

## Najważniejsze miary

Podsumowanie oblicza liczbę zgłoszeń, liczbę i udział eskalacji, medianę godzin rozwiązania dla rekordów z uzupełnionym czasem oraz rozbicie według kategorii i miesiąca. Formuły są widoczne w arkuszu, a pełne dane pozostają na osobnej karcie.

## Uruchomienie zapytań

1. Utwórz lokalną bazę SQLite.
2. Zaimportuj `data/tickets.csv` do tabeli `tickets`, zachowując nagłówki jako nazwy kolumn.
3. Wykonaj zapytania z `sql/analysis.sql`.

Wartości służą wyłącznie do demonstracji. Nie należy opisywać ich jako rzeczywistych wyników pracy ani przenosić do CV jako osiągnięć.
