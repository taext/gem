# gem 
(GnuPG encryption module)

<br>

**gem** as a Linux CLI tool
    
    gem "cleartext" [pub_key_file_name] [pub_key_file_path]

<br>

**gem** can also take piped string input

    echo "Hello" | gem

<br>
    
or be imported as a Python module

    import gem
    
    encrypted_str = gem.main(clear_text, 
                             pubkey_file_name='pubkey.asc', 
                             pubkey_file_path='/home/dd/Documents/pubkeys/')
   (rename or copy the file `gem` to `gem.py` before importing)

<br>    

When executed with no arguments or piped input, **gem** takes input from the keyboard

    gem
    
(end keyboard input with CTRL-D)

<br>

# cle 
(clipboard encryption)

<br>

**cle** encrypts the clipboard content in place

    cle
    
(custom keyboard shortcut execution recommended)
