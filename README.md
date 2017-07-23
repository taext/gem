# gem

**gem** is a Linux CLI for GPG string encryption
    
    gme "cleartext" [pub_key_file_name] [pub_key_file_path]
    
**gem** can also be imported as a Python module

    import gme
    
    encrypted_str = gme.main(clear_text, 
                             pubkey_file_name='pubkey.asc', 
                             pubkey_file_path='/home/dd/Documents/pubkeys/')
   (rename the file `rme` to `rme.py` before importing)


**gem** can also take piped input

    echo "Hello" | gm2
    
when called without arguments, **gem** takes input from the keyboard

    gem
    
(end keyboard input with CTRL-D)

<br>

# cle

**cle** encrypts the clipboard content in place

    cle
    
(adding a custom Linux GUI keyboard shortcut is highly recommended)
