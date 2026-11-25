# Projet Startups : RepFix + Oh My Glow (règles pour Claude)

Ce fichier est le cerveau partagé du projet. Il est lu par tous les Claude qui travaillent dessus :
- le Claude du **projet cloud** (claude.ai, projet « Startups ») ;
- le Claude Code du **MacBook Air** (« petit Mac ») ;
- le Claude Code du **grand Mac** (iMac, Bureau `~/Desktop/Startups/`).

Dépôt public (il sert aussi le site GitHub Pages) : **jamais de mot de passe, de jeton, de clé privée, d'adresse mail perso ni de lien signé** ici.

---

## 0. SYNCHRO : à faire à CHAQUE session (obligatoire)

1. **Au démarrage** : `git pull --rebase origin main`, puis lire `ETAT.md` (tâches en cours, qui fait quoi, dernières décisions).
2. **Avant de commencer une tâche** : ajouter une ligne « EN COURS » dans `ETAT.md` (qui, quoi, heure de Paris), puis `git commit` + `git push` tout de suite. C'est le « verrou » : l'autre Claude voit que la tâche est prise.
3. **Si une tâche est déjà « EN COURS » par l'autre** depuis moins de 12 h : ne pas la faire, prendre autre chose. Plus de 12 h : demander à pm.
4. **À la fin de chaque tâche** : mettre `ETAT.md` à jour (FAIT + résultat + ce qui reste), ajouter les nouvelles règles de pm dans ce fichier (section 9), puis commit + push.
5. **Hors ligne** : on travaille quand même, on commit en local. À la reconnexion : `git pull --rebase origin main` puis `git push`.
6. **Conflit git** : on garde les DEUX versions (on fusionne les lignes de `ETAT.md` et de `CLAUDE.md`, rien ne se perd). Pour un fichier vidéo ou une page du site : garder la version la plus récente et le noter dans `ETAT.md`. Jamais de `git push --force`.
7. **Buffer = la vérité** pour ce qui est programmé. Avant de programmer quoi que ce soit : lister les posts déjà programmés sur Buffer (deux Claude qui programment en même temps = doublons, c'est déjà arrivé le 18/11).
8. Commits courts en français : `Mac : …` ou `Cloud : …` au début du message.

Fichiers :
- `CLAUDE.md` : règles permanentes (ce fichier).
- `ETAT.md` : journal + tâches en cours + état des vidéos par compte.
- `notes-claude/` : scripts des vidéos, suivi, guides (copiés depuis le projet cloud).
- `media/` : les vidéos en ligne (servies à Buffer). `repfix/`, `ohmyglow/` : les sites.

---

## 1. Qui, comment parler

- Co-fondateurs : **pm** (Pierre-Marie) et **Jean**.
- Toujours en **français**, simple, direct, tutoiement. pm dicte à la voix : deviner le sens des mots mal transcrits.
- pm est étudiant (2 licences), très peu de temps : **minimiser ses tâches manuelles**, faire à sa place quand c'est possible.
- Outils **gratuits** uniquement. Pas de création de comptes. Jamais demander ni écrire de mot de passe / jeton.
- Demander avant de : publier quelque chose de nouveau, envoyer un message à l'extérieur, supprimer. (La routine Buffer quotidienne est déjà autorisée, voir section 5.)
- **Ne jamais supprimer** de fichier sur le Drive : déplacer dans « À trier - doublons ».

## 2. Les deux startups

**RepFix** (ex-REPS) : appli de coaching muscu. 9,99 €/mois ou 59,99 €/an, essai 7 jours, 1 mois offert, sortie début 2027. Couleurs #0B0B0F (fond), #B6FF3B (vert citron), #F2F1EC. Ne plus utiliser l'ancien site de Jean.

**Oh My Glow** : appli self-care tout-en-un (routine, peau, eau, sommeil, repas, tenues), cible féminine 15 ans et +, « en préparation ». Sur les PAGES : jamais de prix, de date, ni de promesse de résultat.

Test en cours : 2 pages « bientôt disponible » + liste d'attente.

## 3. Hébergement et liens

- Tout est sur **GitHub Pages** : compte OMG-RFX, ce dépôt → https://omg-rfx.github.io/Startup/
  - Sites : `/Startup/repfix/` et `/Startup/ohmyglow/`
  - Vidéos pour Buffer : `https://omg-rfx.github.io/Startup/media/<fichier>.mp4` (fichiers < 25 Mo).
  - Tableau de bord (tous les liens) : https://omg-rfx.github.io/Startup/ohmyglow/tableau-de-bord-x7k2q9.html
- **Netlify abandonné** (crédits épuisés), **Hostinger arrêté** : ne plus jamais les utiliser.
- Liste d'attente : Web3Forms (clé publique déjà dans le code des formulaires) → mails sur la boîte Oh My Glow. Testé OK.
- Liens courts par site (dossiers dans `repfix/` et `ohmyglow/`) : `/tt /ig /yt /sc /pub /ami` + `/tt-us /ig-us /yt-us /sc-us`. Ils redirigent avec `utm_source`. **À garder à l'identique** à chaque modification du site.
- Compteur : abacus, namespace `ohmyglow-x7k2q9`, clés `{coach|glowup}.{événement}.{source|total}`. Règle de décision : 300 visites min, gagnant = +30 %, 30 visites min par source.
- Pour vérifier qu'une vidéo est en ligne : `curl -sI https://omg-rfx.github.io/Startup/media/<fichier>` doit répondre 200 (attendre 1-2 min après le push).

## 4. Comptes réseaux

| Startup | TikTok | Instagram | YouTube | Buffer |
|---|---|---|---|---|
| RepFix | @sport2fou45 | @conseil2sportif | Sport2fou | compte biztestn2 |
| Oh My Glow | @girl70463 | @conseil2glowup | Oh2glowup | compte ohmyglowpub |

- TikTok : lien en bio non cliquable, pas de compte Business.
- CTA en fin de vidéo : « écris **REP** » / « écris **GLOW** » en commentaire → on répond « Envoyé en privé 📩 » et on envoie le lien `/tt` ou `/ig` en DM.
- Légendes : garder « Écris REP/GLOW en commentaire… » + « 🔗 Le lien de l'appli est aussi dans ma bio ». YouTube : en plus le lien en clair `https://omg-rfx.github.io/Startup/<repfix|ohmyglow>/yt/`.
- Instagram : 5 hashtags max. TikTok : cocher « contenu IA » pour RepFix (voix générée).
- ManyChat : mis de côté (à reproposer seulement si un Reel dépasse ~10 commentaires REP/GLOW).

## 5. ROUTINE QUOTIDIENNE (pm, 17/11 : « tous les jours, plus rapide »)

Chaque soir, programmer **le lendemain** sur Buffer pour les 2 startups : **10 posts par startup**.
- Cible : TikTok 5, YouTube 3, Insta 2. Mais Buffer refuse une 3e vidéo YouTube par jour → **TikTok 5, YouTube 2, Insta 3** (pm, 23/11).
- Horaires habituels : TikTok 10h, 12h, 15h, 18h, 21h30 ; YouTube 12h30, 18h ; Insta 12h, 16h, 19h30 (heure de Paris).
- Vidéos hébergées sur GitHub (jamais Netlify). **Pas de doublon par compte** : chaque vidéo ne passe qu'une fois par compte.
- Forfait Buffer gratuit : **10 posts programmés max en même temps** par compte Buffer.
- Le connecteur Buffer ne voit **qu'un compte Buffer à la fois** (pm bascule entre biztestn2 et ohmyglowpub). Ne jamais programmer du RepFix sur ohmyglowpub ni l'inverse.
- Si Buffer refuse `delete_post` : passer le post en brouillon.
- Quand une vidéo est passée sur les 3 réseaux → la déplacer dans « 2 - Vidéos déjà postées » sur le Drive.
- Mettre à jour le tableau d'usage dans `ETAT.md` après chaque programmation.

IDs Buffer (non secrets) : org RepFix 6afb4dcff0c2b572c75442f6 (TikTok 6afb4f78ece6dfde5fe8dffb, YouTube 6afb8d8aece6dfde5fecf2e5 catégorie 17, Insta 6afb4e3bece6dfde5fe8bdeb type reel) ; org OMG 6afb8dfa7943e37453702018 (TikTok 6afb8f5cece6dfde5fed2650, YouTube 6afb918bece6dfde5fed6308 catégorie 26, Insta 6afb8e6dece6dfde5fed0be3). Fuseau Europe/Paris.

## 6. D'où viennent les vidéos (Google Drive « startups », règle du 21/11)

Le dossier Drive « startups » (partagé pm + Jean) est la **source centrale des vidéos**. pm = partie FR, Jean = partie US + vidéos Oh My Glow FR. pm autorise tout transfert / modif / téléchargement sur ce Drive.
- **Oh My Glow** : on prend UNIQUEMENT les vidéos FR du Drive (« OMG FR / 1 - Vidéos à poster »). **On ne crée rien.** Les vidéos de Jean sont postées TELLES QUELLES (même avec score de beauté, calories, alcool, petites promesses : accord du collaborateur, ne plus bloquer).
- **RepFix** : 1) vidéos FR inédites du Drive ; 2) sinon vidéos US de Jean transformées en FR ; 3) sinon on crée une vidéo FR et on la dépose dans « RepFix FR / 1 - Vidéos à poster ».
- **On ne crée jamais de vidéo US.** Toujours publier via Buffer.
- Sur un Mac avec « Google Drive pour ordinateur » : le dossier est dans `~/Library/CloudStorage/GoogleDrive-<compte>/Mon Drive/startups/`. Copier avec `cp -n` (jamais écraser, jamais supprimer). Le connecteur Drive refuse les fichiers > ~3 Mo.
- Doc **« Prompts »** sur le Drive (dossier Prompts) : consignes IA de pm ET de Jean. **Le lire avant de créer ou adapter une vidéo** et respecter les règles de Jean. Y ajouter les nouvelles consignes de pm.
- IDs Drive utiles : dossier startups 1odmEbrhPuzetLSpq_iQmz78p0kRYr36Y ; doc Prompts 1sPFzCMBeuPk5g1-jMOWgje3VFYUlKapPl7mg_1M_-BA ; RepFix FR à poster 1LIV7t4SluSYNge5cPDgTCm-4cmiL7-2T, déjà postées 1ywLMmmoglM81hlC40TfAY-xLheikbARX ; OMG FR à poster 1BWu_AkpdVoFjVLDQXHtxLUpCYKopdUCm, déjà postées 1deYTg8BBZ46OitmAHUuyLaLn6XC-tOJZ ; À trier 12_Nt0cwqXcSPvt-mVRX0DZlVIALY16R8.
- Nommage OMG : `OhMyGlow_<titre>_FR.mp4` du Drive → `media/glow-NN-<titre-avec-tirets>.mp4`.

