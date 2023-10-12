# Huffman-coding-for-binary-file-compression-and-decompression


Implementation of Huffman coding for both compression and decompression of binary files.

It begins by reading an input binary file, 'balloon.jpg', and compressing its contents using Huffman coding, resulting in a compressed binary file named 'balloon_compressed.bin'. During compression, the code generates Huffman codes for each unique byte pattern in the input, efficiently encoding the data. The compression ratio (CR), a measure of file size reduction, is 1.00028 which is displayed in the console. Subsequently, the code performs decompression, reading 'balloon_compressed.bin' and recreating the original binary data. The decompressed data is then written to 'balloon_decompressed.jpg'. The specific compression ratio and content of the decompressed file depend on the original 'balloon.jpg' file's content. This code showcases the Huffman coding technique, a widely-used method for lossless data compression.
