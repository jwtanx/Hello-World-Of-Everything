# Markdown Document

## Introduction

Markdown is a plain text formatting syntax.

Paragraphs are separated by empty lines.

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

## Character Styles

These spans result in 'em' tags:

- single asterisks
- single underscores

These spans result in 'strong' tags:

- *double asterisks*
- _double underscores_

These spans result in 'del' tags:

- ~double tildes~

## Links and Images

This is an [example inline link](https://www.actiprosoftware.com "Actipro Software") with tooltip text specified.
[This link](https://www.actiprosoftware.com) has no tooltip text specified.

URLs and e-mail addresses can be turned into links by enclosing them in angle braces:

- <https://www.actiprosoftware.com>  
- <support@microsoft.com>

[This link](#markdown-document) links to the first heading in this document via custom ID.

## Images

This is an example of an image:

![Image](https://www.microsoft.com/favicon.ico)

This is an example of an image with a link:

[![Image](https://www.google.com/favicon.ico)](https://www.google.com)

## Blockquotes

Markdown said:

> This is the first level of quoting.
>
> > This is a nested blockquote.
>
> Back to the first level.

## Lists

Unordered list using minus signs (-):

- Step 1
- Step 2
- Step 3
  - Step 3a
  - Step 3b
  - Step 3c

Unordered list using plus signs (+):

+ Step 1
+ Step 2
+ Step 3
  + Step 3a
  + Step 3b
  + Step 3c

Unordered list using asterisks (*):

* Step 1
* Step 2
* Step 3
  * Step 3a
  * Step 3b
  * Step 3c

Ordered list:

1. Step 1
1. Step 2
1. Step 3
    1. Step 3a
    1. Step 3b
    1. Step 3c

Nested (unordered within ordered) list:

1. Step 1
1. Step 2
1. Step 3
    - Step 3a
    - Step 3b
    - Step 3c

Definition list:

Term #1
: This is the definition of term #1.

Term #2
: This is the definition of term #2.

## Code Blocks

Inline `code` can be delimited with characters.

This code block is fenced with three backticks and has its language specified:

javascript
var oldUnload = window.onbeforeunload;
window.onbeforeunload = function() {
    saveCoverage();
    if (oldUnload) {
        return oldUnload.apply(this, arguments);
    }
};


This code block is fenced with three tildes and has its language specified:

~~~ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
~

This code block is created by indenting the code, but no language can be specified:

    var foo = 1;

## Tables

| Fruit  | Color  |
| ------ | ------ |
| Apples | Red    |
| Grapes | Purple |
| Lemons | Yellow |

## Horizontal Rules

Horizontal rules are formed by placing three or more hyphens, asterisks, or underscores on a line by themselves.

---

*

_

## HTML Tags

<strong>HTML tags</strong> can optionally be used in <em>Markdown</em>.

## Special Characters

Unescaped:
\ ` * _ { } [ ] ( ) # + - . !

Backslash-Escaped:
\\ \` \* \_ \{ \} \[ \] \( \) \# \+ \- \. \!