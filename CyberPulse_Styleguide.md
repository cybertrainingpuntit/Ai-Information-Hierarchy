# CyberPulse Huisstijlboek

**Laatste update:** 13 juni 2026

**Bronnen:** visuele inspectie van http://localhost:5173/, `client/src/index.css`, publieke pagina's, login‑flow en gedeelde UI‑componenten.

---

## 1. Merkessentie

**CyberPulse** is een cybersecurity‑awareness platform waarin medewerkers elke week leren denken als verdediger, met **Cipher** als terugkerende tegenkracht. De stijl moet voelen als: professioneel, dreigend genoeg om urgentie te geven, maar helder genoeg voor gewone medewerkers en management.

**Kernzin:**
> CyberPulse maakt cyberrisico concreet met een doorlopend weekprogramma waarin medewerkers aanvallen leren herkennen, verdediging oefenen en voortgang aantoonbaar maken.

**Belofte:**
- **Voor medewerkers:** korte, herkenbare training zonder schoolse toon.
- **Voor admins:** meetbare voortgang, risico‑inzicht en bewijs richting audits.
- **Voor resellers:** white‑label inzetbaar zonder het onderliggende CyberPulse‑kwaliteitsgevoel te verliezen.

**Merkpersoonlijkheid:**
- Scherp, maar niet schreeuwerig.
- Technisch geloofwaardig, maar niet elitair.
- Verhalend, maar functioneel.
- Donker en cinematografisch op publieke/security‑schermen; rustiger en taakgericht in dashboards.

---

## 2. Logo en beeldmerk

**Primaire logo‑assets in de app:**
- Donker thema: `/cyberpulsewit.webp` en `/cyberpulsewit.svg`
- PWA/icons: `/icons/icon-192.png`, `/icons/icon-512.png`

**Gebruik:**
- Gebruik het **witte** CyberPulse‑logo op donkere achtergronden.
- Houd rondom het logo minimaal de hoogte van de letters als vrije ruimte.
- Plaats het logo in publieke headers linksboven, zonder extra kader.
- In login‑ en intro‑schermen mag het logo compact en functioneel zijn, niet dominant boven de inhoud.

**Niet doen:**
- Geen glow, bevel, drop‑shadow of extra outline op het logo.
- Geen logo op drukke delen van Cipher‑afbeeldingen zonder donkere overlay.
- Geen willekeurige kleurvarianten buiten platform‑branding of reseller‑branding.

---

## 3. Kleurensysteem

De standaardidentiteit is donker. Light‑mode bestaat voor toegankelijkheid en beheercontext, maar de publieke CyberPulse‑signatuur is donker.

### Primaire tokens
| Rol | Token | HSL | Hex | Gebruik |
|-----|-------|-----|-----|--------|
| Cipher void | `--cipher-void` | 222 40% 2% | `#030407` | Intro, login, hero‑achtergronden |
| Achtergrond | `--background` | 222 25% 6% | `#0b0e13` | App‑achtergrond |
| Kaart | `--card` | 222 22% 10% | `#14171f` | Panels, cards, dialogs |
| Border | `--border` | 222 20% 16% | `#212631` | Subtiele scheiding |
| Tekst | `--foreground` | 210 18% 92% | `#e7ebee` | Hoofdtekst op donker |
| Gedempte tekst | `--muted-foreground` | 210 12% 58% | `#8794a1` | Uitleg, metadata, secondary copy |
| Primair rood | `--primary` | 357 100% 45% | `#e6000b` | CTA, focus, alarm, merkaccent |
| Rood oppervlak | `--primary‑surface` | 357 72% 12% | `#35090b` | Subtiele rode panels/badges |
| Cyaan accent | `--accent` | 190 70% 46% | `#23acc7` | Blue‑team, signalen, ondersteunende highlights |

### Statuskleuren
| Status | Token | Hex | Gebruik |
|--------|-------|-----|---------|
| Succes | `--success` | `#21c45d` | Voltooid, veilig, geslaagd |
| Waarschuwing | `--warning` | `#f59f0a` | Aandacht nodig, bijna verlopen |
| Info | `--info` | `#3c83f6` | Neutrale uitleg, systeemstatus |
| Destructief | `--destructive` | *roodfamilie* | Fouten, risico, blokkades |

