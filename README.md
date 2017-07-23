# gem

**gem** is a Linux CLI for GPG string encryption
    
    gme "cleartext" [pub_key_file_name] [pub_key_file_path]
    
**gem** can also be used as a Python module

    import gme
    
    encrypted_str = gme.main(clear_text, 
                             pubkey_file_name='pubkey.asc', 
                             pubkey_file_path='/home/dd/Documents/pubkeys/')
   (rename the file `rme` to `rme.py` before importing)


**gem** can also take piped input

    echo "Hello" | gm2
    
when called without arguments, **gm2** takes input from the keyboard

    gm2
    
(end keyboard input with CTRL-D)

<br>

# gmc

**gmc** encrypts the clipboard content in place

    gmc
    
(add a custom keyboard shortcut for convenience)
