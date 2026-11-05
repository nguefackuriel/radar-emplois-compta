# Radar Emplois Compta

Page publique : https://nguefackuriel.github.io/radar-emplois-compta/

Offres d'emploi en comptabilité au Québec (technicienne / commis, comptable / CPA, analyste / contrôle), repérées chaque matin sur Indeed, Google Emplois et Guichet-Emplois. La page garde les offres trouvées dans les 45 derniers jours et permet de filtrer par type de poste, ville, période, source et télétravail.

- `index.html` : la page. Elle lit `data.json` à chaque ouverture.
- `data.json` : les offres, réécrit par l'agent après chaque balayage.
- `build_data.py` : assemble `data.json` à partir d'un export de la base de l'agent (`python3 build_data.py <dossier_export> data.json`).

Vérifiez chaque offre sur le site de l'employeur avant de postuler : certaines peuvent déjà être fermées.
