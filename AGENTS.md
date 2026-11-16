# Schrijftafel aanpassen: instructies voor de AI

Je helpt iemand die deze schrijftafel naar eigen smaak wil maken. Ga ervan uit dat die persoon geen programmeur is. Dit bestand vertelt wat je vrij mag veranderen en wat heel moet blijven.

## Hoe je werkt

- Werk in een kopie van de map. Het origineel blijft onaangeroerd.
- Maak één wijziging per keer, zo klein als kan.
- Leg in gewone taal uit wat je hebt veranderd en hoe de gebruiker dat zelf controleert.
- Zeg eerlijk wat je werkelijk hebt getest en wat niet.
- Publiceer, verstuur of upload niets. Test met de meegeleverde demomap `Schrijftafel`, niet met de eigen documenten van de gebruiker.
- Er is geen bouwstap. Een opgeslagen wijziging werkt na herladen van de pagina.

## Waar alles staat

| Wat | Waar |
|---|---|
| De pagina zelf: kop, zijbalk, knoppen, vensters | `▶ Begin hier.html` |
| Kleuren van de donkere en lichte weergave | de eerste twee blokken van `Onderdelen/style.css` |
| Overige vormgeving | `Onderdelen/style.css` en de stijl in `▶ Begin hier.html` |
| Lezen, bewerken, opslaan, zoeken, opmaakbalk | `Onderdelen/app.js` |
| Mappen koppelen en bestanden beheren | `Onderdelen/workspace.js` |
| Projectkeuze | `Onderdelen/projects.js` |
| Vorige versie herstellen | `Onderdelen/recovery.js` |
| Afbeeldingen en video | `Onderdelen/media.js` |
| Links tussen documenten | `Onderdelen/internal-links.js` |
| Wat bij het doorzoeken wordt overgeslagen | `Onderdelen/ignore-rules.js` |
| De demo-inhoud | de map `Schrijftafel` |
| Bibliotheken van anderen | `Onderdelen/vendor` (niet aanpassen) |

Verander je de meegeleverde uitleg `00 - Begin hier.md`, draai dan `node Onderdelen/scripts/embed-introduction.cjs` om de ingebouwde versie bij te werken.

## Vrij te veranderen

Kleuren, letters, indeling, naam, alle teksten, de taal, knoppen in de opmaakbalk, sjablonen, exportmogelijkheden en nieuwe functies. Dit is een vertrekpunt: de vormgeving van de maker is geen voorschrift.

## Wat heel moet blijven

Deze app schrijft in de echte bestanden van de gebruiker. Wees daar zuinig op.

1. **Opslaan overschrijft niet blind.** Is het bestand elders veranderd, dan blijft de bewerking in de editor staan en wordt er niet opgeslagen.
2. **De herstelkopie.** Bij opslaan gaat de vorige tekst eerst naar `.werkbank-herstel`. Lukt die kopie niet, dan wordt het origineel niet overschreven.
3. **Hernoemen en verplaatsen kopiëren eerst**, controleren de inhoud en verwijderen pas daarna de bron.
4. **Verwijderen vraagt altijd bevestiging.**
5. **Extra documentgegevens bovenaan een bestand blijven behouden** bij opslaan.
6. **Alles blijft lokaal.** Geen analytics, geen automatische verbinding met een AI of andere dienst. Video maakt pas verbinding na een klik.
7. **Credits en licenties.** De basis is de Markdown Browser van Joost Plattel. Laat `LICENSE`, `HERKOMST.md`, `THIRD_PARTY_NOTICES.md` en de naamsvermelding van Joost Plattel staan.

## Controleren na elke wijziging

Laat de gebruiker dit zelf doen in Chrome of Edge, met de demomap:

1. Open `▶ Begin hier.html`, kies **+ Project toevoegen** en selecteer de map `Schrijftafel`.
2. Open een document, kies **Bewerken**, verander een zin en klik **Opslaan**.
3. Herlaad de pagina. Staat de wijziging er nog?
4. Kies **Meer → Vorige versie herstellen** en bekijk de kopie.
5. Zoek op een woord uit het document.

Wie Node.js, Playwright en Chrome heeft, kan de proeven in `Onderdelen/tests/` draaien, te beginnen met `node Onderdelen/tests/smoke.cjs`.

## Een eigen versie delen

De code valt onder MIT, met naamsvermelding van Joost Plattel en Erwin Blom. Geef een versie die je verspreidt een eigen naam, zodat duidelijk is dat het niet de officiële Schrijftafel is. "Gebaseerd op Schrijftafel" vermelden mag.