## 7. Fabriquer une vidéo RepFix

- Style @winterarc.ios : fond noir #0B0B0F, sous-titres mot par mot, rouge = erreur, vert citron #B6FF3B = solution, cartes « ERREUR 1 / ERREUR 2 / SOLUTION », musique phonk.
- Fabriquées en **Swift** sur le Mac (pas de ffmpeg sur les Mac). Moteur : grand Mac `~/Desktop/Startups/RepFix/Moteur vidéo (Swift)/` (dernier lot : `lot-2311`) ; copie dans le Drive « RepFix FR / outils ».
- Voix : ElevenLabs « Hugo – Punchy French Creator », modèle eleven_v4. **Jamais `say`.**
- Écho : toujours passer la voix en **isolation vocale ElevenLabs** puis `voixseche.swift` (passe-haut 80 Hz, expandeur) avant le mix. Pas de reverb.
- Musique ~7 dB sous la voix (volume ~0,12-0,15), bien audible. Alterner les phonks validées : `phonk-repfix-essai-1.mp3` (composée par Claude), gr0za gym music 590961, et Pixabay Aggressive Sport Phonk 464391, Hard Phonk 279363, Shade Drift Phonk 150200 (si présentes).
- Export : 1080x1920, H.264 ~12 Mbps, AAC 256k, < 25 Mo. Nom : `repfix-NN-<theme>-v2.mp4`.
- Fin : « écris REP » + « abonne-toi pour plus de conseils sport ».
- Les accroches sur **l'habitude du spectateur** font 6x plus de vues qu'un conseil technique.
- Lot standard = 5 nouvelles vidéos sur 5 thèmes jamais traités. Thèmes déjà faits (01-25) : voir `ETAT.md`.
- Livraison : `media/` du dépôt (commit + push, vérifier 200) + copie `cp -n` dans le Drive « RepFix FR / 1 - Vidéos à poster ».
- ~530 crédits ElevenLabs par voix + autant pour l'isolation : vérifier qu'il en reste.

