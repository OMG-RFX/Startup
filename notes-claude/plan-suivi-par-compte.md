# Suivi des clics par compte promo (prêt à intégrer)

## 1. Nouveaux liens courts (à AJOUTER en haut du `_redirects`, les 6 liens actuels restent)

reps-coach-app (RepFix) :
```
/ig-c2s   /?utm_source=instagram&utm_medium=organique&utm_campaign=test_coach&utm_content=conseil2sportif   302
/tt-s2f   /?utm_source=tiktok&utm_medium=organique&utm_campaign=test_coach&utm_content=sport2fou45          302
```

ohmyglow (Oh My Glow) :
```
/ig-c2g   /?utm_source=instagram&utm_medium=organique&utm_campaign=test_glowup&utm_content=conseil2glowup   302
/tt-g70   /?utm_source=tiktok&utm_medium=organique&utm_campaign=test_glowup&utm_content=girl70463           302
```

## 2. Compteur abacus : nouvelle clé par compte

Dans le script de suivi de chaque page, en plus des clés actuelles :
```js
// Ne compte pas les robots ni nous-mêmes
var ua = navigator.userAgent || "";
var estRobot = navigator.webdriver || /bot|crawl|spider|facebookexternalhit|meta-externalagent|facebookcatalog|preview|curl|wget|headless/i.test(ua);
var params = new URLSearchParams(location.search);
if (params.get("moi") === "1") { try { localStorage.setItem("moi", "1"); } catch (e) {} }
var estMoi = false; try { estMoi = localStorage.getItem("moi") === "1"; } catch (e) {}

if (!estRobot && !estMoi) {
  var compte = (params.get("utm_content") || "").replace(/[^a-z0-9_]/gi, "").toLowerCase();
  if (compte) {
    // ex : coach.visite.compte-conseil2sportif / coach.inscription.compte-conseil2sportif
    fetch("https://abacus.jasoncameron.dev/hit/ohmyglow-x7k2q9/" + PAGE + ".visite.compte-" + compte);
    try { sessionStorage.setItem("compte", compte); } catch (e) {}
  }
  // ... compteurs existants inchangés
}
```
Les événements suivants (scroll-50, clic-formulaire, inscription) ajoutent aussi `.compte-<compte>` si `sessionStorage.compte` existe.

## 3. Tableau de bord : bloc « Par compte »

Lit `{page}.{visite|clic-formulaire|inscription}.compte-{compte}` pour :
- coach : conseil2sportif, sport2fou45
- glowup : conseil2glowup, girl70463

## 4. Messages privés à utiliser ensuite

- @conseil2sportif : reps-coach-app.netlify.app/ig-c2s
- @sport2fou45 : reps-coach-app.netlify.app/tt-s2f
- @conseil2glowup : ohmyglow.netlify.app/ig-c2g
- @girl70463 : ohmyglow.netlify.app/tt-g70

Pour ne pas te compter toi-même : ouvre une fois chaque site avec `?moi=1` à la fin, sur chaque téléphone.
