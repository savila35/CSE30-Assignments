from steganography import Steganography

# Driver program to test Steganography
if __name__ == '__main__':
    
    score = 0

# test with input 'hello' including data attributes    
    try:
        s = Steganography()
        s.encode('fractal.jpg', 'fractal.png', 'hello', 'binary')
        assert s.text == 'hello'
        assert s.binary == '011010000110010101101100011011000110111100100011'
        print('Steganography encoding works with simple input +7/7 points')
        score += 7
    except:
        print('Steganography encoding does not work with simple input +0/7 points ')
    try:
        s.decode('fractal.png', 'binary')
        assert s.text == 'hello'
        assert s.binary == '011010000110010101101100011011000110111100100011'
        print('Steganography decoding works with simple input +8/8 points')
        score += 8
    except:
        print('Steganography decoding does not work simple input +0/8 points ')

# test with input 'Casino Royale 10:30 Order martini'
    try:
        s = Steganography()
        s.encode('fractal.jpg', 'fractal.png', 'Casino Royale 10:30 Order martini', 'binary')
        print('Steganography encoding works with any text +5/5 points')
        score += 5
    except:
        print('Steganography encoding does not work with any text +0/5 points ')
    try:
        s.decode('fractal.png', 'binary')
        print('Steganography decoding works with any text +5/5 points')
        score += 5
    except Exception:
        print('Steganography decoding does not work with any text +0/5 points ')

# additional test of data attributes
# binary should have a delimiter and text should not have a delimiter
    try:
        assert s.binary == '01000011011000010111001101101001011011100110111100100000010100100110111101111001011000010110110001100101001000000011000100110000001110100011001100110000001000000100111101110010011001000110010101110010001000000110110101100001011100100111010001101001011011100110100100100011'
        assert s.text == 'Casino Royale 10:30 Order martini'
        print('Steganography encoding/decoding works correctly +5/5 points')
        score += 5
    except:
        print('Steganography encoding/decoding does not work correctly +0/5 points ')

# output results        
    print(f'your score is {score}')
    with open('tmp', 'w') as f:
        f.write(str(score))
