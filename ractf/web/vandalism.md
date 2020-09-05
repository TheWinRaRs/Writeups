# Vandalism

Earlier on, I noticed the path `/__adminPortal` in an undefined response header.

Now with admin access, I decided to visit it.

It gave us some nice ASCII art, but in a hidden `<p>` there was some Zalgo'd text.

Using a [Zalgo Remover](https://cable.ayra.ch/zalgo/) , I retrieved the original text:  
Lorem Ipsum, but hidden inside:

## ractf{h1dd3n1npl4n3s1ght}

