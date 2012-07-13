import sys
import hashlib

def phash(password):
    return hashlib.sha512(password).hexdigest()

def main():
    if len(sys.argv) != 2:
        return False
  
    print sys.argv[1]
    print phash(sys.argv[1])
    
if __name__ == '__main__':
    main()
    