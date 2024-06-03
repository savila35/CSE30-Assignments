# author: Sebastian Avila
# date: March 14, 2023
# file: stegonography.py is a python program that contains a steganography class. 
# input: message to be coded (strings)
# output: coded message


# steganography
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes

class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        print(image) # for debugging
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            self.codec = HuffmanCodes()
        binary = self.codec.encode(message+self.delimiter)

        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message
            self.binary = binary
            binary_l = [*self.binary]
            # your code goes here
            # you may create an additional method that modifies the image array
            i = -1
            k = -1
            for x in range(len(binary_l)):                
                if x % 3 == 0:
                    i +=1
                if i % image.shape[1]:
                    k +=1
                j = x % 3
                if binary_l[x] == '1':
                    image[k,i,j] = image[k,i,j]+1 if image[k,i,j] % 2 == 0 else image[k,i,j]
                else:
                    image[k,i,j] = image[k,i,j] if image[k,i,j] % 2 == 0 else image[k,i,j]+1
            cv2.imwrite(fileout, image)
                   
    def decode(self, filein, codec):
        image = cv2.imread(filein)
        #print(image) # for debugging      
        flag = True
        
        # convert into text
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            # your code goes here
            # you may create an additional method that extract bits from the image array
            binary_data = []
            i = -1
            k = -1
            for x in range(len([*self.binary])):
                if x % 3 == 0:
                    i +=1
                if i % image.shape[1]:
                    k +=1
                j = x % 3
                if image[k,i,j] % 2 == 0:
                    binary_data.append(0)
                else:
                    binary_data.append(1)
            # update the data attributes:
            binary_ = ''
            for x in binary_data:
                binary_ += str(x)

            self.binary = binary_             
        
    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()

if __name__ == '__main__':
    
    s = Steganography()

    s.encode('fractal.jpg', 'fractal.png', 'hello', 'binary')
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print(s.binary)
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'

    s.decode('fractal.png', 'binary')
    print(s.binary)
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'
    print('Everything works!!!')
   
