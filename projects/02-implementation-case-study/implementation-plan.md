# Plan wdrożenia portalu obsługi odbiorów

## 1. Cel i zakres

**Scenariusz:** fikcyjna spółka komunalna wdraża portal do rejestrowania zleceń odbioru, przekazywania danych do systemu stacji i udostępniania dokumentów klientom.

**Cel demonstracji:** uporządkować zadania klienta, dostawcy i zespołu wdrożeniowego tak, aby zależności techniczne, testy i szkolenie były widoczne przed uruchomieniem.

**W zakresie:** konfiguracja organizacji i użytkowników, test połączenia z systemem stacji, UAT, instruktaż, decyzja go/no-go i przekazanie do wsparcia.

**Poza zakresem:** migracja historycznych danych, zmiany w systemie dostawcy, administracja infrastrukturą klienta i gwarancja wyników biznesowych.

## 2. Plan 30 dni roboczych

| Etap | Termin | Właściciel prowadzący | Rezultat / kryterium przejścia |
|---|---:|---|---|
| Kickoff i potwierdzenie zakresu | D1–D3 | Koordynator wdrożenia | Zakres, kontakty, odpowiedzialności i zależności zatwierdzone |
| Przygotowanie środowiska | D4–D8 | IT klienta + dostawca | Dostępy testowe, adresy, porty i certyfikaty sprawdzone przez właścicieli systemów |
| Konfiguracja i integracja | D9–D15 | Dostawca + koordynator | Konfiguracja gotowa; podstawowa wymiana danych potwierdzona |
| UAT i poprawki | D16–D21 | Użytkownicy kluczowi | Przypadki UAT wykonane, błędy opisane i przypisane, blokery zamknięte |
| Szkolenie i gotowość | D22–D26 | Koordynator + klient | Użytkownicy przeszkoleni, procedury i lista kontaktów dostępne |
| Go/no-go i uruchomienie | D27–D28 | Sponsor klienta | Decyzja zapisana; plan wycofania i kanał zgłoszeń potwierdzone |
| Stabilizacja i przekazanie | D29–D30 | Wsparcie + klient | Otwarte sprawy przekazane, właściciele i następne kroki ustalone |

Terminy są przykładowe. Ograniczenia IT klienta i terminy dostawcy mogą przesunąć etapy zależne; zmiana terminu powinna mieć wskazaną przyczynę, właściciela i wpływ na start.

## 3. Role i odpowiedzialności

| Obszar | Klient | Koordynator wdrożenia | Dostawca systemu stacji | Zespół wsparcia |
|---|---|---|---|---|
| Zakres i osoby kontaktowe | A/R | R | C | I |
| Sieć, certyfikaty i dostępność IT | A/R | C | R za własny system | I |
| Konfiguracja portalu | C | A/R | C | I |
| UAT i akceptacja biznesowa | A/R | R | C | I |
| Poprawki po stronie dostawcy | I | C | A/R | I |
| Szkolenie użytkowników | A/R | R | I | C |
| Go/no-go | A | R | C | C |
| Przekazanie zgłoszeń | C | A/R | C | R |

Legenda: **R** – wykonuje, **A** – odpowiada za decyzję, **C** – konsultowany, **I** – informowany.

## 4. Zależności i ryzyka

| Ryzyko / zależność | Sygnał ostrzegawczy | Działanie | Właściciel |
|---|---|---|---|
| Brak gotowości sieci lub certyfikatów | Brak potwierdzenia przed końcem D8 | Wskazać wymagania i właściciela po stronie klienta; aktualizować wpływ na harmonogram | IT klienta |
| Niedostępność dostawcy | Brak terminu testu integracyjnego | Zarezerwować termin podczas kickoffu; eskalować zależność z datą potrzebną | Koordynator |
| Użytkownicy nie mają czasu na UAT | Nieobsadzone przypadki testowe | Uzgodnić zastępstwa i okna testowe przed D16 | Klient |
| Błąd blokujący test | Brak obejścia lub właściciela poprawki | Zarejestrować kroki, dane, wpływ, dowód i termin następnej aktualizacji | Koordynator + dostawca |
| Niska frekwencja na szkoleniu | Brak listy uczestników przed D22 | Uzgodnić grupy i materiały; zaplanować krótkie uzupełnienie | Klient |

## 5. UAT – przykładowe scenariusze

| ID | Scenariusz | Oczekiwany rezultat | Priorytet |
|---|---|---|---|
| UAT-01 | Zalogowanie użytkownika z aktywnym kontem | Użytkownik widzi funkcje przypisane do roli | Wysoki |
| UAT-02 | Próba wejścia na funkcję bez uprawnienia | Dostęp jest odmówiony; dane nie są ujawnione | Wysoki |
| UAT-03 | Utworzenie poprawnego zlecenia | Zlecenie zapisane z potwierdzeniem i identyfikatorem | Wysoki |
| UAT-04 | Brak wymaganego pola w zleceniu | Formularz wskazuje brakujące pole i nie zapisuje rekordu | Średni |
| UAT-05 | Wysłanie zlecenia do integracji | Status i wynik wymiany danych są widoczne | Wysoki |
| UAT-06 | Niedostępność systemu stacji | Błąd jest czytelny, a sprawa możliwa do ponowienia lub eskalacji | Wysoki |
| UAT-07 | Wyszukanie dokumentu po numerze zlecenia | Zwracany jest właściwy dokument lub jasny brak wyniku | Średni |
| UAT-08 | Ponowne wysłanie tej samej referencji | Użytkownik otrzymuje kontrolowany komunikat o duplikacie | Średni |
| UAT-09 | Dezaktywacja użytkownika | Dezaktywowane konto nie może rozpocząć nowej sesji | Wysoki |

Wynik UAT powinien zawierać: ID przypadku, tester, datę, dane testowe bez danych osobowych, wynik, dowód, opis odchylenia i właściciela poprawki.

## 6. Gotowość do startu

- [ ] Zakres, właściciele i kontakty są aktualne.
- [ ] Zależności IT zostały potwierdzone przez ich właścicieli.
- [ ] Krytyczne scenariusze UAT zakończyły się wynikiem pozytywnym lub mają zaakceptowane obejście.
- [ ] Błędy blokujące mają właściciela i decyzję go/no-go.
- [ ] Użytkownicy znają podstawowe zadania i sposób zgłaszania problemów.
- [ ] Lista ról i dostępów została przejrzana przez klienta.
- [ ] Kanał wsparcia, zakres stabilizacji i sposób eskalacji zostały potwierdzone.
- [ ] Klient zna warunki wycofania lub zatrzymania uruchomienia.

## 7. Szkolenie i przekazanie

Szkolenie obejmuje logowanie, typowy przebieg zlecenia, kontrolę statusu, najczęstsze błędy i sposób zgłoszenia problemu. Przekazanie do wsparcia zawiera zakres wdrożenia, konfigurację, znane ograniczenia, otwarte sprawy, kontakt do dostawcy oraz kroki pierwszej diagnozy.
