#!/usr/bin/env python3
"""Assemble data.json (lu par index.html) à partir d'un export de la base de l'agent.

Usage : python3 build_data.py <dossier_export> [sortie]
Le dossier d'export contient jobs/*.json (une offre par fichier) et meta/status.json.
"""
import json, pathlib, sys

FIELDS = ("title company city cities salary jobType telework category lang "
          "source via posted url foundAt").split()
CATS = {"tech", "cpa", "analyste"}


def body(path):
    d = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(d, dict) and isinstance(d.get("data"), dict) and not ({"title", "lastRunAt"} & d.keys()):
        return d["data"]
    return d


def main():
    src = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "data.json")
    jobs = []
    for p in sorted((src / "jobs").glob("*.json")):
        j = body(p)
        if not (j.get("title") and j.get("company") and str(j.get("url", "")).startswith("https://")):
            continue
        if j.get("category") not in CATS:
            continue
        jobs.append({k: j[k] for k in FIELDS if k in j and j[k] not in (None, "", [])})
    jobs.sort(key=lambda j: j.get("foundAt", ""), reverse=True)
    meta_file = src / "meta" / "status.json"
    meta = body(meta_file) if meta_file.exists() else {}
    meta = {k: meta[k] for k in ("lastRunAt", "sources", "newCount") if k in meta}
    meta["total"] = len(jobs)
    out.write_text(json.dumps({"meta": meta, "jobs": jobs}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{out}: {len(jobs)} offres")


if __name__ == "__main__":
    main()