### Kleurregels
- **Rood** is het primaire actie‑ en dreigingssignaal. Gebruik het spaarzaam, zodat CTA’s en risico’s gewicht houden.
- **Cyaan** is secundair: blue‑team, bescherming, analyse, systeeminzicht.
- **Oranje/amber** is voor beloning, aandacht of certificering.
- Wit op donker mag veel voorkomen, maar bodytekst hoort meestal op 50‑70 % opacity.
- Borders zijn dun en subtiel: meestal `white/8`, `white/10`, `border`, of `border‑primary/20`.
- Vermijd grote rode vlakken buiten primaire CTA’s; rood moet urgent blijven.

---

## 4. Typografie

**Tokens:**
- **Sans/heading:** `Inter`, fallback `DM Sans`, `sans‑serif`
- **Mono:** `JetBrains Mono`, fallback `Fira Code`, `monospace`
- **Dyslexic/accessibility fallback:** `Arial`, `Verdana`, `Consolas`

**Gebruik:**
- Grote publieke **H1’s** gebruiken `Inter`, licht gewicht (`font‑light / 300`), strak en ruim.
- Dashboard‑titels gebruiken `Inter`, `font‑bold`, meestal 24‑30 px.
- Navigatie, labels, technische metadata, inputs en bodycopy in de publieke experience gebruiken vaak `JetBrains Mono`.
- Uppercase microcopy gebruikt ruime tracking, bv. `tracking-[0.18em]` tot `tracking-[0.2em]`.

**Richtmaten:**
- **Hero H1 desktop:** 64‑72 px, licht gewicht, line‑height rond 1.02.
- **Sectietitel:** 36‑48 px, licht gewicht.
- **Dashboard H1:** 24‑30 px, bold.
- **Body publiek:** 14‑18 px, mono, line‑height ruim.
- **Labels:** 10‑12 px, uppercase, mono.

**Niet doen:**
- Geen speelse of ronde display‑fonts.
- Geen zware all‑caps headlines voor lange zinnen.
- Geen negatieve letterspacing.
- Geen bodycopy in fel wit; dat wordt te hard op het donkere thema.

---

## 5. Layout en compositie

### Publieke pagina’s
- Full‑bleed donkere achtergrond met Cipher‑beeld, matrix/kana‑signalering of subtiele overlays.
- Header zweeft boven de pagina met transparante, afgeronde navigatie.
- Hero is links sterk typografisch, rechts een functioneel panel of beeldlaag.
- Sections gebruiken ruime verticale ademruimte en donkere cards met zachte transparantie.

### App / dashboard
- Sidebar‑gebaseerde structuur met rolgerichte menu‑clusters.
- Page headers combineren een Lucide‑icoon in een rood getint vlak met titel en subtitel.
- Cards zijn functioneel: status, voortgang, rapportage, modules, gebruikers.
- In beheerinterfaces: minder cinematografisch, meer scanbaar.

**Radii:**
- Basisradius: `--radius: .5rem` (8 px).
- Inputs/buttons in app: meestal 8‑9 px.
- Publieke pills en nav‑items: full rounded.
- Grote marketingcards mogen 16 px gebruiken als ze op transparante donkere achtergronden liggen.

**Schaduw en diepte:**
- Gebruik vooral borders, transparantie en blur.
- Zware shadows alleen voor overlays, modals en floating widgets.
- Geen decoratieve gradient‑orbs of losse bokeh‑elementen.

---

## 6. Componentrichtlijnen

### Buttons
- **Primaire CTA:**
  - Achtergrond: rood `#e6000b` (`bg‑red‑600`).
  - Hover: iets lichter (`bg‑red‑500`).
  - Tekst: wit, medium/semibold.
  - Radius: 8‑9 px in formulieren, full rounded in publieke hero.
- **Secundaire CTA:**
  - Transparant of `white/5`.
  - Border `white/15` tot `white/20`.
  - Tekst `white/58` tot `white/85`.
  - Hover naar meer contrast, niet naar felle kleur.
- **Iconen:** gebruik Lucide‑icons voor acties en navigatie. Pijlen versterken flow (start trial, doorgaan, openen). Security‑iconen moeten inhoudelijk kloppen: `Shield`, `Eye`, `Lock`, `KeyRound`, `Swords`, `MailWarning`, `FileCheck`.

### Inputs
- Donkere achtergrond: `black/40` of `white/5`.
- Border: `white/15`; focus naar rood of witte ring afhankelijk van context.
- Placeholder: `white/30`.
- Radius: 8‑9 px.
- Labels: uppercase, mono, klein, gedempt.

