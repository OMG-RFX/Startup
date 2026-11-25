# Banque de formats viraux (RepFix + Oh My Glow)

Créée le 25/11/2026 (Cloud), à partir du TikTok envoyé par pm + veille des formats qui marchent en ce moment.
À enrichir : chaque nouveau format trouvé = une nouvelle fiche en bas (avec la date et le lien d'origine).

Rappels : Oh My Glow, on ne crée rien → les idées OMG sont des **suggestions pour Jean** (et pour ses carrousels). RepFix : on fabrique (moteur v3 cloud ou Swift Mac). On ne fait jamais d'US.

---

## Règle de rotation (pm, 25/11)

1. **Jamais 2 fois le même format d'affilée** sur un même compte TikTok dans la journée. Sur les 5 TikTok du jour : au moins **3 formats différents**.
2. Chaque nouveau lot RepFix de 5 vidéos = **au moins 3 formats** de cette banque (pas 5 fois « erreur / solution »).
3. **Veille chaque semaine** : trouver au moins 1 nouveau format viral (liens de pm, Process `list_tiktok_formats`, comptes fitness / self-care qui explosent) et l'ajouter ici.
4. Noter le format de chaque vidéo dans `ETAT.md` (colonne ou mention « format : … ») pour savoir lequel marche le mieux.
5. Toujours garder : accroche sur **l'habitude du spectateur** (6x plus de vues), CTA « écris REP / GLOW ».

## Pourquoi la rétention est faible (5,8 s en moyenne sur TikTok RepFix) et ce qu'on change

- La 1re image doit déjà montrer le **conflit visuel** (deux options, une erreur visible), pas un titre.
- Vidéos plus **courtes** : 12-20 s. Une vidéo de 20 s regardée 2 fois vaut mieux qu'une vidéo de 45 s lâchée à 6 s.
- Une **question** posée tout de suite (« lequel gagne ? ») : on reste pour la réponse.
- La fin doit **reboucler** sur le début (boucle) : TikTok compte les revisionnages.
- Chiffres et barres qui bougent à l'écran : l'œil suit le mouvement.

---

## 1. Simulation « A vs B » animée (le TikTok envoyé par pm)

**Source** : @visionownitknow, « Slow vs fast reps: which wins? » (8/11/2026). 20 s, ~98 K j'aime, **18 K enregistrements, 7,9 K partages** (énorme ratio : les gens le gardent et l'envoient).

**Comment c'est fait**
- Fond noir, titre en 2 couleurs : « **Slow** vs **fast**. » (bleu vs orange) + sous-titre « On the bicep curl, which wins? ».
- Deux bonshommes bâtons blancs, chacun sous un projecteur (cône de lumière), qui font le mouvement en même temps à 2 vitesses (« 4 s up · 4 s down » vs « 1 s up · 1 s down »). Le muscle qui travaille s'allume en couleur.
- Un compteur « **Week 1 of 8** » qui avance, et en bas des **barres de stats** qui montent pour chacun (Time under tension, Muscle, Power).
- Fin : le verdict (« même croissance musculaire, bonus différents »). Pas de voix, juste un son, du texte très court. Tout est lisible sans le son.

**Pourquoi ça marche** : question « qui gagne ? » dès la 1re seconde ; on reste jusqu'à la semaine 8 pour voir le résultat ; c'est un jeu de pronostic (les gens commentent leur camp) ; l'info est utile → enregistrée.

**RepFix (on peut le fabriquer : animation Python/ffmpeg du moteur v3 ou Swift)**
- Lent vs rapide (version FR, notre angle : « tu fais tes reps trop vite ? »).
- 3 séances vs 5 séances par semaine, semaine 1 → 12.
- Dormir 6 h vs 8 h : barres « récup », « force », « muscle ».
- Machine vs poids libre ; échec à chaque série vs 2 reps en réserve ; 1 série lourde vs 3 séries moyennes.
- Fin : « Écris REP, l'appli te dit lequel choisir pour TOI. »

