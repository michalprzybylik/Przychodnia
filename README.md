# BD2Projekt
BD2Projekt - (RA2) System obsługi rezerwacji wizyt lekarskich
...
Python3, Django 2.2.8

## Bundle
- fontawesome-free ^5.12.0
- bootstrap ^4.4.1
- jquery ^3.4.1
- popper.js ^1.16.0

## Passy
- superużytkownik: admin / admin
- rejestratorka: rejestratorka / 123456789
- lekarz: lekarz / 123456789

## ToDo
[x] usunąć pole Opis z widoku rejestratorki
[ ] wynik w modelu BadLab i BadFiz to bool czy text ?

## Opis

### Definiowanie użytkowników:
- rejestratorka
- lekarz
- laborant
- kierownik laboratorium
- manager

### Operacje:
- towrzenie danych słownikówych (badania fizykalne/laboratoryjne)
- danych pacjenta
- rejestracji wizyty przez rejestratorke
- wykonywania badania laboratoryjnego przez laboranta (i jego weryfikacji przez kierownika laboratorium)
- wykonanie wizyty przez lekarza
- przegląd wyników badań
- obsługa stanów wizyt i stanów badań laboratoryjnych

### Raporty o charakterze:
- medycznym
- zarządczym

### Program administraotra użytkowników i uprawnień.