### Cards en panels
- Basis: donkere kaart `#060a11` / `#14171f`, border `white/8` of `white/10`.
- Transparantie en backdrop‑blur zijn toegestaan op publieke pagina’s.
- Vermijd cards in cards.
- Gebruik cards voor herhaalde items, pricing, moduleblokken, rapportageblokken en modals.

### Navigatie
- Publieke nav: rounded pill, mono, kleine tekst, gedempt wit.
- Actieve taal/button: `white/10`, border `white/30`.
- App‑sidebar: rolgebaseerde groepen met duidelijke iconen en labels.
- Groepen horen inhoudelijk te zijn: overzicht, medewerkers, training, integraties, klanten, platform, account.

---

## 7. Beeldtaal

**Primaire beeldlaag:** Cipher is de herkenbare tegenkracht. Gebruik bestaande assets uit `client/public`: `cipher‑hero.webp`, `cipher‑met‑laptop.webp`, `cipher‑intro.webp`, `cipher‑wijst.webp`, `cipher‑glazebol.webp` enzovoort.
- Beelden moeten donker, scherp en contextueel zijn: hacker/analist, laptop, briefing, dossier, observatie.

**Overlays:**
- Altijd voldoende contrast met zwarte/donkere gradient overlays.
- Hero‑overlays mogen lopen van `#030508` naar transparant.
- Tekst nooit direct op druk beeld zonder overlay.

**Niet doen:**
- Geen generieke stockfoto’s van hangsloten, datacenters of handen op toetsenbord zonder CyberPulse‑context.
- Geen cartoonachtige hackerstijl.
- Geen overmatig blauwe corporate SaaS‑look; CyberPulse moet eigen en dreigend blijven.

---

## 8. Motion en interactie

**Signatuur:** Glitch, kana/matrix‑achtige laadervaring en subtiele scan‑effecten horen bij Cipher. Motion moet spanning geven, niet de taak vertragen.

**Regels:**
- Gebruik animatie vooral in publieke intro, hero, ceremony en module‑start.
- Dashboards moeten rustig blijven.
- Respecteer `cp‑reduced‑motion` en `cp‑no‑animations`.
- Laadervaringen mogen merkend zijn, maar moeten kort blijven.

---

## 9. Tone of voice

**Stem:** Direct, concreet, volwassen. Geen bangmakerij zonder handelingsperspectief.
- Security‑termen zijn toegestaan, maar altijd gekoppeld aan herkenbare werkdagen.
- Cipher mag dreiging concreet maken, maar CyberPulse blijft de gids.

**Veelgebruikte woorden en frames:**
- Cipher, rode draad, weekprogramma, aanvallers‑perspectief, verdediging, voortgang, aantoonbaar, phishing‑simulaties, datalek‑monitoring, privacy‑by‑design, auditbare voortgang.

**Schrijfstijl:**
- Korte zinnen voor UI.
- Actieve werkwoorden.
- Geen jargonstapels in medewerkerflows.
- Voor management: nadruk op bewijs, ritme, risico en compliance.
- Voor resellers: nadruk op white‑label, klantbeheer, bundelbaarheid en eigen propositie.

**Voorbeelden:**
- Goed: "Start gratis met je team"
- Goed: "Vraag Cipher"
- Goed: "Maak awareness aantoonbaar voor management en audits."
- Minder goed: "Optimaliseer uw cyberweerbaarheidsparadigma via modulaire awareness‑interventies."

---

## 10. Doelgroepen

| Doelgroep | Toon | Belofte | UI‑focus |
|----------|------|----------|----------|
| Medewerkers | herkenbaar, praktisch, kort | je leert signalen zien voordat ze schade veroorzaken | voortgang, badges, missie, korte modules |
| Admins | beheersbaar, meetbaar, rustig | inzicht in voortgang, risico en bewijs | dashboards, rapportages, gebruikersbeheer, SSO, modules |
| Superadmins | operationeel en precies | platform‑controle, contentbeheer, support, billing | compact, datarijk, weinig theatrale effecten |
| Resellers | professioneel, commercieel toepasbaar | CyberPulse onder eigen propositie beheren | klantorganisaties, branding, modules, facturatie, SSO |

---

## 11. White‑label en reseller‑branding

