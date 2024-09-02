---
links:
  - "[[Obsidian]]"
URL: https://github.com/blacksmithgu/obsidian-dataview
---
List all of the files in the `books` folder, sorted by the last time you modified the file:

## Notes modified in last 3 weeks

```dataview
TABLE WITHOUT ID
    link(file.path, file.folder + " / " + file.name) AS "Note",
    file.mtime AS "Last modified"
FROM "/"
WHERE file.mtime >= date(today) - dur(21 days)
AND file.name != this.file.name
    AND file.name != "Inbox"
    AND file.name != "TODOs"
SORT file.mtime DESC 
```

```dataview
TABLE 
file.mtime AS "Last Modified"
frontmatter.status as "Status"
FROM "content/Zettelkasten/Books"
SORT file.mtime DESC
```

# List all tasks in un-completed projects

```dataview
TASK
FROM "content"
```

---
obsidianUIMode: preview
---

## Inline \#todo's

```query
tag:#todo
```

---

## Tasks

```dataview
TASK 
FROM "Notes" OR "People"
WHERE file.name != this.file.name
	AND file.name != "Obsidian"
SORT file.mtime DESC 
```

## Stubs

```query
tag:#stub
```