## 8. Ce que chaque machine peut faire (connu au 23/11)

- **Cloud (projet claude.ai)** : connecteurs Buffer, Google Drive, ElevenLabs. Lit ce dépôt, mais NE PEUT PAS y pousser tant que l'appli Claude GitHub n'est pas installée sur le compte OMG-RFX : en attendant il pousse via le grand Mac (Remote Control). Ne peut pas éditer un Google Doc existant (seulement créer des fichiers). Bloqué : tiktok.com, instagram.com, pixabay, netlify.app, abacus. Ne travaille que quand pm lui écrit (ou via une tâche programmée).
- **Mac (Claude Code)** : fabrique les vidéos (Swift), copie vers le Drive local, pousse sur GitHub. Les connecteurs claude.ai (Buffer, Drive, ElevenLabs) sont normalement disponibles dans Claude Code quand on est connecté avec le même compte Claude ; sinon passer par le navigateur ou demander au cloud.
- Les chiffres TikTok / Insta : demander des captures à pm (sites bloqués pour Claude).

## 9. Nouvelles règles de pm (ajouter ici, avec la date)

- 23/11 : synchro cloud ↔ Mac via ce dépôt (`CLAUDE.md` + `ETAT.md`).
- 23/11 : le Google Drive de pm est PLEIN (quota dépassé) : les copies vers le Drive échouent tant qu'il n'a pas fait de place.
- 25/11 : carrousels TikTok = TOUJOURS en mode rappel Buffer (`schedulingType: notification`) : Buffer ne peut pas mettre de musique sur un carrousel, pm publie depuis l'appli TikTok et choisit un son tendance. Garder le format carrousel (pas de diaporama vidéo). Carrousels toujours illustrés (24/11). Carrousels RepFix et OMG programmés à la MÊME heure (18h) pour que pm soit prévenu une seule fois pour les 2 (il bascule de compte dans l'appli).
- 25/11 (soir) : carrousels TikTok livrés à pm DANS LE FIL du projet, pas par la notif Buffer (l'appli Buffer de pm n'a qu'un compte). Chaque jour avec carrousels : programmer un rappel (`send_later`) à **17h55** qui poste dans le fil les images (5 max par message) + la légende prête à coller, pour les 2 comptes ; pm publie à 18h depuis TikTok avec un son. Le post Buffer reste en rappel (il ne part pas tout seul). Horaires carrousels : TikTok 18h (les 2 comptes), Insta 16h (automatique, sans son).
