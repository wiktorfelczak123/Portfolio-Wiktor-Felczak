# Integracje API i diagnostyka problemu aplikacji

Zanonimizowany opis dwóch sytuacji z pracy przy wdrożeniach systemu B2B. Materiał przedstawia zakres koordynacji integracji oraz sposób przygotowania informacji dla dostawcy podczas problemu z aplikacją.

## Przypadek: problem z aplikacją mobilną

Po aktualizacji po stronie dostawcy pojawił się problem z działaniem aplikacji mobilnej. W ramach diagnozy sprawdziłem dostępne logi aplikacji w panelu Plesk, opisałem obserwacje i przekazałem raport właściwemu dostawcy. Następnie monitorowałem poprawkę.

## Koordynacja integracji

W projektach uzgadniałem z klientem i dostawcą wymagania połączenia systemów, w tym kwestie sieci, portów, certyfikatów i protokołów. Dopilnowywałem właścicieli zależności i przekazywałem dostawcy informacje potrzebne do diagnozy.

W jednym z projektów zdalne uporządkowanie konfiguracji pozwoliło wznowić pracę wstrzymaną przez prawie dwa lata.

## Karta przekazania problemu

W repozytorium znajduje się [zanonimizowany szablon raportu dla dostawcy](incident-handoff-template.md). To opracowanie do portfolio, a nie kopia raportu z firmy. Nie publikuje identyfikatorów klientów, adresów, logów ani danych dostępowych.

## Zakres pracy

- zebranie objawów, zakresu wpływu i czasu wystąpienia;
- sprawdzenie dostępnych logów aplikacji w panelu Plesk;
- przygotowanie czytelnego raportu i przekazanie go dostawcy;
- śledzenie poprawki oraz ustalenie dalszego właściciela działania.

Dawne pliki ćwiczeniowe Mock API, OpenAPI i Postman są oznaczone jako archiwalne. Opis powyżej dotyczy zakresu pracy przy rzeczywistych wdrożeniach.
