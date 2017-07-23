<br>
#gme

**gme** is a Linux CLI for GPG string encryption:
    
    gme "cleartext" [pub_key_file_name] [pub_key_file_path]
    
gme can also be used as a Python module:

    import gme
    
    encrypted_str = gme.gme(clear_text, 
                            pubkey_file_name='pubkey.asc', 
                            pubkey_file_path='/home/dd/Documents/pubkeys')

<br>
#gm2

**gm2** is a Linux CLI tool for piping input:

    echo "Hello" | gm2
    
gm2 also takes keyboard input when called without arguments:

    gm2
    
(end keyboard input with CTRL-D)
