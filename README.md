# StatFoot

StatFoot je semestrální databázová webová aplikace vytvořená v Django. Projekt se zaměřuje na evidenci a porovnávání statistik profesionálních fotbalistů, týmů, soutěží a sezon. Cílem je navrhnout přehledný informační systém nad sportovními daty, který bude možné v dalších etapách rozšířit o filtrování, detailní přehledy, komentáře, hodnocení i pokročilejší analytické výstupy.

## Téma projektu

Název projektu: **StatFoot**

StatFoot je návrh databázové aplikace pro správu a analýzu fotbalových statistik. Aplikace bude evidovat ligy, sezony, kluby, hráče a jejich výkonnostní ukazatele. Uživatel bude moci vyhledávat hráče podle jména, pozice, národnosti nebo příslušnosti k týmu a zároveň porovnávat jejich statistiky napříč sezonami. Součástí systému budou i uživatelské komentáře a hodnocení, takže aplikace nebude sloužit jen jako pasivní katalog, ale i jako prostor pro práci s obsahem a sdílení názorů. Téma vychází z oblasti sportovních statistik, která nabízí přirozeně bohatou a dobře strukturovatelnou databázi.

## Odborný článek

Projekt StatFoot představuje webovou databázovou aplikaci z oblasti fotbalové analytiky. Jejím cílem je přehledně evidovat a zobrazovat informace o _ligách_, _sezonách_, _týmech_, _hráčích_, _statistikách_, _komentářích_ a _hodnoceních_. V praxi půjde o systém, ve kterém bude možné sledovat výkonnost profesionálních fotbalistů v kontextu konkrétní soutěže i konkrétního ročníku. Klíčovou rolí datového modelu je vazba mezi _hráčem_ a _týmem_, mezi _týmem_ a _ligou_ a následně mezi _hráčem_ a jeho sezonními _statistikami_.

Anonymní návštěvník bude moci procházet veřejnou část aplikace, zobrazovat přehledy a číst základní informace o hráčích a soutěžích. Registrovaný uživatel získá možnost vytvářet _komentáře_ a přidávat _hodnocení_, čímž se z aplikace stane interaktivní databáze s komunitní vrstvou. Administrátor bude spravovat obsah přes administrační rozhraní Django, tedy zakládat nové _ligy_, _týmy_, _hráče_ a upravovat jejich vazby i jednotlivé statistické záznamy.

Z pohledu problémové domény je důležité, že jeden _tým_ patří do jedné _ligy_, jeden _hráč_ náleží k jednomu _týmu_ a pro každou _sezonu_ může mít vytvořenou samostatnou sadu _statistik_. Ty budou zahrnovat například počet gólů, asistencí, odehraných minut, žlutých a červených karet nebo počet startů. Takto navržený systém umožní budoucí rozšíření o žebříčky, filtrování, porovnávání výkonu i detailní analytické pohledy nad sportovními daty.

## Uživatelské role

- Anonymní návštěvník: prohlíží obsah webu a základní statistické přehledy.
- Registrovaný uživatel: přidává komentáře a hodnotí hráče.
- Administrátor: spravuje databázové záznamy a obsah přes Django admin.

## Přiložené návrhy

Do adresáře `imgs/` lze průběžně ukládat podklady k analýze a návrhu:

- `imgs/user-flow.jpg` nebo `imgs/user-flow.png`
- `imgs/wireframes.jpg` nebo `imgs/wireframes.png`
- `imgs/er-diagram.jpg` nebo `imgs/er-diagram.png`

Po doplnění obrázků je možné do README vložit například:

```md
![User Flow](imgs/user-flow.png)
![Wireframes](imgs/wireframes.png)
![E-R diagram](imgs/er-diagram.png)
```

## Struktura repozitáře

```text
.
|-- fixtures/
|   |-- comments.yaml
|   |-- leagues.yaml
|   |-- players.yaml
|   |-- ratings.yaml
|   |-- seasons.yaml
|   |-- statistics.yaml
|   |-- teams.yaml
|   `-- users.yaml
|-- imgs/
|-- prj/
|   |-- app/
|   |   `-- templates/
|   |-- prj/
|   `-- manage.py
|-- .gitignore
|-- README.md
`-- requirements.txt
```

## Spuštění projektu

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python prj/manage.py migrate
python prj/manage.py loaddata users leagues seasons teams players statistics comments ratings
python prj/manage.py createsuperuser
python prj/manage.py runserver
```

## Poznámky k odevzdání

- V repozitáři není verzováno `venv`, `db.sqlite3` ani `*.pyc`.
- Adresář `fixtures/` obsahuje ukázková testovací data rozdělená do samostatných YAML souborů podle modelů.
- Adresář `imgs/` je připravený pro vložení user flow, wireframů a E-R diagramu.
