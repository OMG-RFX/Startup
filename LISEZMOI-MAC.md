# Installer la synchro sur le MacBook (une seule fois, ~5 min)

1. Ouvre l'app **Terminal** et colle :
   ```
   cd ~/Desktop && git clone https://github.com/omg-rfx/startup.git Startup-sync && cd Startup-sync && claude
   ```
   (Si le Mac propose d'installer les « outils de développement » pour `git`, clique **Installer** puis recommence.)
2. Claude Code s'ouvre dans le dossier et lit tout seul `CLAUDE.md`. Écris-lui :
   > Configure git pour que tu puisses pousser sur GitHub (connexion par le navigateur, sans mot de passe dans le chat), puis fais la synchro.
   Il te fera cliquer sur « Authorize » dans le navigateur. C'est la seule étape à la main.
3. Ensuite, à chaque fois : Terminal → `cd ~/Desktop/Startup-sync && claude` → dis ce que tu veux (« fais la routine Buffer de demain », « on fait les vidéos RepFix »…). Il fait `git pull` au début et `git push` à la fin tout seul.

Hors connexion : il travaille quand même et synchronise dès que le Wi-Fi revient (il suffit de lui dire « synchronise »).
