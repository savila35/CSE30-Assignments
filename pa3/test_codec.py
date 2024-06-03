# from codec import Codec, CaesarCypher
# from codec import HuffmanCodes # uncomment it if a student implemented it

# Driver program to test codecs
if __name__ == '__main__':
    
    score = 0
    
# test Binary
# NOTE: binary should have a delimiter and text should not have a delimiter
    try:
        binary1 = ''
        binary2 = ''
        from codec import Codec
        text1, text2 = 'hello', 'Casino Royale 10:30 Order martini'
        c = Codec()
        binary1 = c.encode(text1+'#')
        assert binary1 == '011010000110010101101100011011000110111100100011'
        binary2 = c.encode(text2+'#')
        assert binary2 == '01000011011000010111001101101001011011100110111100100000010100100110111101111001011000010110110001100101001000000011000100110000001110100011001100110000001000000100111101110010011001000110010101110010001000000110110101100001011100100111010001101001011011100110100100100011'
        print('Binary encoding works +5/5 points')
        score += 5
    except:
        print('Binary encoding does not work +0/5 points ')
        print('Text: hello')
        print('Your output:', binary1)
        print('Correct output:', '011010000110010101101100011011000110111100100011')
        print('--------------------------------------')
        print('Text: Casino Royale 10:30 Order martini')
        print('Your output:', binary2)
        print('Correct output:', '01000011011000010111001101101001011011100110111100100000010100100110111101111001011000010110110001100101001000000011000100110000001110100011001100110000001000000100111101110010011001000110010101110010001000000110110101100001011100100111010001101001011011100110100100100011')
        print('--------------------------------------')

    try:
        assert c.decode(binary1) == text1
        assert c.decode(binary2) == text2
        print('Binary decoding works +5/5 points')
        score += 5
    except:
        print('Binary decoding does not work +0/5 points ')
        try:
            print("Your output:", c.decode(binary1))
            print("Correct output:", text1)
            print('--------------------------------------')
            print("Your output:", c.decode(binary2))
            print("Correct output:", text2)
            print('--------------------------------------')
        except:
            pass

# test CaesarCypher
# NOTE: binary should have a delimiter and text should not have a delimiter
    try:
        binary1 = ''
        binary2 = ''
        from codec import CaesarCypher
        text1, text2 = 'hello', 'Casino Royale 10:30 Order martini'
        cc = CaesarCypher()
        binary1 = cc.encode(text1+'#')
        assert binary1 == '011010110110100001101111011011110111001000100110'
        binary2 = cc.encode(text2+'#')
        assert binary2 == '01000110011001000111011001101100011100010111001000100011010101010111001001111100011001000110111101101000001000110011010000110011001111010011011000110011001000110101001001110101011001110110100001110101001000110111000001100100011101010111011101101100011100010110110000100110'
        print('Caesar cypher encoding works +8/8 points')
        score += 8
    except:
        print('Caesar Cypher encoding does not work +0/8 points ')
        print('Text: hello')
        print('Your output:', binary1)
        print('Correct output', '011010110110100001101111011011110111001000100110')
        print('--------------------------------------')
        print('Text: Casino Royale 10:30 Order martini')
        print('Your output:', binary2)
        print('Correct output:', '01000110011001000111011001101100011100010111001000100011010101010111001001111100011001000110111101101000001000110011010000110011001111010011011000110011001000110101001001110101011001110110100001110101001000110111000001100100011101010111011101101100011100010110110000100110')
        print('--------------------------------------')
    try:
        assert cc.decode(binary1) == text1
        assert cc.decode(binary2) == text2
        print('Caesar cypher decoding works +8/8 points')
        score += 8
    except:
        print('Caesar cypher decoding does not work +0/8 points ')
        try:
            print("Your output:", cc.decode(binary1))
            print("Correct output:", text1)
            print('--------------------------------------')
            print("Your output:", cc.decode(binary2))
            print("Correct output:", text2)
            print('--------------------------------------')
        except:
            pass

# test HuffmanCodes

    try:
        from codec import HuffmanCodes
        text1 = 'hello'
        h = HuffmanCodes()
        binary1 = h.encode(text1+'#')
        assert binary1 == '11011110100001'
        print('Huffman codes encoding works for a simple input +2/2 points')
        score += 2
    except:
        print('Huffman codes encoding does not work for a simple input +0/2 points ')
    try:
        assert h.decode(binary1) == text1
        print('Huffman codes decoding works for a simple input +3/3 points')
        score += 3
    except:
        print('Huffman codes decoding does not work for a simple input +0/3 points ')

    try:
        text2 = 'Casino Royale 10:30 Order martini'
        h = HuffmanCodes()
        binary2 = h.encode(text2+'#')
        assert binary2 == '011101101011111110000101000011000001001000111011001001010011001101101010010101011000110110111110111010111110011100011011111110011110000111100000'
        print('Huffman codes encoding works +2/2 points')
        score += 2
    except:
        print('Huffman codes encoding does not work +0/2 points ')
    try:
        assert h.decode(binary2) == text2
        print('Huffman codes decoding works +3/3 points')
        score += 3
    except:
        print('Huffman codes decoding does not work +0/3 points ')

# output results        
    print(f'your score is {score}')
    with open('tmp', 'w') as f:
        f.write(str(score))