CyberPulse ondersteunt reseller‑ en organisatiebranding. Houd daarbij deze grenzen aan:
- Primaire kleur mag veranderen via branding token, maar contrastregels blijven gelden.
- Login kan reseller‑branding tonen zonder Cipher‑beeld; gebruik dan een subtiele glow in de primaire kleur.
- Logo’s van resellers gebruiken dezelfde max‑height en spacing als CyberPulse‑logo’s.
- Verberg CyberPulse‑attributie alleen als `hidePlatformBranding` dat expliciet aangeeft.
- Laat white‑label niet leiden tot inconsistente componenten; buttons, inputs, spacing en typografie blijven CyberPulse‑systematiek.

---

## 12. Toegankelijkheid

**Aanwezige instellingen:**
- Font size classes: `cp‑font‑small`, `cp‑font‑normal`, `cp‑font‑large`, `cp‑font‑xlarge`
- Density classes: `cp‑density‑compact`, `cp‑density‑normal`, `cp‑density‑comfortable`
- High contrast: `cp‑high‑contrast`
- Dyslexic font: `cp‑dyslexic‑font`
- Motion controls: `cp‑reduced‑motion`, `cp‑no‑animations`

**Richtlijnen:**
- Focus states moeten zichtbaar zijn, bij voorkeur ring in rood of high‑contrast amber.
- Bodytekst op donker minimaal rond `white/50`; belangrijke tekst `white/80+`.
- Kleine uppercase labels nooit als enige informatiebron gebruiken.
- Iconen altijd ondersteunen met tekst of duidelijke context, behalve in compacte herhaalde navigatie met tooltip/aria‑label.

---

## 13. Praktische UI‑recepten

**Hero:**
```tsx
<section className="relative min-h-screen bg-[#030508] text-white">
  <CipherBackground intensity="quiet" imageSrc="/cipher-met-laptop.webp" />
  <h1 className="text-5xl font-light leading-[1.02] tracking-tight md:text-7xl">
    Train medewerkers met Cipher als rode draad.
  </h1>
</section>
```

**Panel:**
```tsx
<div className="rounded-2xl border border-white/10 bg-[#060a11]/72 p-6 backdrop-blur">
  <p className="text-xs uppercase tracking-[0.18em] text-red-200/60">Maak kennis met Cipher</p>
  <h2 className="text-2xl font-semibold text-white">Wat weet Cipher over jou?</h2>
  <p className="font-mono text-sm leading-relaxed text-white/50">Controleer zakelijke signalen.</p>
</div>
```

**Dashboard page header:**
```tsx
<PageHeader
  icon={Shield}
  title="Risicoregister"
  subtitle="Bekijk signalen, voortgang en opvolging per team."
/>
```

---

## 14. Do's en don'ts

**Do:**
- Gebruik donkerte, rood en Cipher om urgentie te maken.
- Houd dashboards functioneel en rustig.
- Schrijf vanuit concrete situaties: phishing, haast, vertrouwen, gelekte data.
- Gebruik bestaande tokens en componenten.
- Gebruik Lucide‑icons consequent.
- Laat witruimte en borders het werk doen.

**Don't:**
- Geen generieke SaaS‑gradient of blauwe corporate landingpage.
- Geen speelse gamificationstijl die de security‑serieusheid ondermijnt.
- Geen lange technische claims zonder bewijs of context.
- Geen willekeurige neonkleuren naast rood/cyaan/amber.
- Geen overvolle cards met meerdere visuele stijlen tegelijk.
- Geen extra decoratie als de informatie zelf al spanning heeft.

---

## 15. Implementatiebronnen

**Belangrijkste bestanden:**
- `client/src/index.css` – design tokens, thema’s, toegankelijkheidsklassen.
- `client/src/pages/public/HomePage.tsx` – publieke merkervaring.
- `client/src/components/public/CipherPublicShell.tsx` – publieke shell, achtergrond en buttons.
- `client/src/App.tsx` – login‑flow en algemene app‑shell.
- `client/src/components/AppSidebar.tsx` – rolgebaseerde navigatie.
- `client/src/components/PageHeader.tsx` – standaard page‑header patroon.
- `client/public/` – logo‑, Cipher‑ en badge‑assets.

---

*Dit huisstijlboek dient als leidraad voor alle UI‑ontwerp, component‑ontwikkeling en content‑creatie binnen CyberPulse.*
