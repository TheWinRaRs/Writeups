# Solved in a flash
When we download the file, we're presented with a file called flash.bin. Running ```file``` on it, we get that it's just data.
If we try and ```cat``` the file, we get a whole load of junk. Great. Lets try adn see if we can enumerate any strings from it.

```string flash.bin``` 
scroll up - yep, there's the flag.

#### Flag: ractf{Fl4shDump5Ar3VeryFun!!}
