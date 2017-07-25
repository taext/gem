# gem 
(GnuPG encryption module)

<br>

**gem** provides easy encryption to a default or explicit public key. It can be used 

1. as a Linux CLI tool
2. as a Python module

<br>

1a. **gem** as a Linux CLI tool
    
    gem "cleartext" [pub_key_file_name] [pub_key_file_path]

<br>

1b. **gem** accepts piped string input

    echo "Hello" | gem

<br>
    
2. **gem** as a Python module

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
