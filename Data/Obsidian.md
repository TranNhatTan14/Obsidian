---
tags:
  - Tool
  - Application
---
# Definition

Obsidian is a powerful note-taking application that emphasizes the creation and management of a personal knowledge base through its unique features. Below are the key features that distinguish Obsidian from other note-taking apps:

## Core Features

- Markdown Support
- Linking and Backlinking
- Graph View
- Canvas Feature
- Plugins and Customization
- Local Storage with Sync Options
- Templates
- Intuitive Interface
- Search Functionality
- Audio and Video Recording

# Notes

- Delete unused image and attach
- For project, should note paste code in Obsidian

# Files and Links

- Exclude folder from search

# Search

- Can search with many features

# Hotkeys

- Random note Alt R

# Highlight

- Find highlight with search ==

# Link and Tag

## Tag

The concept of dynamic folder, "not" folder

Tag is like clustering

**Tags are keywords or topics that help you quickly find the notes you want.** **A link is a relationship between two files and a mechanism that allows you to open the linked file**. A link can be a backlink, an outgoing link, a link to an external file or site and even a link to a non-existing note

I don’t use tags myself, however I do know you can put tags in YAML Frontmatter and they won’t show up in preview mode. They are searchable

### Images

# Links

[This is how you can link to a block in a note without create connection](Obsidian#Heading 3)
[Link without create connection](Machine Learning Scientist.md#^40291f)

Create connection without create new note

Tại sao minh sử dụng Obsidian thay vi Notion
1. It is simple, minh có thể tập trung vào nội dung hơn thay vì trình bày
2. Connect the dot, cách kết nối giữa các note của mình
3. Font chữ nhìn khá ổn đấy chứ

# Plugins

## Core plugins

### Templates

### Quick switcher

### Backlinks
## Community plugins

### Waypoint
### Contextual Typography
### Tasks

### [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition)

### [Dataview](https://github.com/blacksmithgu/obsidian-dataview)

List all of the files in the folder, sorted by the last time you modified the file:

```dataview
TABLE WITHOUT ID
    link(file.path, file.folder + " / " + file.name) AS "Note",
    file.mtime AS "Last modified"
FROM "/"
WHERE file.mtime >= date(today) - dur(21 days)
AND file.name != this.file.name
AND file.folder != "Vocabulary"
AND file.name != "TODOs"
SORT file.mtime DESC 
```

```dataview
TASK 
FROM "Notes" OR "People"
WHERE file.name != this.file.name
	AND file.name != "Obsidian"
SORT file.mtime DESC 
```
