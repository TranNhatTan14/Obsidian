---
tags:
  - Obsidiian
  - Plugin
date: 2025-01-25 23:33
URL: https://github.com/blacksmithgu/obsidian-dataview
---

# Information

```dataview
TABLE WITHOUT ID
    link(file.path, file.folder + " / " + file.name) AS "Note",
    file.mtime AS "Last modified"
FROM "/"
WHERE file.mtime >= date(today) - dur(365 days)
AND file.name != this.file.name
AND file.folder != "Vocabulary"
AND file.name != "TODOs"
SORT file.mtime DESC 

---

```dataview
TABLE file.ctime AS Created, file.mtime AS Modified, file.path AS Path
FROM "" AND -#People AND -#Journal AND -#Film
WHERE !contains(file.path, "Resources/") 
AND !contains(file.path, "Archives/") 
SORT file.ctime DESC