**Oh My Glow (idée pour Jean)**
- « Routine 10 étapes vs routine 3 étapes », semaine 1 → 8 : barres « régularité », « temps perdu », « motivation » (la routine courte gagne parce qu'on la tient).
- « 0,5 L vs 2 L d'eau par jour » ; « téléphone au lit vs livre au lit » (barre sommeil).
- Deux silhouettes stylisées (pas de vraies photos), couleurs de la marque.

---

## 2. POV + son tendance (sans voix)

**Pourquoi** : identification immédiate, rapide à faire, et c'est le format où le **son tendance** compte → parfait en **carrousel TikTok publié à la main** par pm (il choisit le son).
- **RepFix** : « POV : tu fais 45 min de biceps et 0 min de jambes », « POV : ton pote te regarde faire ton squat ». Dernière image : l'erreur corrigée + « écris REP ».
- **OMG** : « POV : tu as acheté 12 sérums et tu n'en utilises aucun », « POV : lundi tu commences ta routine (encore) ».

## 3. Note iPhone (carrousel)

**Pourquoi** : ressemble à une confidence, pas à une pub. Très enregistré.
- **RepFix** : « Ce que j'aurais aimé savoir à ma 1re année de salle » (7 points courts, l'appli glissée au point 5).
- **OMG** : « Mes règles glow-up qui tiennent même en période de partiels ».
- Fabrication : fond Notes (clair ou sombre), texte brut, petites imperfections autorisées. Facile avec `carrousel.py`.

## 4. Tier list (carrousel ou vidéo)

**Pourquoi** : désaccord = commentaires.
- **RepFix** : tier list des exercices pecs (S : développé incliné haltères… D : pec deck en ego lifting) ; tier list des compléments (créatine en S, « brûle-graisse » en D).
- **OMG** : tier list des habitudes du soir ; tier list des erreurs de skincare.
- Astuce : mettre un élément discutable en S.

## 5. Vrai ou faux ? (mythe / vérité avec minuteur)

**Pourquoi** : le spectateur répond dans sa tête avant la réponse (3 s de minuteur) → il reste et revoit.
- **RepFix** : « Les courbatures = la séance a marché : vrai ou faux ? », « Il faut manger toutes les 3 h ». 4-5 affirmations, 15-20 s.
- **OMG** : « Boire de l'eau suffit pour la peau : vrai ou faux ? », « Il faut changer de routine tous les mois ».

## 6. « Arrête la vidéo sur… » / choisis ton profil

**Pourquoi** : le jeu oblige à revoir la vidéo (revisionnages) et à commenter son résultat.
- **RepFix** : des programmes qui défilent vite → « arrête la vidéo, c'est ta séance de demain ». Ou « choisis ton problème : 1, 2 ou 3 » puis la correction de chacun.
- **OMG** : « arrête la vidéo sur une couleur : c'est ta tenue de demain » (l'onglet tenues de l'appli).

## 7. Vue « rayons X » : le muscle qui travaille

**Pourquoi** : visuel inédit, éducatif, enregistré. Colle à l'envie de pm d'apprendre l'anatomie.
- **RepFix** : silhouette + muscle qui s'allume pendant le mouvement ; montrer qu'en changeant un détail (coudes, prise, inclinaison) c'est un autre muscle qui s'allume. « Tu crois travailler tes pecs, en fait c'est tes épaules. »
- **OMG** : pas adapté tel quel → variante « carte du visage » (zones peau / habitudes) pour Jean.

## 8. Faux texto / conversation

**Pourquoi** : on lit les bulles une par une, la rétention est forte, ça fait rire.
- **RepFix** : conversation « mon pote vs moi » : « je fais 2 h de salle par jour » / « et tes jambes ? » / « … » → chute + REP.
- **OMG** : conversation entre copines sur la routine abandonnée le mercredi.

## 9. « Semaine 1 vs semaine 8 » / défi suivi

**Pourquoi** : une fin promise, on reste pour le résultat, et ça devient une série (on revient voir l'épisode suivant).
- **RepFix** : « Je corrige mon squat pendant 8 semaines » (épisodes courts, un détail par épisode). Pas de fausses promesses de transformation.
- **OMG** : « 7 jours de la même routine de 3 étapes » (Jean filme ou carrousel jour par jour).

## 10. Réponse à un commentaire

**Pourquoi** : chaque commentaire devient une vidéo, et TikTok la montre à ceux qui ont vu la 1re.
- **Les deux comptes** : prendre les vraies questions sous nos vidéos (pm envoie une capture) → une vidéo réponse avec la bulle du commentaire en haut.

---

## Fiches à ajouter (veille)

Format : `### NN. Nom (date, lien d'origine)` + pourquoi + idée RepFix + idée OMG.
