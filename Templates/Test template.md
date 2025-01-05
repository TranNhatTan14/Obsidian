<%*
let title = tp.file.title;

if (title.startsWith("Untitled")) {
  title = await tp.system.prompt("Enter a title:");
  await tp.file.rename(title);
}

tR += "---";
%>
title: <%* tR += title %>
tags:
  - Vocabulary
---
https://www.perplexity.ai/?q=cat

List the CEFR level, pronunciation (include help to pronunciation like EX-am-ple, stress information), word parts, example for each word forms including common phrases or idioms where applicable, mnemonic, Vietnamese translation of "<% tp.file.title %>" in bullet list.

<iframe
    height="500"
    width="100%"
    style="padding: 0; margin: 0;"
    src="https://www.perplexity.ai">
</iframe>

### Pronunciation

<iframe
    height="500"
    width="100%"
    style="padding: 0; margin: 0;"
    src="https://www.google.com/search?q=how+to+pronounce+<% tp.file.title %>&hl=en">
</iframe>

### Visual Association

Describe a clear mental image or simple diagram representing the word's meaning.

<iframe
    height="800"
    width="100%"
    style="padding: 0; margin: 0;"
    src="https://www.google.com/search?tbm=isch&q=<% tp.file.title %>">
</iframe>