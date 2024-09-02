# Most Important Tasks (MITs)

```tasks
sort by due
sort by priority
limit 5
```

---
# Tasks

```tasks
sort by due
group by function task.file.filenameWithoutExtension + (task.hasHeading ? (' > ' + task.heading) : '')
```