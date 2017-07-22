#!/home/dd/Anaconda3/bin/python

# gpgme.py v1.0 (July 22nd 2017)

import gnupg, sys, os


def gpg_me(pubkey_filename, clear_text, err=False):
    
    """Takes pubkey filename and clear text string, 
    returns GPG encrypted string."""
    
    gpg = gnupg.GPG()
    os.chdir('/home/dd/Documents/pubkeys')
    key_data = open(pubkey_filename).read()
    
    import_result = gpg.import_keys(key_data)
    fingerprint = import_result.results[0]['fingerprint']
    
    encr_data = gpg.encrypt(clear_text, fingerprint)
    result = str(encr_data)
    
    if err: 
        return result, encr_data.stderr
    else:
        return result
        
if __name__ == '__main__':
    
    print(gpg_me(sys.argv[1], sys.argv[2], err=False))