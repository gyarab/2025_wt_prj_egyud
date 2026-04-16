# 2025_wt_prj_egyud

## Tema projektu

Tematem projektu je webova databazova aplikace **StatFoot**, ktera se zameri na sledovani statistik profesionalnich fotbalistu z nejlepsich evropskych soutezi. Uzivatel bude moci prochazet databazi hracu, tymu, lig a sezon a jednoduse porovnavat jejich vykony podle vybranych ukazatelu. V aplikaci budou evidovany statistiky jako pocet golu, asistenci, odehranych minut, karet nebo poctu zapasu. Datovy model bude postaven nad vazbami mezi hracem, klubem, ligou a konkretnim rocnikem souteze. Soucasti projektu budou prehledove stranky, filtrovani, zebricky a do budoucna take komentare nebo uzivatelske hodnoceni. Cilem je vytvorit prehlednou databazi sportovnich dat s moznosti dalsiho rozsireni v Django prostredi.

## Zaklad projektu

Repozitar obsahuje zakladni strukturu Django projektu:

- `prj` jako hlavni projekt
- `core` jako uvodni aplikaci
- sablony `base.html`, `home.html` a `about.html`
- Bootstrap layout pro responzivni frontend

## Spusteni

```bash
python manage.py runserver
```
test