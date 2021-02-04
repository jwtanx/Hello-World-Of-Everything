# <center><b>Hello World Of Everything</b></center>
**_<center>Journey to the realm of Computer Science</center>_**  
> <center>Note for the future me: "Haiyaa... Why do you keep forgetting how to code?"</center>

---
### Table of Contents
- [ ] [Python](https://github.com/junwheih/Hello-World-Of-Everything/tree/main/Python)
- [ ] [HTML](https://github.com/junwheih/Hello-World-Of-Everything/tree/main//HTML)
- [ ] [Brainfuck](https://github.com/junwheih/Hello-World-Of-Everything/tree/main//Brainfuck)

---
## Hello World of Markdown
### List of references
- [Tutorial](https://guides.github.com/features/mastering-markdown/)
- [Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Markdown Chrome Extension](https://chrome.google.com/webstore/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk?hl=en)

### Table of Contents
- [x] [Text Formatting](../main/README.md#1-text-formatting)
- [x] [List](../main/README.md#2-lists)
- [x] [Code & Syntax](../main/README.md#3-code-and-syntax)
- [x] [Image](../main/README.md#4-image)
- [x] [Embedding](../main/README.md#5-embedding)
- [ ] [Special Features](../main/README.md#6-special-features)
Special features include advanced links, checklist, horizontal line, tables, inserting video without embedding

---
### 1. Text Formatting

```
To myself: <br />
> "Be **BOLD** and <ins>keep</ins> moving *forward* in your **_LIFE_**." [Double space here to skip a line]
> When in _doubt_, ~~GIVE UP~~ <u>[Google it](https://www.google.com)</u>!

[Horizontal Line] <hr /> OR --- OR ___ OR *** OR <hr style="border:2px solid blue"> </hr>
```

To myself: <br />
> "Be **BOLD** and <ins>keep</ins> moving *forward* in your **_LIFE_**."  
> When in _doubt_, ~~GIVE UP~~ <u>[Google it](https://www.google.com)</u>!

**Notes**

| Types of Formatting    | Examples
| :--------------------- | --------
| Heading 1              | `# Text`
| Heading 2              | `## Text`<br>Note: `# Text`(h1: Biggest) to `###### Text`(h6: Smallest)
| **Bold**               | `**Text**`<br>`__Text__`<br>`<b>Text</b>`<br>`<strong>Text</strong>`
| _Italic_               | `*Text*`<br>`_Text_`<br>`<i>Text</i>`<br>`<em>Text</em>`
| <u>Underline</u>       | `<u>Text</u>`<br>`<ins>Text</ins>`
| ~~Strikethrough~~      | `~~Text~~`<br>`<s>Text</s>`<br>`<del>Text</del>`
| <mark>Highlight</mark> | `<mark>Highlight</mark>` [Not supported]
| Blockquotes            | `> Text`
| `Inline code`          | ``` `Text` ```
| Web link               | `[Google](https://www.google.com)`<br>`<a href=https://www.github.com>Github</a>`

**_References_**
- [Next Line](https://stackoverflow.com/questions/33191744/how-to-add-new-line-in-markdown-presentation/33191810)
- [Underline](https://stackoverflow.com/questions/3003476/get-underlined-text-with-markdown)
- [Horizontal Line](https://www.markdownguide.org/basic-syntax/)

---
### 2. Lists

#### <b>Unordered</b>
`*` OR `-` : The bullet
```
* Item 1
* Item 2
  * Item 2.1 <-- Make sure you tap space thrice first before typing * Item 2.1
    * Item 2.1.1
  * Item 2.2
    * Item 2.2.1
    * Item 2.2.2
        * Item 2.2.2.1 <-- No more other bulleting style
* Item 3
```
* Item 1
* Item 2
  * Item 2.1
    * Item 2.1.1
  * Item 2.2
    * Item 2.2.1
    * Item 2.2.2
        * Item 2.2.2.1
* Item 3

#### <b>Ordered</b>
```
1. Item 1
1. Item 2
   1. Item 2.1 <-- Make sure you tap space thrice first before typing 1. Item 2.1
   1. Item 2.2
      1. Item 2.2.1
         1. Item 2.2.1.1 <-- No more other bulleting style
1. Item 3
   1. Item 3.1
```
1. Item 1
1. Item 2
   1. Item 2.1
   1. Item 2.2
      1. Item 2.2.1
         1. Item 2.2.1.1
1. Item 3
   1. Item 3.1

#### <b>Ordered (with a starting numbering)</b>
```
4. Item 1
1. Item 2
   3. Item 2.1
   1. Item 2.2
      2. Item 2.2.1
1. Item 3
```
4. Item 1
1. Item 2
   3. Item 2.1
   1. Item 2.2
      2. Item 2.2.1
1. Item 3

---
### 3. Code and Syntax

Overview:
<pre>
```[Programming language name]
foo & bar went to play FOOtball before becoming a BARista
```
</pre>

Example 1: With programming langauge name
<pre>
```python
def say_hello(name):
    return "hello " + name
```
</pre>
Output 1:
```python
def say_hello(name):
    return "hello " + name
```
---
Example 2: Without programming langauge name
<pre>
```
def say_hello(name):
    return "hello " + name
```
</pre>

Output 2:
```
def say_hello(name):
    return "hello " + name
```

**_References_**
- [Code Preview](https://raw.githubusercontent.com/adam-p/markdown-here/master/README.md)

---
### 4. Images
Overview:
``` 
![<Text to be shown if the image is unable to be loaded>](<Image URL> <"Title to be shown when cursor is hovered above the image">) 
```

Example 1: PNG
```
![Vim](https://raw.githubusercontent.com/junwheih/Hello-World-Of-Everything/main/.src/Markdown%20Images/Vim%20Knight.png "Vim Knight")
```
> ![Vim](https://raw.githubusercontent.com/junwheih/Hello-World-Of-Everything/main/.src/Markdown%20Images/Vim%20Knight.png "Vim Knight")</center>
---
Example 2: GIF
```
![Google](https://raw.githubusercontent.com/junwheih/Hello-World-Of-Everything/main/.src/Markdown%20Images/Google.gif "Google Gif")
```

> ![Google](https://raw.githubusercontent.com/junwheih/Hello-World-Of-Everything/main/.src/Markdown%20Images/Google.gif "Google Gif") ![Google](https://raw.githubusercontent.com/junwheih/Hello-World-Of-Everything/main/.src/Markdown%20Images/Google.gif "Google Gif") ![Google](https://raw.githubusercontent.com/junwheih/Hello-World-Of-Everything/main/.src/Markdown%20Images/Google.gif "Google Gif") ![Google](https://raw.githubusercontent.com/junwheih/Hello-World-Of-Everything/main/.src/Markdown%20Images/Google.gif "Google Gif") ![Google](https://raw.githubusercontent.com/junwheih/Hello-World-Of-Everything/main/.src/Markdown%20Images/Google.gif "Google Gif")

---
### 5. Embedding

> #### Google Map
> <center>
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d90226.6277624465!2d-157.48923146856956!3d1.9569736864334517!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x17804a9efa2123c0!2sMcDonalds!5e0!3m2!1sen!2smy!4v1611672093311!5m2!1sen!2smy" width="80%" height="250" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
</center>

> #### Spotify
> <center>
    <iframe src="https://open.spotify.com/embed/playlist/1HEsB94zQHrmE7yfFOn7t2" width="80%" height="300" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
> </center>

> #### Soundcloud
> <center>
    <iframe width="80%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/319656316&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/ilyanaazman" title="ilyana azman" target="_blank" style="color: #cccccc; text-decoration: none;">ilyana azman</a> · <a href="https://soundcloud.com/ilyanaazman/sets/best-of-mrrevillz" title="Best Of MrRevillz" target="_blank" style="color: #cccccc; text-decoration: none;">Best Of MrRevillz</a></div>
> </center>

> #### YouTube
> <center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/S96r4jdYtqM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
> </center>

**_References_**
- [Video Tutorial](https://www.youtube.com/watch?v=S96r4jdYtqM)

