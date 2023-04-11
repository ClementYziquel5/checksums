import hashlib

def sha256sum(filename,algorithm):
    if(algorithm == 'sha256'):
        h = hashlib.sha256()
    elif(algorithm == 'sha512'):
        h = hashlib.sha512()
    elif(algorithm == 'sha1'):
        h = hashlib.sha1()
    elif(algorithm == 'md5'):
        h = hashlib.md5()
    else:
        print("Error")
        print("Usage : python sha256.py path_to_file (sha256 | sha512 | sha1 | md5)")
        return
    
    if(filename == ''):
        print("Error")
        print("Usage : python sha256.py path_to_file (sha256 | sha512 | sha1 | md5)")
        return

    with open(filename,'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024),b''):
            h.update(b)
    return h.hexdigest()

if __name__ == '__main__':
    import sys
    import os
    print('')
    print('Algorithm:   ' + sys.argv[2])
    print('Hash:        ' + sha256sum(sys.argv[1],sys.argv[2]))
    print('File:        ' + os.path.abspath(sys.argv[1]))
    print('')
else :
    print("Error")
    print("Usage : python sha256.py path_to_file (sha256 | sha512 | sha1 | md5)")
