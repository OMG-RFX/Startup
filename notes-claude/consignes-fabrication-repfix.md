# Fabrication lot 23/11 (RepFix 21 à 25) – consignes pour la session Mac

Refaire EXACTEMENT comme le lot 22/11 (dossier Mac « RepFix/Moteur vidéo (Swift)/lot-2211 », vidéos 16-20) : même moteur Swift, même style winter arc (fond #0B0B0F, sous-titres mot par mot, rouge = erreur, #B6FF3B = solution, cartes ERREUR 1 / ERREUR 2 / SOLUTION), même aligneur local, même export 1080x1920 H.264 haute qualité, AAC 256k. Jamais `say`, jamais ffmpeg si le lot précédent ne l'utilisait pas.
Nouveau dossier : lot-2311 (à côté de lot-2211).

Voix (déjà isolées par ElevenLabs ; liens valables jusqu'au 23/11 ~09h heure de Paris) : télécharger avec curl, puis passer chacune dans voixseche.swift avant le mix.

Textes exacts (pour les sous-titres) : voir scripts-5-videos-repfix-23-11.md dans ce même dossier (copie ci-dessous à recevoir dans le message).
Musique (~7 dB sous la voix) : 21 gr0za, 22 phonk-repfix-essai-1, 23 gr0za, 24 essai-1, 25 gr0za (sauf si les phonks Pixabay sont maintenant dans « RepFix musiques », alors alterner les 4).

Livraison :
1. Fichiers repfix-21-que-machines-v2.mp4, repfix-22-changer-programme-v2.mp4, repfix-23-echec-v2.mp4, repfix-24-respiration-v2.mp4, repfix-25-seance-trop-longue-v2.mp4 (< 25 Mo chacun).
2. Copier dans le dépôt GitHub OMG-RFX/Startup, dossier media/, commit + push (comme le commit b51d72c du lot 16-20, via l'outil gh de « Migration GitHub/outils »). Vérifier que https://omg-rfx.github.io/Startup/media/<fichier> répond 200.
3. Copier (cp -n) dans Google Drive : ~/Library/CloudStorage/GoogleDrive-<compte>/Mon Drive/startups/…/RepFix FR/1 - Vidéos à poster/.
4. Ne rien supprimer.
